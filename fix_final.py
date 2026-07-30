import re, os

BASE = r'D:\运营小跟班\pinmoon-website'

nav_script = '''<script>
(function(){
var lang=localStorage.getItem('pinmoon_lang')||'en';
document.body.className=lang;
var btn=document.getElementById('langToggle');
if(btn)btn.textContent=lang==='en'?'\u4e2d\u6587':'English';
window.toggleLang=function(){lang=lang==='en'?'zh':'en';localStorage.setItem('pinmoon_lang',lang);document.body.className=lang;var b=document.getElementById('langToggle');if(b)b.textContent=lang==='en'?'\u4e2d\u6587':'English';};
window.toggleMenu=function(){var m=document.getElementById('navLinks');if(m)m.classList.toggle('open');};
var links=document.querySelectorAll('.nav-links a');
for(var i=0;i<links.length;i++)links[i].addEventListener('click',function(){var m=document.getElementById('navLinks');if(m)m.classList.remove('open');});
})();
</script>'''

form_script = '''<script>
(function(){
var lang=localStorage.getItem('pinmoon_lang')||'en';
document.body.className=lang;
var btn=document.getElementById('langToggle');
if(btn)btn.textContent=lang==='en'?'\u4e2d\u6587':'English';
window.toggleLang=function(){lang=lang==='en'?'zh':'en';localStorage.setItem('pinmoon_lang',lang);document.body.className=lang;var b=document.getElementById('langToggle');if(b)b.textContent=lang==='en'?'\u4e2d\u6587':'English';};
window.toggleMenu=function(){var m=document.getElementById('navLinks');if(m)m.classList.toggle('open');};
var links=document.querySelectorAll('.nav-links a');
for(var i=0;i<links.length;i++)links[i].addEventListener('click',function(){var m=document.getElementById('navLinks');if(m)m.classList.remove('open');});
var form=document.getElementById('inquiryForm');
if(form)form.addEventListener('submit',function(e){e.preventDefault();alert(lang==='en'?'Thank you! We will respond within 24 hours.':'\u611f\u8c22\uff01\u6211\u4eec\u5c06\u572824\u5c0f\u65f6\u5185\u56de\u590d\u3002');this.reset();});
})();
</script>'''

files = ['products.html', 'product-rp-hp200.html', 'product-bp-bb180.html',
         'product-odm-fa220.html', 'factory.html', 'contact.html']

for fname in files:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    use_form = fname == 'contact.html'
    script = form_script if use_form else nav_script
    
    # Find and replace the last <script> block
    # Look for pattern: <script>let lang= ... </script> or <script>(function...)</script>
    old = re.search(r'<script>.*?(let lang=|\(function).*?</script>', content, re.DOTALL)
    if old:
        content = content[:old.start()] + script + content[old.end():]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {fname}')
    else:
        print(f'SKIP {fname} - pattern not found')
        # Fallback: try to find any <script> after footer
        idx = content.rfind('<script>')
        if idx > 0:
            end = content.index('</script>', idx) + len('</script>')
            content = content[:idx] + script + content[end:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Fixed {fname} (fallback)')

print('Done')
