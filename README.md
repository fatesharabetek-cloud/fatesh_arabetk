# فتش عربيتك — النسخة النهائية (Static + Supabase + Vercel)

## المزايا
- بحث حقيقي (لوحة/شاسيه) عبر `search_vehicles`؛ يُرجع «وُجد/لم يوجد» فقط حمايةً للخصوصية. عند عدم الظهور: توجيه للتسجيل أولاً ثم قناة التلجرام.
- حفظ البلاغات والكشوفات في Supabase مع رفع الصور مضغوطة (Storage خاص) ورقم بلاغ من الخادم.
- رسوم التسجيل (12,000 جنيه — بنكك 2113114 باسم سعد قسم الباري) في شاشة البلاغات الذكية ونافذة التسجيل (ابحث عن `fee-box`).
- بيع وشراء العربات المشلعة (`salvage_requests`) وطلب قطع غيار هيونداي (`spare_parts_leads`) مع رسائل واتساب جاهزة؛ عمود `chassis_match` ينبّهك إن كان شاسيه المعروض مسجلاً كبلاغ.
- قسم «تابعنا»: تلجرام وفيسبوك وتيك توك.
- Google Analytics 4 (G-RZ0BCZ4KWD) مع أحداث: search (found/not_found)، submit_report، parts_request، salvage_request، open_register، social_click، screen_view. لا تُرسل أرقام الشاسيه/اللوحات ولا الهواتف.
- PWA قابل للتثبيت، و`/api/healthcheck` + Vercel Cron يومي لمنع إيقاف Supabase المجاني.
- ترويسات أمان (CSP) في `vercel.json`؛ إن استخدمت نطاق Supabase مخصصاً أضفه إلى `connect-src`.

## النشر
1. Supabase: أعد تشغيل المشروع `fetesh-arabiytak` (Unpause).
2. SQL Editor: نفّذ `supabase/migration_intake.sql` (راجع أعمدة `vehicles`).
3. ضع Project URL وanon key في `config.js`.
4. Vercel > Environment Variables: `SUPABASE_URL` و`SUPABASE_ANON_KEY` و`CRON_SECRET`.
5. ارفع الملفات في جذر المستودع، ثم افتح `/api/healthcheck` للتأكد.

لا تضع مفتاح service_role في أي ملف أمامي. Vercel Hobby يسمح بـ Cron مرة يومياً.

## SEO
- صفحات ثابتة مولّدة بالسكربت `tools/build_seo.py` (شغّله بعد أي تعديل على المحتوى: `python3 tools/build_seo.py`)، ويولّد كذلك `sitemap.xml` و`robots.txt` و`404.html` وصور OG.
- روابط التطبيق العميقة: `/#search` و`/#register` و`/#salvage` و`/#parts`.
- لتغيير النطاق لاحقاً عدّل المتغير `SITE` في السكربت وروابط `canonical` في `index.html`.
