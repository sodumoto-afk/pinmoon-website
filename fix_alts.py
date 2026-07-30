import re, os
BASE = r'D:\运营小跟班\pinmoon-website'

alt_map = {
    'product-2.jpg': 'RP-HP200 hotel pocket spring mattress OEM bulk manufacturer China',
    'product-3.jpg': 'BP-BB180 bonnell spring B&B dormitory mattress wholesale Foshan factory',
    'product-1.jpg': 'ODM-FA220 custom OEM foldable apartment mattress private label manufacturer',
    'factory.jpg': 'Pinmoon Foshan mattress factory manufacturer OEM bulk orders CE RoHS ISO 9001',
    'cert-rohs-ms3007.jpg': 'RoHS certificate Pinmoon mattress manufacturer OEM Foshan factory',
    'cert-ce-ms3039.jpg': 'CE certificate Pinmoon mattress manufacturer OEM Foshan factory',
    'cert-iso9001.jpg': 'ISO 9001 certificate Pinmoon mattress manufacturer OEM Foshan factory',
}

files = ['index.html', 'products.html', 'product-rp-hp200.html', 'product-bp-bb180.html',
         'product-odm-fa220.html', 'factory.html', 'contact.html', 'certifications.html']

for fname in files:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = False
    for img, new_alt in alt_map.items():
        pattern = r'(src="{}")\s+alt="[^"]*"'.format(re.escape(img))
        replacement = 'src="{}" alt="{}"'.format(img, new_alt)
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            updated = True
    if updated:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed alts: ' + fname)
print('Done')
