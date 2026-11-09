// يولّد config.js من متغيرات البيئة في Vercel أثناء البناء.
// إن لم تُضبط المتغيرات يُترك config.js كما هو (الوضع التجريبي أو القيم اليدوية).
const fs = require('fs');
const url = (process.env.SUPABASE_URL || '').trim();
const key = (process.env.SUPABASE_ANON_KEY || '').trim();
if (!url || !key) { console.log('gen-config: SUPABASE_URL/SUPABASE_ANON_KEY غير مضبوطة، تم تخطي التوليد.'); process.exit(0); }
if (/service_role/i.test(key) || key.split('.').length === 3 && JSON.parse(Buffer.from(key.split('.')[1], 'base64').toString()).role === 'service_role') {
  console.error('خطأ: هذا مفتاح service_role. استخدم anon public فقط.'); process.exit(1);
}
fs.writeFileSync('config.js', 'window.FA_CONFIG = ' + JSON.stringify({ SUPABASE_URL: url, SUPABASE_ANON_KEY: key }, null, 2) + ';\n');
console.log('gen-config: تم توليد config.js');
