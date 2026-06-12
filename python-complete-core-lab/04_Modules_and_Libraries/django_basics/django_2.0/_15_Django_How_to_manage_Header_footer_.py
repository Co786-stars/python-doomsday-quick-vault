"""
In this module we are discussing:
How to manage header and footer sections in Django projects,
how to reuse them across multiple pages using template inclusion,
and how to maintain clean modular design.
"""

# ------------------------------------------------------------------------
# 1. INTRODUCTION TO HEADER & FOOTER MANAGEMENT
# ------------------------------------------------------------------------
# - Header and footer are common sections repeated across multiple pages.
# - Instead of rewriting them in every HTML file, Django allows modular reuse.
# - We can create separate child templates (e.g., top_div_header.html, top_div_footer.html).
# - These child templates are then included in parent pages using Django template tags.

# ------------------------------------------------------------------------
# 2. USING {% include %} TAG
# ------------------------------------------------------------------------
# - Syntax:
#       {% include "child_template.html" %}
#
# - Example:
#       {% include "top_div_header.html" %}
#       {% include "top_div_footer.html" %}
#
# - This inserts the content of the child template into the parent template.
# - Works like copy-paste, but keeps code DRY (Don’t Repeat Yourself).

# ------------------------------------------------------------------------
# 3. FOLDER STRUCTURE EXAMPLE
# ------------------------------------------------------------------------
# project_root/
# ├── templates/
# │   ├── base.html
# │   ├── top_div_header.html
# │   ├── top_div_footer.html
# │   └── registration.html
#
# - base.html → main layout
# - top_div_header.html → header section
# - top_div_footer.html → footer section
# - registration.html → form page that includes header & footer

# ------------------------------------------------------------------------
# 4. SAMPLE IMPLEMENTATION
# ------------------------------------------------------------------------
# registration.html:
#   {% include "top_div_header.html" %}
#   <h2>Registration Form</h2>
#   <form> ... </form>
#   {% include "top_div_footer.html" %}
#
# top_div_header.html:
#   <header>
#       <h1>Welcome to Our Registration Page</h1>
#       <nav>
#           <a href="/">Home</a> | <a href="/about">About</a> | <a href="/contact">Contact</a>
#       </nav>
#   </header>
#
# top_div_footer.html:
#   <footer>
#       <p>&copy; 2026 My Website | All Rights Reserved</p>
#       <p>Follow us: Facebook | Twitter | Instagram</p>
#   </footer>

# ------------------------------------------------------------------------
# 5. ADVANTAGES OF USING {% include %}
# ------------------------------------------------------------------------
# - Avoids duplication of header/footer code.
# - Easier maintenance → update once, changes reflect everywhere.
# - Cleaner project structure.
# - Promotes modular design and reusability.

# ------------------------------------------------------------------------
# 6. BEST PRACTICES
# ------------------------------------------------------------------------
# - Keep header and footer in separate template files.
# - Use consistent naming (e.g., top_div_header.html, top_div_footer.html).
# - Place reusable templates in a common folder (e.g., templates/includes/).
# - Combine with base.html + {% block %} for advanced template inheritance.

# ------------------------------------------------------------------------
# 7. SUMMARY
# ------------------------------------------------------------------------
# - Django allows modular header/footer management using {% include %}.
# - Child templates (header/footer) are inserted into parent templates.
# - This keeps code DRY, clean, and easy to maintain.
# - Recommended structure: base.html + includes/ folder for reusable sections.
#
# ------------------------------------------------------------------------
# <!------------------------------------------------------------------------
# Note VVI (Very very Important):
#
# In Django templates, header and footer should be modularized.
# Example:
#   {% include "top_div_header.html" %}
#   {% include "top_div_footer.html" %}
#
# This ensures consistency across pages and simplifies updates.
# ------------------------------------------------------------------------->
