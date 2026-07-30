import re, os

BASE = r'D:\运营小跟班\pinmoon-website'

new_script = '''<script>
let lang=localStorage.getItem('pinmoon_lang')||'en';
document.body.className=lang;
document.getElementById('langToggle').textContent=lang==='en'?'\\u4e2d\\u6587':'English';
function toggleLang(){lang=lang==='en'?'zh':'en';localStorage.setItem('pinmoon_lang',lang);document.body.className=lang;document.getElementById('langToggle').textContent=lang==='en'?'\\u4e2d\\u6587':'English';}
function toggleMenu(){document.getElementById('navLinks').classList.toggle('open');}
document.querySelectorAll('.nav-links a').forEach(l=>l.addEventListener('click',()=>document.getElementById('navLinks').classList.remove('open')));
</script>'''

form_script = '''<script>
let lang=localStorage.getItem('pinmoon_lang')||'en';
document.body.className=lang;
document.getElementById('langToggle').textContent=lang==='en'?'\\u4e2d\\u6587':'English';
function toggleLang(){lang=lang==='en'?'zh':'en';localStorage.setItem('pinmoon_lang',lang);document.body.className=lang;document.getElementById('langToggle').textContent=lang==='en'?'\\u4e2d\\u6587':'English';}
function toggleMenu(){document.getElementById('navLinks').classList.toggle('open');}
document.querySelectorAll('.nav-links a').forEach(l=>l.addEventListener('click',()=>document.getElementById('navLinks').classList.remove('open')));
document.getElementById('inquiryForm').addEventListener('submit',function(e){e.preventDefault();alert(lang==='en'?'Thank you! We will respond within 24 hours.':'\\u611f\\u8c22\\uff01\\u6211\\u4eec\\u5c06\\u572824\\u5c0f\\u65f6\\u5185\\u56de\\u590d\\u3002');this.reset();});
</script>'''

files = ['index.html', 'products.html', 'product-rp-hp200.html', 'product-bp-bb180.html',
         'product-odm-fa220.html', 'factory.html', 'contact.html']

for fname in files:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    use_form = fname in ['index.html', 'contact.html']
    script = form_script if use_form else new_script
    
    # Replace the script block using string split
    idx_start = content.index('<script>')
    idx_end = content.index('</script>', idx_start) + len('</script>')
    content = content[:idx_start] + script + content[idx_end:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {fname}')

print('Done - language now persists across pages')
