import re, os

BASE = r'D:\运营小跟班\pinmoon-website'

with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    src = f.read()

nav_match = re.search(r'(<nav>.*?</nav>)', src, re.DOTALL)
nav = nav_match.group(1)
nav = nav.replace('href="#products"', 'href="products.html"')
nav = nav.replace('href="#factory"', 'href="factory.html"')
nav = nav.replace('href="#certifications"', 'href="factory.html"')
nav = nav.replace('href="#inquiry"', 'href="contact.html"')

ft_match = re.search(r'(<footer>.*?</footer>)', src, re.DOTALL)
footer = ft_match.group(1)
footer = footer.replace('href="#products"', 'href="products.html"')
footer = footer.replace('href="#factory"', 'href="factory.html"')
footer = footer.replace('href="#inquiry"', 'href="contact.html"')

# Fix: Add active class CSS already in style.css, fix product pages
for fname in ['product-rp-hp200.html', 'product-bp-bb180.html', 'product-odm-fa220.html']:
    with open(os.path.join(BASE, fname), 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="style.css">', content, flags=re.DOTALL)
    content = re.sub(r'<nav>.*?</nav>', nav, content, count=1, flags=re.DOTALL)
    content = re.sub(r'<footer>.*?</footer>', footer, content, count=1, flags=re.DOTALL)
    
    with open(os.path.join(BASE, fname), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {fname}')

# Fix products.html
with open(os.path.join(BASE, 'products.html'), 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'<nav>.*?</nav>', nav, content, count=1, flags=re.DOTALL)
content = re.sub(r'<footer>.*?</footer>', footer, content, count=1, flags=re.DOTALL)
with open(os.path.join(BASE, 'products.html'), 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed products.html')

# Fix index.html nav links
with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('href="#products"', 'href="products.html"')
content = content.replace('href="#factory"', 'href="factory.html"')
content = content.replace('href="#certifications"', 'href="factory.html"')
content = content.replace('href="#inquiry"', 'href="contact.html"')
with open(os.path.join(BASE, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed index.html nav/footer links')

print('Done.')
