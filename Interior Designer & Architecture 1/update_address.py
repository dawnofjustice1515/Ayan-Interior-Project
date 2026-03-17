import os
import re

directory = r"c:\Users\rites\Downloads\Interior Designer & Architecture 1"

footer_old = r"<strong>Location:</strong> Mumbai, India"
footer_new = "<strong>Location:</strong> Dreams apartment, shop no8, sector 6a, plot no 48 Kamothe, Navi Mumbai 410209"

contact_address_old = "123 Design Avenue, Creative City, ST 12345"
contact_address_new = "Dreams apartment, shop no8, sector 6a, plot no 48 Kamothe, Navi Mumbai 410209"

map_old = r'<iframe\s+src="https://www\.google\.com/maps/embed\?pb=[^"]+"\s+width="100%"\s+height="500"\s+style="border:0;\s*filter:\s*grayscale\(100%\);"\s+allowfullscreen=""\s+loading="lazy"></iframe>'
map_new = '<iframe src="https://maps.google.com/maps?q=Dreams%20apartment,%20shop%20no8,%20sector%206a,%20plot%20no%2048%20Kamothe,%20Navi%20Mumbai%20410209&t=&z=15&ie=UTF8&iwloc=&output=embed" width="100%" height="500" style="border:0; filter: grayscale(100%);" allowfullscreen="" loading="lazy"></iframe>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content

        content = content.replace(footer_old, footer_new)
        content = content.replace(contact_address_old, contact_address_new)
        content = re.sub(map_old, map_new, content)
        
        if original_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
