import os
import re

directory = r"c:\Users\rites\Downloads\Interior Designer & Architecture 1"

new_header = """<header style="width: 100%; z-index: 1000; position: fixed; top: 0; display: flex; flex-direction: column; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <!-- Top Contact Bar -->
    <div class="top-bar" style="background-color: var(--color-primary); color: #fff; padding: 0.5rem 5%; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; flex-wrap: wrap; gap: 1rem;">
        <div class="contact-info" style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
            <a href="tel:+918368151207" style="color: #fff; text-decoration: none; display: flex; align-items: center; gap: 0.5rem;">
                📞 +91 8368151207
            </a>
            <a href="mailto:ayaninteriordecorators@gmail.com" style="color: #fff; text-decoration: none; display: flex; align-items: center; gap: 0.5rem;">
                ✉️ ayaninteriordecorators@gmail.com
            </a>
        </div>
        <div class="social-links" style="display: flex; gap: 1rem; align-items: center;">
            <a href="#" aria-label="Facebook" style="color: #fff;"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
            <a href="#" aria-label="Instagram" style="color: #fff;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
        </div>
    </div>
    
    <!-- Main Navigation Bar -->
    <div class="main-nav" style="background-color: rgba(255, 255, 255, 0.98); padding: 1rem 5%; display: flex; justify-content: space-between; align-items: center; flex-wrap: nowrap; overflow-x: auto;">
        <div class="logo" style="flex-shrink: 0; margin-right: 1rem;">
            <a href="index.html">
                <img src="assets/images/logo.png" alt="Ayan Interior Decorators Logo" style="height: 85px; max-width: 100%; object-fit: contain;">
            </a>
        </div>
        <nav style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: nowrap; white-space: nowrap;">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="services.html">Services</a>
            <a href="portfolio.html">Portfolio</a>
            <a href="process.html">Process</a>
            <a href="testimonials.html">Testimonials</a>
            <a href="blog.html">Blog</a>
            <a href="contact.html" class="cta-button" style="padding: 0.5rem 1.5rem; font-size: 0.8rem; margin-left: 0.5rem; color: #fff !important; min-width: max-content;">Contact Us</a>
        </nav>
    </div>
</header>"""

new_footer = """<footer style="background-color: #111; color: #fff; padding: 4rem 5% 1rem;">
    <div class="footer-container" style="display: flex; justify-content: space-between; flex-wrap: wrap; text-align: left; gap: 2rem; max-width: 1400px; margin: 0 auto;">
        <div class="footer-col" style="flex: 1; min-width: 250px;">
            <div style="background-color: #fff; padding: 0.5rem 1rem; display: inline-block; border-radius: 4px; margin-bottom: 1.5rem;">
                <img src="assets/images/logo.png" alt="Ayan Interior Decorators Logo" style="height: 70px; display: block; object-fit: contain;">
            </div>
            <p style="margin-bottom: 1rem; line-height: 1.6; color: rgba(255, 255, 255, 0.8);">With over 10 years of industry excellence, we build dream homes that inspire living. Elegance, creativity, and steadfast functionality in every space.</p>
            <p style="font-weight: bold; color: var(--color-accent-gold); margin-bottom: 0.5rem;">✓ 700+ Projects Handled</p>
            <p style="font-weight: bold; color: var(--color-accent-gold);">✓ 400+ Happy Clients</p>
        </div>
        
        <div class="footer-col" style="flex: 1; min-width: 250px;">
            <h3 style="margin-bottom: 1.5rem; color: #fff; font-family: var(--font-heading); font-size: 1.5rem;">Connect With Us</h3>
            <p style="margin-bottom: 0.5rem; color: rgba(255,255,255,0.8);"><strong>Phone:</strong> <a href="tel:+918368151207" style="color: inherit; text-decoration: none;">+91 8368151207</a></p>
            <p style="margin-bottom: 0.5rem; color: rgba(255,255,255,0.8);"><strong>Email:</strong> <a href="mailto:ayaninteriordecorators@gmail.com" style="color: inherit; text-decoration: none;">ayaninteriordecorators@gmail.com</a></p>
            <p style="margin-bottom: 1rem; color: rgba(255,255,255,0.8);"><strong>Location:</strong> Mumbai, India</p>
            
            <div class="social-links" style="display: flex; gap: 1rem; margin-top: 1.5rem;">
                <a href="#" aria-label="Facebook" style="color: var(--color-accent-gold); transition: color 0.3s;"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
                <a href="#" aria-label="Instagram" style="color: var(--color-accent-gold); transition: color 0.3s;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
                <a href="#" aria-label="LinkedIn" style="color: var(--color-accent-gold); transition: color 0.3s;"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
            </div>
        </div>
        
        <div class="footer-col" style="flex: 1; min-width: 250px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <h2 style="font-size: 1.8rem; margin-bottom: 1.5rem; color: #fff; font-family: var(--font-heading);">Ready to Transform Your Space?</h2>
            <a href="contact.html" class="cta-button" style="display: inline-block;">Consult With Us Today</a>
        </div>
    </div>
    <div style="text-align: center; margin-top: 3rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1.5rem;">
        <p style="color: rgba(255,255,255,0.5); margin: 0; font-size: 0.9rem;">&copy; 2026 Ayan Interior Decorators. All rights reserved.</p>
    </div>
    
    </div>
</footer>"""

floating_buttons = """
    <!-- Floating Contact Buttons -->
    <div class="floating-contact">
        <a href="https://wa.me/918368151207" class="float-whatsapp" target="_blank" aria-label="WhatsApp">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>
            </svg>
        </a>
        <a href="tel:+918368151207" class="float-phone" aria-label="Call Us">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor">
                <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
            </svg>
        </a>
    </div>
"""

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update active nav indicator in the new header based on file
        current_header = new_header
        # Basic replacement: "index.html" -> "index.html" class="active" if filename is index.html
        if filename != 'index.html':
            current_header = current_header.replace(f'href="{filename}"', f'href="{filename}" class="active"')
        else:
            # Need to uniquely identify the first Home link
            current_header = current_header.replace('<a href="index.html">Home</a>', '<a href="index.html" class="active">Home</a>')


        # Remove old floating buttons if they exist
        content = re.sub(r'\s*<!-- Floating Contact Buttons -->\s*<div class="floating-contact">.*?</div>\s*', '\n', content, flags=re.DOTALL | re.IGNORECASE)

        # Replace header start to header end
        content = re.sub(r'<header[^>]*>.*?</header>', current_header, content, count=1, flags=re.DOTALL | re.IGNORECASE)

        # Replace footer
        content = re.sub(r'<footer.*?</footer>', new_footer, content, count=1, flags=re.DOTALL | re.IGNORECASE)

        # Insert floating buttons right before body
        content = re.sub(r'</body>', floating_buttons + '\n</body>', content, flags=re.IGNORECASE)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {filename}")

print(f"Total files updated: {count}")
