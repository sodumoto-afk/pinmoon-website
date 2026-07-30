import re, os

BASE = r'D:\运营小跟班\pinmoon-website'

with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    src = f.read()

# Read shared assets
with open(os.path.join(BASE, 'style.css'), 'r', encoding='utf-8') as f:
    css = f.read()

# Extract nav (already updated)
nav_match = re.search(r'(<nav>.*?</nav>)', src, re.DOTALL)
nav = nav_match.group(1)
nav = nav.replace('href="#products"', 'href="products.html"')
nav = nav.replace('href="#factory"', 'href="factory.html"')
nav = nav.replace('href="#certifications"', 'href="factory.html"')
nav = nav.replace('href="#inquiry"', 'href="contact.html"')

# Extract footer (already updated)
ft_match = re.search(r'(<footer>.*?</footer>)', src, re.DOTALL)
footer = ft_match.group(1)
footer = footer.replace('href="#products"', 'href="products.html"')
footer = footer.replace('href="#factory"', 'href="factory.html"')
footer = footer.replace('href="#inquiry"', 'href="contact.html"')

# Scripts
nav_script = '''<script>
let lang='en';
function toggleLang(){lang=lang==='en'?'zh':'en';document.body.className=lang;document.getElementById('langToggle').textContent=lang==='en'?'\\u4e2d\\u6587':'English';}
function toggleMenu(){document.getElementById('navLinks').classList.toggle('open');}
document.querySelectorAll('.nav-links a').forEach(l=>l.addEventListener('click',()=>document.getElementById('navLinks').classList.remove('open')));
</script>'''

form_script = '''<script>
let lang='en';
function toggleLang(){lang=lang==='en'?'zh':'en';document.body.className=lang;document.getElementById('langToggle').textContent=lang==='en'?'\\u4e2d\\u6587':'English';}
function toggleMenu(){document.getElementById('navLinks').classList.toggle('open');}
document.querySelectorAll('.nav-links a').forEach(l=>l.addEventListener('click',()=>document.getElementById('navLinks').classList.remove('open')));
document.getElementById('inquiryForm').addEventListener('submit',function(e){e.preventDefault();alert(lang==='en'?'Thank you! We will respond within 24 hours.':'\\u611f\\u8c22\\uff01\\u6211\\u4eec\\u5c06\\u572824\\u5c0f\\u65f6\\u5185\\u56de\\u590d\\u3002');this.reset();});
</script>'''

def make_page(title, desc, canonical, body, active, use_form=False):
    h = '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
    h += '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
    h += f'<title>{title}</title>\n'
    h += f'<meta name="description" content="{desc}">\n'
    h += '<meta name="robots" content="index,follow">\n'
    h += f'<link rel="canonical" href="https://www.pinmoonmattress.com{canonical}">\n'
    h += f'<link rel="alternate" hreflang="en" href="https://www.pinmoonmattress.com{canonical}">\n'
    h += f'<link rel="alternate" hreflang="zh" href="https://www.pinmoonmattress.com{canonical}">\n'
    h += '<link rel="stylesheet" href="style.css">\n'
    h += '</head>\n<body class="en">\n\n'
    
    # Nav with active class
    n = nav.replace('<a href="products.html"', '<a href="products.html"' + (' class="active"' if 'product' in active else ''))
    n = n.replace('<a href="factory.html"', '<a href="factory.html"' + (' class="active"' if active == 'factory' else ''))
    n = n.replace('<a href="contact.html"', '<a href="contact.html"' + (' class="active"' if active == 'contact' else ''))
    
    h += n + '\n\n' + body + '\n\n' + footer + '\n\n'
    h += (form_script if use_form else nav_script) + '\n</body>\n</html>'
    return h

# ===== FACTORY PAGE =====
factory_body = '''
<header class="page-header" style="margin-top:68px;padding:60px 40px 40px;text-align:center;background:var(--cream);">
    <div class="section-tag"><span class="en">Our Factory</span><span class="zh">我们的工厂</span></div>
    <h1><span class="en">World-Class Manufacturing</span><span class="zh">世界级制造基地</span></h1>
</header>

<section style="padding:60px 40px;">
    <div class="section-inner" style="max-width:1000px;">
        <div class="factory-layout">
            <div class="factory-image">
                <img src="factory.jpg" alt="Foshan Yexuan Furniture Pinmoon Factory" style="width:100%;display:block;border-radius:20px;">
            </div>
            <div class="factory-content">
                <h2><span class="en">Foshan Yexuan Furniture Manufacture Co., Ltd</span><span class="zh">佛山市叶轩家具制造有限公司</span></h2>
                <p class="en">Specializing in furniture engineering and bulk project orders — we serve hotel chains, property developers, B&Bs, and apartment operators with reliable volume production and competitive factory-direct pricing.</p>
                <p class="zh">主营家具工程类批量订单——服务酒店连锁、地产开发商、民宿和公寓运营商，稳定量产能力和工厂直供价格。</p>
                <p class="en">From raw material selection to final packaging, we maintain full control over the production process — ensuring consistent quality, on-time delivery, and competitive pricing for our global partners.</p>
                <p class="zh">从原材料筛选到成品包装，全程品控——为全球合作伙伴保障稳定的品质、准时交付和竞争力价格。</p>
                <div class="factory-stats">
                    <div class="factory-stat"><div class="number">10,000</div><div class="label">m2 <span class="en">Facility</span><span class="zh">厂房</span></div></div>
                    <div class="factory-stat"><div class="number">30</div><div class="label"><span class="en">Skilled Staff</span><span class="zh">技术工人</span></div></div>
                    <div class="factory-stat"><div class="number">15+</div><div class="label"><span class="en">Years Exp.</span><span class="zh">年经验</span></div></div>
                </div>
            </div>
        </div>
    </div>
</section>

<section style="padding:60px 40px;background:#fff;">
    <div class="section-inner" style="max-width:1000px;">
        <div class="section-header">
            <div class="section-tag"><span class="en">Quality Assurance</span><span class="zh">品质保障</span></div>
            <h2><span class="en">International Certifications</span><span class="zh">国际认证资质</span></h2>
            <p><span class="en">All our products and processes meet the highest global standards.</span><span class="zh">所有产品与生产流程符合全球最高标准。</span></p>
            <div class="section-divider"></div>
        </div>
        <div class="certs-grid">
            <div class="cert-card"><img src="cert-rohs-ms3007.jpg" alt="RoHS Certificate"><div class="cert-body"><h4>RoHS</h4></div></div>
            <div class="cert-card"><img src="cert-ce-ms3039.jpg" alt="CE Certificate"><div class="cert-body"><h4>CE</h4></div></div>
            <div class="cert-card"><img src="cert-iso9001.jpg" alt="ISO 9001 Certificate"><div class="cert-body"><h4>ISO 9001</h4></div></div>
        </div>
    </div>
</section>

<section style="padding:40px 40px 60px;text-align:center;">
    <a href="contact.html" class="btn btn-primary" style="font-size:16px;padding:16px 48px;"><span class="en">Contact Our Factory</span><span class="zh">联系我们工厂</span></a>
</section>
'''

factory_html = make_page(
    'Pinmoon Factory | Foshan Mattress Manufacturer | CE RoHS ISO 9001 Certified',
    'Visit Pinmoon factory in Foshan, Guangdong. 10,000 sqm facility, 30 skilled staff, CE RoHS ISO 9001 certified. Bulk mattress OEM for hotels, B&Bs, schools, villas.',
    '/factory', factory_body, 'factory'
)

with open(os.path.join(BASE, 'factory.html'), 'w', encoding='utf-8') as f:
    f.write(factory_html)
print(f'factory.html: {len(factory_html)} bytes')

# ===== CONTACT PAGE =====
contact_body = '''
<header class="page-header" style="margin-top:68px;padding:60px 40px 40px;text-align:center;background:var(--cream);">
    <div class="section-tag"><span class="en">Contact Us</span><span class="zh">联系我们</span></div>
    <h1><span class="en">Let's Talk Business</span><span class="zh">我们聊聊合作</span></h1>
    <p><span class="en">Whether you're a distributor, retailer, hotel chain, or brand looking for OEM/ODM — tell us your requirements and we'll respond within 24 hours.</span><span class="zh">无论您是经销商、零售商、酒店集团，还是寻求 OEM/ODM 的品牌——告知需求，24 小时内回复。</span></p>
</header>

<section id="inquiry" style="background:var(--cream);">
    <div class="section-inner" style="max-width:1000px;">
        <div class="inquiry-layout">
            <div class="inquiry-info">
                <h2><span class="en">Contact Information</span><span class="zh">联系信息</span></h2>
                <p><span class="en">Reach us directly for bulk orders, custom OEM projects, or factory visits.</span><span class="zh">直接联系我们咨询批量订单、定制 OEM 项目或工厂参观。</span></p>
                <div class="inquiry-detail"><div class="icon">*</div><div class="info"><strong>Email</strong><span>sodumoto@gmail.com</span></div></div>
                <div class="inquiry-detail"><div class="icon">*</div><div class="info"><strong>WhatsApp</strong><span>+86 13088813138</span></div></div>
                <div class="inquiry-detail"><div class="icon">*</div><div class="info"><strong><span class="en">Address</span><span class="zh">地址</span></strong><span class="en">No.4 Zhenye East 1st Road, Shatou Industrial Park, Jiujiang Town, Nanhai District, Foshan, Guangdong, China</span><span class="zh">广东省佛山市南海区九江镇沙头工业园振业东一路4号首层之一</span></div></div>
            </div>
            <div class="inquiry-form">
                <h3><span class="en">Send an Inquiry</span><span class="zh">发送询盘</span></h3>
                <form id="inquiryForm">
                    <div class="form-group"><label><span class="en">Your Name *</span><span class="zh">您的姓名 *</span></label><input type="text" required></div>
                    <div class="form-group"><label><span class="en">Company Name</span><span class="zh">公司名称</span></label><input type="text"></div>
                    <div class="form-group"><label><span class="en">Email *</span><span class="zh">邮箱 *</span></label><input type="email" required></div>
                    <div class="form-group"><label><span class="en">Product Interest</span><span class="zh">感兴趣的产品</span></label>
                        <select><option value=""><span class="en">-- Select --</span><span class="zh">-- 请选择 --</span></option><option>RP-HP200 (Hotel Pocket)</option><option>BP-BB180 (Bonnell B&B)</option><option>ODM-FA220 (Foldable Apartment)</option><option><span class="en">Custom OEM/ODM</span><span class="zh">定制 OEM/ODM</span></option></select></div>
                    <div class="form-group"><label><span class="en">Estimated Order Quantity</span><span class="zh">预计订单量</span></label><input type="text" placeholder="e.g. 1x40HQ container"></div>
                    <div class="form-group"><label><span class="en">Message *</span><span class="zh">留言 *</span></label><textarea required></textarea></div>
                    <button type="submit" class="form-submit"><span class="en">Send Inquiry</span><span class="zh">发送询盘</span></button>
                </form>
            </div>
        </div>
    </div>
</section>
'''

contact_html = make_page(
    'Contact Pinmoon | Mattress OEM Inquiry | Bulk Order Quote',
    'Contact Pinmoon mattress factory for bulk OEM orders. Email sodumoto@gmail.com, WhatsApp +86 13088813138. Foshan, Guangdong, China. Hotel, B&B, school, villa mattress supplier.',
    '/contact', contact_body, 'contact', use_form=True
)

with open(os.path.join(BASE, 'contact.html'), 'w', encoding='utf-8') as f:
    f.write(contact_html)
print(f'contact.html: {len(contact_html)} bytes')

print('All pages created.')
