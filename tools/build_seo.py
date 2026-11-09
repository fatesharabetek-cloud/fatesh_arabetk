# -*- coding: utf-8 -*-
"""يولّد صفحات SEO الثابتة + sitemap.xml + صور OG. تشغيل: python3 tools/build_seo.py"""
import os, json, glob
SITE='https://sudan-car.vercel.app'; DATE='2026-11-02'; ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TG='https://t.me/sudan_car'; FB='https://www.facebook.com/share/1EwiMK83ef/'; TT='https://www.tiktok.com/@sudan_car1'
ORG={"@type":"Organization","@id":SITE+"/#org","name":"فتش عربيتك","url":SITE+"/","logo":SITE+"/icons/icon-512.png","sameAs":[TG,FB,TT]}
def P(slug,title,desc,h1,intro,secs,cta,rel,kind='Service',img='search',faq=None,svc=None):
    return dict(slug=slug,title=title,desc=desc,h1=h1,intro=intro,secs=secs,cta=cta,rel=rel,kind=kind,img=img,faq=faq or [],svc=svc)
S='ابحث الآن'
pages=[
P('lost-cars-sudan','البحث عن السيارات المفقودة في السودان | فتش عربيتك','محرك بحث للسيارات والعربات المفقودة في السودان: ابحث برقم الشاسي أو اللوحة في الكشوفات المسجلة، وسجّل عربيتك لنتابع معك تلقائياً.',
 'البحث عن السيارات المفقودة في السودان',
 'فتش عربيتك محرك بحث يساعدك على معرفة هل ظهرت عربيتك المفقودة في الكشوفات المنشورة للعربات المستردة، بإدخال رقم الشاسي أو رقم اللوحة فقط.',
 [('كيف يعمل البحث',['افتح التطبيق واختر البحث برقم الشاسي أو برقم اللوحة.',['أدخل الرقم كما هو مكتوب في أوراقك.','يفحص المحرك الرقم في الكشوفات المسجلة لدينا.','عند وجود تطابق محتمل نتواصل معك للتحقق قبل تسليم أي معلومة.','إن لم يظهر الرقم بعد، تسجّل عربيتك ونتابع لك تلقائياً مع كل كشف جديد.']]),
  ('لماذا لا نعرض تفاصيل التطابق علناً',['حمايةً لخصوصية أصحاب العربات لا نعرض في نتيجة البحث بيانات المالك أو أرقام الهواتف. تظهر لك فقط إشارة إلى وجود تطابق محتمل، ثم نتحقق منك مباشرة.']),
  ('مناسب لعربات كل الولايات',['البحث لا يتقيد بالمدينة؛ يناسب عربات الخرطوم وأم درمان وبحري والجزيرة ونهر النيل وبقية ولايات السودان.']),
  ('نصائح لمن فقد عربيته',[['احتفظ بصورة واضحة لرقم الشاسي ولأوراق العربية.','سجّل بلاغك مبكراً حتى تُطابَق عربيتك مع أي كشف جديد.','تابع قناة التلجرام للاطلاع على الكشوفات يدوياً.']])],
 (S,'/#search'),['search-by-chassis','search-by-plate','report-lost-car','guides/how-to-check-chassis-number'],'Service','search',
 [('هل البحث مجاني؟','نعم، البحث برقم الشاسي أو اللوحة مجاني. التسجيل للمتابعة التلقائية برسوم رمزية.'),('هل تضمنون العثور على عربيتي؟','لا. نعرض ما ورد في الكشوفات المتاحة لدينا، وتُضاف كشوفات جديدة باستمرار، لذلك لا نقدّم ضماناً بالعثور على كل عربية.')],'البحث عن السيارات المفقودة في السودان'),
P('search-by-chassis','البحث برقم الشاسي في السودان | فتش عربيتك','ابحث عن عربيتك برقم الشاسي في الكشوفات المسجلة لدى فتش عربيتك. اعرف أين تجد رقم الشاسي وكيف تكتبه بشكل صحيح للبحث.',
 'البحث برقم الشاسي في السودان',
 'رقم الشاسي هو الرقم الأدق لتمييز العربية، ولذلك هو أفضل وسيلة للبحث عنها في الكشوفات. أدخله كاملاً وسنفحصه لك في قاعدتنا.',
 [('أين أجد رقم الشاسي؟',['غالباً يوجد في أحد هذه الأماكن:',['أسفل الزجاج الأمامي من جهة السائق.','ملصق عند إطار باب السائق.','داخل حجرة المحرك.','أوراق العربية.']]),
  ('كيف أكتبه للبحث؟',['اكتب الرقم كما هو دون مسافات أو شرطات، ويمكنك استخدام الأرقام العربية أو الإنجليزية. الأخطاء في حرف أو رقم واحد تعني عدم التطابق، فراجع الرقم بعناية.']),
  ('ماذا يحدث بعد البحث؟',['إن وُجد تطابق محتمل نتحقق منك ونسلّمك المعلومة. وإن لم يظهر الرقم، يمكنك تسجيل عربيتك لنتابع تلقائياً مع أي كشف جديد.'])],
 ('ابحث برقم الشاسي','/#search'),['search-by-plate','lost-cars-sudan','guides/how-to-check-chassis-number','report-lost-car'],'Service','search',None,'البحث برقم الشاسي'),
P('search-by-plate','البحث برقم اللوحة في السودان | فتش عربيتك','ابحث عن عربية برقم اللوحة في كشوفات فتش عربيتك المسجلة. طريقة كتابة رقم اللوحة وما تفعله إن لم يظهر نتيجة.',
 'البحث برقم اللوحة في السودان',
 'إن كانت عربيتك مسجلة بلوحة، فيكفيك رقمها للبدء. نفحص رقم اللوحة في الكشوفات المسجلة لدينا ونخبرك بوجود تطابق محتمل.',
 [('متى أستخدم رقم اللوحة؟',['استخدمه عندما لا يتوفر لديك رقم الشاسي الآن. وللنتيجة الأدق يفضّل البحث بالشاسي أيضاً متى توفر.']),
  ('نصائح لكتابة رقم اللوحة',[['اكتب الرقم كما هو دون مسافات زائدة.','تأكد من الحروف والأرقام بالترتيب نفسه.','جرّب البحث برقم الشاسي إن لم تجد نتيجة.']]),
  ('لم تظهر نتيجة؟',['الكشوفات تُضاف باستمرار؛ سجّل عربيتك لنتابع معك تلقائياً، أو ابحث يدوياً في قناة التلجرام.'])],
 ('ابحث برقم اللوحة','/#search'),['search-by-chassis','lost-cars-sudan','report-lost-car'],'Service','search',None,'البحث برقم اللوحة'),
P('report-lost-car','تسجيل بلاغ سيارة مفقودة في السودان | فتش عربيتك','سجّل بلاغ عربيتك المفقودة في فتش عربيتك ليتم الربط التلقائي مع أي كشف جديد. ما البيانات المطلوبة وكيف نحمي خصوصيتك.',
 'تسجيل بلاغ سيارة مفقودة',
 'التسجيل يجعلنا نتابع عربيتك نيابةً عنك: عند ظهور كشف جديد يحتوي رقماً مطابقاً نتواصل معك.',
 [('ماذا تحتاج لتسجيل بلاغ؟',[['نوع العربية وبياناتها الأساسية.','رقم الشاسي و/أو رقم اللوحة.','رقم هاتف للتواصل.','رسوم التسجيل الرمزية.']]),
  ('كيف نعامل بياناتك؟',['نراجع كل بلاغ بشرياً قبل اعتماده، ولا ننشر أرقام الشاسي أو اللوحات أو الهواتف على صفحات عامة.']),
  ('بعد التسجيل',['عند ظهور تطابق في كشف جديد نتواصل معك للتحقق قبل أي خطوة. لا نضمن ظهور تطابق، لكننا نتابعه معك.'])],
 ('سجّل بلاغك','/#register'),['lost-cars-sudan','search-by-chassis','search-by-plate'],'Service','search',None,'تسجيل بلاغ سيارة مفقودة'),
P('sell-salvage-cars','بيع سيارة مشلعة في السودان | فتش عربيتك','اعرض عربيتك المشلعة أو المتضررة عبر فتش عربيتك: نفحص الشاسيه ونطابق عرضك مع طلبات المشترين وننسّق الاتفاق.',
 'بيع سيارة مشلعة في السودان',
 'إن عندك عربية مشلعة أو متضررة أو ناقصة قطع، تعرضها عبر الإدارة فنفحص الشاسيه أولاً ثم نبحث لك عن مشترٍ مناسب.',
 [('كيف تعرض عربيتك؟',[['املأ الماركة والموديل وسنة الصنع.','أدخل رقم الشاسيه (إلزامي).','حدد حالة الأوراق: شهادة بحث أو أورنيك إجراءات أو بدون لوحات.','اكتب المكان والسعر المطلوب أو «قابل للتفاوض» ووصفاً مختصراً للحالة.','أرسل العرض للإدارة عبر واتساب مع 4 صور وصورة الشاسيه.']]),
  ('لماذا نفحص الشاسيه؟',['لتفادي ربط مشترين بعربات مسجلة كمفقودة، ولحماية الطرفين. أي عرض يتطلب فحص الشاسيه قبل المتابعة.']),
  ('دور الإدارة',['نسجّل العرض، ونطابقه مع الطلبات المتاحة، وننسّق الاتفاق بين البائع والمشتري مقابل رسوم وساطة يُتفق عليها.'])],
 ('اعرض عربيتك','/#salvage'),['buy-salvage-cars','hyundai-salvage-cars','toyota-salvage-cars','guides/before-buying-salvage-car'],'Service','salvage',None,'وساطة بيع السيارات المشلعة'),
P('buy-salvage-cars','شراء سيارات مشلعة في السودان | فتش عربيتك','تبحث عن سيارة مشلعة أو هيكل أو ماكينة؟ ارفع طلبك لفتش عربيتك ونخبرك عند توفر عرض مطابق ومفحوص الشاسيه.',
 'شراء سيارات مشلعة في السودان',
 'لأصحاب الورش والسمكرة وتجار السكراب والأفراد: حدّد ما تحتاجه ونوافيك عند توفر عرض مطابق ومفحوص الشاسيه.',
 [('ماذا تطلب؟',[['العربية المطلوبة: الماركة والموديل وسنة تقريبية.','الغرض: بودي وسمكرة، أو ماكينة وميكانيك، أو سكراب كامل.','مدينة الاستلام المفضلة لتقليل تكلفة السطحة.','ميزانية تقريبية.']]),
  ('كيف نساعدك؟',['نطابق طلبك مع العروض المتاحة، ونزوّدك بتفاصيل المعاينة وموقع العربية، وننسّق عملية المبايعة بين الطرفين.']),
  ('قبل أن تشتري',['اقرأ دليلنا المختصر لفحص العربية المشلعة قبل الدفع.'])],
 ('ارفع طلب شراء','/#salvage'),['sell-salvage-cars','hyundai-salvage-cars','toyota-salvage-cars','guides/before-buying-salvage-car'],'Service','salvage',None,'وساطة شراء السيارات المشلعة'),
P('hyundai-salvage-cars','سيارات هيونداي مشلعة في السودان | فتش عربيتك','تبحث عن توسان أو أفانتي أو أكسنت أو كليك مشلعة؟ اعرض أو اطلب عبر فتش عربيتك، ونفحص الشاسيه قبل الربط.',
 'سيارات هيونداي مشلعة في السودان',
 'هيونداي من أكثر الماركات تداولاً في سوق العربات المشلعة. سواء عندك توسان أو أفانتي أو أكسنت أو كليك للبيع، أو تحتاج هيكلاً أو ماكينة، نربط بين الطرفين.',
 [('الموديلات التي يتكرر طلبها',[['توسان مشلعة للبيع أو للشراء.','أفانتي مشلعة للبيع أو للشراء.','أكسنت مشلعة (بودي أو ماكينة).','كليك مشلعة.']]),
  ('أنت بائع أم مشترٍ؟',['البائع يرسل بيانات عربيته مع رقم الشاسيه. المشتري يحدد الموديل والغرض والميزانية. نفحص الشاسيه ونطابق ونتواصل مع الطرفين.']),
  ('تحتاج قطع غيار؟',['إن كان طلبك قطعاً محددة لهيونداي فيمكنك إرسال طلب قطع غيار من التطبيق.'])],
 ('اعرض أو اطلب','/#salvage'),['sell-salvage-cars','buy-salvage-cars','toyota-salvage-cars'],'Service','salvage',None,'وساطة السيارات المشلعة هيونداي'),
P('toyota-salvage-cars','سيارات تويوتا مشلعة وكوريلا مشلعة | فتش عربيتك','عرض وطلب سيارات تويوتا المشلعة في السودان، ومنها الكوريلا، عبر فتش عربيتك مع فحص الشاسيه ووساطة الإدارة.',
 'سيارات تويوتا مشلعة في السودان',
 'تويوتا، ومنها الكوريلا، مطلوبة دائماً بين أصحاب الورش والمشترين. اعرض عربيتك أو اطلب ما تحتاجه ونتولى الفحص والمطابقة.',
 [('كوريلا مشلعة',['إن كانت عندك كوريلا مشلعة للبيع فأرسل الموديل والسنة ورقم الشاسيه وحالة الأوراق. وإن كنت تبحث عن كوريلا للسمكرة أو الماكينة فاكتب غرضك وميزانيتك.']),
  ('ما نحتاجه منك',[['ماركة وموديل وسنة الصنع.','رقم الشاسيه.','حالة الأوراق والمكان.','السعر أو الميزانية.']]),
  ('الفحص والوساطة',['نفحص الشاسيه أولاً، ثم نطابق العرض مع الطلبات المتاحة وننسّق المبايعة.'])],
 ('اعرض أو اطلب','/#salvage'),['sell-salvage-cars','buy-salvage-cars','hyundai-salvage-cars'],'Service','salvage',None,'وساطة السيارات المشلعة تويوتا'),
P('guides','أدلة ومقالات السيارات في السودان | فتش عربيتك','أدلة عملية: كيف تجد رقم الشاسي وتتحقق منه، وماذا تفحص قبل شراء سيارة مشلعة في السودان.',
 'أدلة ومقالات فتش عربيتك','مقالات قصيرة وعملية تساعدك في البحث عن عربيتك وفي التعامل الآمن مع سوق العربات المشلعة.',
 [('الأدلة المتاحة',[['<a href="/guides/how-to-check-chassis-number">كيف تعرف رقم الشاسي وتتحقق منه</a>','<a href="/guides/before-buying-salvage-car">قبل شراء سيارة مشلعة: 8 نقاط تفحصها</a>']])],
 (S,'/#search'),['lost-cars-sudan','sell-salvage-cars','buy-salvage-cars'],'CollectionPage','guides'),
P('guides/how-to-check-chassis-number','كيف تعرف رقم الشاسي وتتحقق منه | فتش عربيتك','أين يوجد رقم الشاسي في السيارة؟ كيف تقرؤه وتتأكد من تطابقه ولماذا يهم عند البحث عن عربية مفقودة أو شراء عربية.',
 'كيف تعرف رقم الشاسي وتتحقق منه',
 'رقم الشاسي هو بصمة العربية. معرفته وكتابته صحيحة هي أول خطوة في البحث عن عربية مفقودة أو في التأكد قبل شراء عربية.',
 [('أماكن رقم الشاسي',[['أسفل الزجاج الأمامي من جهة السائق.','على ملصق عند إطار باب السائق.','في حجرة المحرك.','في أوراق العربية.']]),
  ('كيف تقرؤه؟',['الأرقام الحديثة غالباً من 17 خانة من الأرقام والحروف، ولا تُستخدم فيها الحروف I وO وQ. أما العربات الأقدم فقد يكون رقمها أقصر. صوّره بوضوح وانسخه حرفاً بحرف.']),
  ('تأكد من التطابق',['قارن الرقم الموجود على العربية بالمكتوب في أوراقها. اختلاف الأرقام أو أثر كشط أو تغيير علامة تحذير، فلا تكمل أي صفقة قبل التوضيح.']),
  ('ثم ماذا؟',['ابحث بالرقم في فتش عربيتك. وإن كنت تشتري عربية مشلعة فاقرأ دليل الفحص قبل الشراء.'])],
 ('ابحث برقم الشاسي','/#search'),['search-by-chassis','guides/before-buying-salvage-car','lost-cars-sudan'],'Article','guides'),
P('guides/before-buying-salvage-car','قبل شراء سيارة مشلعة: 8 نقاط تفحصها | فتش عربيتك','8 نقاط عملية تفحصها قبل شراء سيارة مشلعة أو متضررة في السودان: الشاسيه، الأوراق، الهيكل، الماكينة، والاتفاق على السعر.',
 'قبل شراء سيارة مشلعة: 8 نقاط تفحصها',
 'شراء عربية مشلعة قد يوفر المال، لكنه يتطلب فحصاً دقيقاً. هذه نقاط عملية تقلل مخاطر الصفقة.',
 [('قائمة الفحص',[['تحقق من رقم الشاسي وتطابقه مع الأوراق، واسأل عن حالته عندنا.','اطلب فهم حالة الأوراق: شهادة بحث أو أورنيك إجراءات أو بدون لوحات.','تأكد من هوية البائع وصلته بالعربية.','افحص الهيكل والشاسيه بحثاً عن ضرر أو لحام أو انحراف.','افحص الماكينة والجيربوكس إن كانت الغاية منهما.','حدد القطع الناقصة بالتفصيل واحسب تكلفتها.','اتفق على السعر وطريقة الاستلام والنقل كتابةً.','لا تدفع قبل المعاينة والتأكد، والتقِ في مكان معروف.']]),
  ('هل تريد وسيطاً؟',['فتش عربيتك تفحص الشاسيه وتنسّق بين البائع والمشتري، ويمكنك البدء من صفحة الشراء أو البيع.'])],
 ('ارفع طلبك','/#salvage'),['buy-salvage-cars','sell-salvage-cars','guides/how-to-check-chassis-number'],'Article','guides'),
]
IDX={p['slug']:p for p in pages}
CSS='*{box-sizing:border-box}body{margin:0;font-family:Tahoma,Arial,sans-serif;background:#F6F7FB;color:#1b2540;line-height:1.9}a{color:#E5231B}header{background:#0F1E45;color:#fff;padding:12px 16px;display:flex;justify-content:space-between;align-items:center}header a{color:#fff;text-decoration:none;font-weight:800}header .app{background:#E5231B;padding:8px 14px;border-radius:12px;font-size:14px}main{max-width:760px;margin:0 auto;padding:18px 16px 30px}nav.bc{font-size:13px;color:#667}nav.bc a{color:#667}h1{font-size:26px;color:#0F1E45;line-height:1.5;margin:10px 0}h2{font-size:19px;color:#0F1E45;margin:24px 0 6px}h3{font-size:16px;margin:14px 0 2px}p,li{font-size:16px}.cta{background:#0F1E45;color:#fff;border-radius:18px;padding:18px;margin:26px 0;text-align:center}.cta a{display:inline-block;background:#E5231B;color:#fff;text-decoration:none;font-weight:800;padding:12px 26px;border-radius:14px;margin-top:6px}.rel a{display:block;padding:6px 0}footer{border-top:1px solid #dde;padding:18px 16px;text-align:center;font-size:14px;color:#556}footer a{margin:0 8px}'
def esc(x): return x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def lnk(slug): return '/'+slug
def render(p):
    u=SITE+'/'+p['slug']; img=SITE+'/icons/og-%s.png'%p['img']
    parts=[('الرئيسية',SITE+'/')]
    if p['slug'].startswith('guides/'): parts.append(('الأدلة',SITE+'/guides'))
    parts.append((p['h1'],u)) if p['slug']!='guides' else parts.append(('الأدلة',u))
    bc=[{"@type":"ListItem","position":i+1,"name":n,"item":l} for i,(n,l) in enumerate(parts)]
    g=[ORG,{"@type":"WebSite","name":"فتش عربيتك","url":SITE+"/","inLanguage":"ar","publisher":{"@id":SITE+"/#org"}},{"@type":"BreadcrumbList","itemListElement":bc}]
    if p['kind']=='Service': g.append({"@type":"Service","name":p['svc'],"serviceType":p['svc'],"description":p['desc'],"provider":{"@id":SITE+"/#org"},"areaServed":{"@type":"Country","name":"السودان"},"url":u})
    elif p['kind']=='Article': g.append({"@type":"Article","headline":p['h1'],"description":p['desc'],"inLanguage":"ar","datePublished":DATE,"dateModified":DATE,"author":{"@id":SITE+"/#org"},"publisher":{"@id":SITE+"/#org"},"mainEntityOfPage":u,"image":img})
    else: g.append({"@type":p['kind'],"name":p['h1'],"description":p['desc'],"url":u,"inLanguage":"ar"})
    ld=json.dumps({"@context":"https://schema.org","@graph":g},ensure_ascii=False)
    body=''
    for h,items in p['secs']:
        body+='<h2>%s</h2>'%h
        for it in items:
            body+=('<ul>%s</ul>'%''.join('<li>%s</li>'%i for i in it)) if isinstance(it,list) else '<p>%s</p>'%it
    if p['faq']:
        body+='<h2>أسئلة شائعة</h2>'+''.join('<h3>%s</h3><p>%s</p>'%(q,a) for q,a in p['faq'])
    rel=''.join('<a href="%s">%s</a>'%(lnk(s),IDX[s]['h1']) for s in p['rel'])
    bch=' › '.join('<a href="%s">%s</a>'%(l.replace(SITE,'') or '/',n) for n,l in parts[:-1])+' › '+esc(parts[-1][0])
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p['title']}</title><meta name="description" content="{p['desc']}">
<link rel="canonical" href="{u}"><meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{'article' if p['kind']=='Article' else 'website'}"><meta property="og:locale" content="ar_AR"><meta property="og:site_name" content="فتش عربيتك"><meta property="og:title" content="{p['title']}"><meta property="og:description" content="{p['desc']}"><meta property="og:url" content="{u}"><meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{p['title']}"><meta name="twitter:description" content="{p['desc']}"><meta name="twitter:image" content="{img}">
<meta name="theme-color" content="#0F1E45"><link rel="icon" href="/icons/icon-192.png"><link rel="manifest" href="/manifest.webmanifest">
<script type="application/ld+json">{ld}</script>
<style>{CSS}</style>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RZ0BCZ4KWD"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-RZ0BCZ4KWD');</script>
</head><body><header><a href="/">فتش عربيتك</a><a class="app" href="/">افتح التطبيق</a></header>
<main><nav class="bc" aria-label="مسار التنقل">{bch}</nav><article><h1>{p['h1']}</h1><p>{p['intro']}</p>{body}</article>
<div class="cta"><div>{p['h1']}</div><a href="{p['cta'][1]}">{p['cta'][0]}</a></div>
<h2>اقرأ أيضاً</h2><div class="rel">{rel}</div></main>
<footer><div><a href="/">الرئيسية</a><a href="/lost-cars-sudan">السيارات المفقودة</a><a href="/sell-salvage-cars">بيع المشلعة</a><a href="/buy-salvage-cars">شراء المشلعة</a><a href="/guides">الأدلة</a></div>
<div style="margin-top:8px"><a href="{TG}" rel="noopener" target="_blank">تلجرام</a><a href="{FB}" rel="noopener" target="_blank">فيسبوك</a><a href="{TT}" rel="noopener" target="_blank">تيك توك</a></div>
<p style="font-size:12px">لا تُنشر أرقام الشاسي أو اللوحات أو الهواتف الخاصة بالبلاغات على هذه الصفحات.</p></footer></body></html>'''
for p in pages:
    path=os.path.join(ROOT,p['slug']+'.html'); os.makedirs(os.path.dirname(path),exist_ok=True)
    open(path,'w',encoding='utf-8').write(render(p))
urls=[SITE+'/']+[SITE+'/'+p['slug'] for p in pages]
open(os.path.join(ROOT,'sitemap.xml'),'w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>%s</loc><lastmod>%s</lastmod></url>\n'%(u,DATE) for u in urls)+'</urlset>\n')
open(os.path.join(ROOT,'robots.txt'),'w').write('User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /config.js\n\nSitemap: %s/sitemap.xml\n'%SITE)
open(os.path.join(ROOT,'404.html'),'w',encoding='utf-8').write('<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>الصفحة غير موجودة | فتش عربيتك</title><style>%s</style></head><body><header><a href="/">فتش عربيتك</a></header><main><h1>الصفحة غير موجودة</h1><p>الرابط غير صحيح أو تم نقل الصفحة.</p><div class="rel"><a href="/">الرئيسية</a><a href="/lost-cars-sudan">البحث عن السيارات المفقودة</a><a href="/sell-salvage-cars">بيع وشراء المشلعة</a><a href="/guides">الأدلة</a></div></main></body></html>'%CSS)
# صور OG
from PIL import Image, ImageDraw, ImageFont
fp=([f for f in glob.glob('/usr/share/fonts/**/*.[to]tf',recursive=True) if 'Arabic' in f and 'Bold' in f]+glob.glob('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))[0]
OG={'home':('فتش عربيتك','السيارات المفقودة والمشلعة في السودان'),'search':('البحث عن السيارات المفقودة','برقم الشاسي أو رقم اللوحة'),'salvage':('بيع وشراء السيارات المشلعة','فحص الشاسيه ووساطة الإدارة'),'guides':('أدلة ومقالات','فتش عربيتك')}
for k,(a,b) in OG.items():
    im=Image.new('RGB',(1200,630),'#0F1E45');d=ImageDraw.Draw(im);d.rectangle([0,590,1200,630],fill='#E5231B')
    def fit(t,sz):
        while sz>20 and d.textlength(t,font=ImageFont.truetype(fp,sz),direction='rtl',language='ar')>1040: sz-=4
        return ImageFont.truetype(fp,sz)
    d.text((600,250),a,font=fit(a,84),fill='white',anchor='mm',direction='rtl',language='ar')
    d.text((600,390),b,font=fit(b,46),fill='#C8D0E8',anchor='mm',direction='rtl',language='ar')
    im.save(os.path.join(ROOT,'icons','og-%s.png'%k),optimize=True)
print('built',len(pages),'pages; font',os.path.basename(fp))
