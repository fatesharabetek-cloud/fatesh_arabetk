-- فتش عربيتك: جداول الاستقبال العام + دوال آمنة (شغّله في Supabase > SQL Editor)
-- ملاحظة: دالتا search_vehicles وsubmit_salvage تفترضان جدولاً public.vehicles فيه plate_number و chassis_number.
-- إن كانت أسماء جدولك/أعمدتك مختلفة عدّلها في الدالتين فقط.

-- جدول المركبات المسجلة (يُنشأ فقط إن لم يكن موجوداً)
create table if not exists public.vehicles(
  id bigint generated always as identity primary key,
  plate_number text,
  chassis_number text,
  created_at timestamptz not null default now()
);
alter table public.vehicles enable row level security;
revoke all on public.vehicles from anon, authenticated;

create table if not exists public.web_contributions(
  id bigint generated always as identity primary key,
  ref_code text generated always as ('FA-'||lpad(id::text,6,'0')) stored,
  kind text not null check (kind in ('single_vehicle','listing')),
  data jsonb not null,
  image_paths text[] not null default '{}',
  status text not null default 'pending' check (status in ('pending','approved','rejected')),
  created_at timestamptz not null default now()
);
create table if not exists public.spare_parts_leads(
  id bigint generated always as identity primary key,
  ref_code text generated always as ('SP-'||lpad(id::text,6,'0')) stored,
  car_model text not null, car_year text, parts text not null, whatsapp text not null,
  status text not null default 'new' check (status in ('new','contacted','invoiced','closed')),
  created_at timestamptz not null default now()
);
create table if not exists public.salvage_requests(
  id bigint generated always as identity primary key,
  ref_code text generated always as ('SV-'||lpad(id::text,6,'0')) stored,
  kind text not null check (kind in ('sell','buy')),
  data jsonb not null,
  chassis_match boolean,
  status text not null default 'new' check (status in ('new','checked','listed','matched','closed','rejected')),
  created_at timestamptz not null default now()
);
alter table public.web_contributions enable row level security;
alter table public.spare_parts_leads enable row level security;
alter table public.salvage_requests enable row level security;
revoke all on public.web_contributions, public.spare_parts_leads, public.salvage_requests from anon, authenticated;

create or replace function public.submit_contribution(p jsonb) returns text
language plpgsql security definer set search_path=public as $$
declare r text;
begin
  if length(p::text) > 20000 then raise exception 'too large'; end if;
  if p->>'kind' not in ('single_vehicle','listing') then raise exception 'bad kind'; end if;
  if coalesce(p->'data'->>'phone','') = '' then raise exception 'phone required'; end if;
  insert into public.web_contributions(kind,data,image_paths)
  values (p->>'kind', p->'data', coalesce(array(select jsonb_array_elements_text(p->'images')),'{}'))
  returning ref_code into r;
  return r;
end $$;

create or replace function public.submit_parts_lead(p jsonb) returns text
language plpgsql security definer set search_path=public as $$
declare r text;
begin
  if length(coalesce(p->>'parts','')) not between 2 and 1000 then raise exception 'bad parts'; end if;
  if coalesce(p->>'whatsapp','') !~ '^\+?[0-9]{9,15}$' then raise exception 'bad phone'; end if;
  insert into public.spare_parts_leads(car_model,car_year,parts,whatsapp)
  values (left(p->>'car_model',60), left(p->>'car_year',8), p->>'parts', p->>'whatsapp')
  returning ref_code into r;
  return r;
end $$;

create or replace function public.submit_salvage(p jsonb) returns text
language plpgsql security definer set search_path=public as $$
declare r text; ch text; m boolean;
begin
  if length(p::text) > 5000 then raise exception 'too large'; end if;
  if p->>'kind' not in ('sell','buy') then raise exception 'bad kind'; end if;
  if p->>'kind'='sell' then
    ch := upper(regexp_replace(coalesce(p->'data'->>'chassis',''),'[\s\-_.]','','g'));
    if length(ch) < 5 then raise exception 'chassis required'; end if;
    select exists(select 1 from public.vehicles where upper(regexp_replace(chassis_number,'[\s\-_.]','','g')) = ch) into m;
  end if;
  insert into public.salvage_requests(kind,data,chassis_match) values (p->>'kind', p->'data', m) returning ref_code into r;
  return r;
end $$;

-- بحث لا يُرجع إلا (وُجد/لم يوجد) كي لا تُكشف بيانات أحد علناً
create or replace function public.search_vehicles(p_kind text, p_q text) returns jsonb
language plpgsql security definer set search_path=public stable as $$
declare q text := upper(regexp_replace(coalesce(p_q,''),'[\s\-_.]','','g')); f boolean;
begin
  if length(q) < case when p_kind='plate' then 3 else 5 end then return jsonb_build_object('found',false); end if;
  if p_kind='plate' then
    select exists(select 1 from public.vehicles where upper(regexp_replace(plate_number,'[\s\-_.]','','g')) = q) into f;
  else
    select exists(select 1 from public.vehicles where upper(regexp_replace(chassis_number,'[\s\-_.]','','g')) = q) into f;
  end if;
  return jsonb_build_object('found',f);
end $$;

create or replace function public.ping() returns timestamptz
language sql security definer set search_path=public as $$ select now() $$;

revoke all on function public.submit_contribution(jsonb), public.submit_parts_lead(jsonb), public.submit_salvage(jsonb), public.search_vehicles(text,text), public.ping() from public;
grant execute on function public.submit_contribution(jsonb), public.submit_parts_lead(jsonb), public.submit_salvage(jsonb), public.search_vehicles(text,text), public.ping() to anon, authenticated;

insert into storage.buckets(id,name,public,file_size_limit,allowed_mime_types)
values ('contribution-images','contribution-images',false,3145728,array['image/jpeg'])
on conflict (id) do nothing;
drop policy if exists "anon upload contribution images" on storage.objects;
create policy "anon upload contribution images" on storage.objects
  for insert to anon with check (bucket_id='contribution-images');
