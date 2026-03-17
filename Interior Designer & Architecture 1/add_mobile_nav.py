import os
import re

directory = r"c:\Users\rites\Downloads\Interior Designer & Architecture 1"

new_header = """<header>
    <!-- Top Contact Bar -->
    <div class="top-bar">
        <div class="contact-info">
            <a href="tel:+918368151207">
                📞 +91 8368151207
            </a>
            <a href="mailto:ayaninteriordecorators@gmail.com">
                ✉️ ayaninteriordecorators@gmail.com
            </a>
        </div>
        <div class="social-links">
            <a href="#" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
            <a href="#" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
        </div>
    </div>
    
    <!-- Main Navigation Bar -->
    <div class="main-nav">
        <div class="logo">
            <a href="index.html">
                <img src="assets/images/logo.png" alt="Ayan Interior Decorators Logo">
            </a>
        </div>
        
        <!-- Hamburger Menu Button -->
        <button class="menu-toggle" aria-label="Toggle Navigation">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
        </button>

        <nav class="nav-links">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="services.html">Services</a>
            <a href="portfolio.html">Portfolio</a>
            <a href="process.html">Process</a>
            <a href="testimonials.html">Testimonials</a>
            <a href="blog.html">Blog</a>
            <a href="contact.html" class="cta-button">Contact Us</a>
        </nav>
    </div>
</header>"""

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        current_header = new_header
        
        # Add active class to corresponding nav link
        if filename != 'index.html':
            current_header = current_header.replace(f'href="{filename}"', f'href="{filename}" class="active"')
        else:
            current_header = current_header.replace('<a href="index.html">Home</a>', '<a href="index.html" class="active">Home</a>')

        # Replace entire header block (stripping out old inline styles)
        content = re.sub(r'<header[^>]*>.*?</header>', current_header, content, count=1, flags=re.DOTALL | re.IGNORECASE)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {filename}")

print(f"Total files updated: {count}")
