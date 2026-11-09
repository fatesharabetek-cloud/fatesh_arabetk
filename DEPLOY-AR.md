# دليل الرفع والربط (10 دقائق)

## 1) Supabase
1. supabase.com/dashboard ← افتح مشروع `fetesh-arabiytak` ← إن كان متوقفاً اضغط **Restore/Unpause**.
2. **SQL Editor** ← New query ← الصق كامل `supabase/migration_intake.sql` ← **Run**.
   (إن كان لديك جدول `vehicles` فعلاً فلن يتغير، وإلا يُنشأ فارغاً.)
3. **Project Settings ← API**: انسخ `Project URL` و `anon public key`. (لا تنسخ service_role أبداً.)

## 2) GitHub
1. github.com/new ← اسم المستودع `fatesh-arabetak` ← Private ← Create (بدون README).
2. من مجلد المشروع على الكمبيوتر:
```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/USERNAME/fatesh-arabetak.git
git push -u origin main
```
   أو بدون أوامر: في صفحة المستودع اضغط **uploading an existing file** واسحب كل الملفات.

## 3) Vercel
1. vercel.com/new ← **Import** مستودع GitHub ← Framework: **Other** (اترك الإعدادات، فهي في vercel.json).
2. قبل Deploy افتح **Environment Variables** وأضف:
   - `SUPABASE_URL` = Project URL
   - `SUPABASE_ANON_KEY` = anon public key
   - `CRON_SECRET` = أي نص عشوائي طويل
3. **Deploy**. أثناء البناء يُولَّد `config.js` تلقائياً من المتغيرين.

## 4) التحقق
- افتح `https://موقعك.vercel.app/api/healthcheck` ← يجب أن يظهر `{"ok":true}`.
- جرّب بحثاً وإرسال بلاغ، ثم راجع الجدولين `web_contributions` و`salvage_requests` في Supabase ← Table Editor.
- أي push جديد إلى `main` ينشر تلقائياً.

## ملاحظات
- النطاق المخصص: Vercel ← Settings ← Domains، ثم حدّث `SITE` في `tools/build_seo.py` وروابط canonical.
- إن غيّرت نطاق Supabase إلى مخصص أضفه إلى `connect-src` في `vercel.json`.
