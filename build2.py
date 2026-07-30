import re, os

BASE = r'D:\运营小跟班\pinmoon-website'

with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    src = f.read()

# Extract CSS
css_match = re.search(r'<style>(.*?)</style>', src, re.DOTALL)
css = css_match.group(1) if css_match else ''

css += '\n.nav-links a.active{color:var(--accent);font-weight:600;}\n'
css += '\n.page-header h1{font-size:36px;color:var(--dark-brown);margin:12px 0 8px;}\n'
css += '.page-header p{font-size:15px;color:var(--text-light);max-width:600px;margin:0 auto;}\n'
css += '@media(max-width:768px){.page-header h1{font-size:24px;}.page-header p{font-size:13px;}}\n'

with open(os.path.join(BASE, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(css)
print(f'style.css created: {len(css)} bytes')

# Extract nav
nav_match = re.search(r'(<nav>.*?</nav>)', src, re.DOTALL)
nav = nav_match.group(1)

# Update nav links
nav = nav.replace('href="#products"', 'href="products.html"')
nav = nav.replace('href="#factory"', 'href="factory.html"')
nav = nav.replace('href="#certifications"', 'href="factory.html"')
nav = nav.replace('href="#inquiry"', 'href="contact.html"')

# Extract footer
ft_match = re.search(r'(<footer>.*?</footer>)', src, re.DOTALL)
footer = ft_match.group(1)

# Update footer links
footer = footer.replace('href="#products"', 'href="products.html"')
footer = footer.replace('href="#factory"', 'href="factory.html"')
footer = footer.replace('href="#certifications"', 'href="factory.html"')
footer = footer.replace('href="#inquiry"', 'href="contact.html"')

print(f'Nav: {len(nav)} chars, Footer: {len(footer)} chars, CSS: {len(css)} bytes')
print('Done')
