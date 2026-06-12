"""
In this module we are discussing:
How to use Django's template inheritance system with {% extends %} and {% block %},
how to combine it with {% include %} for reusable sections,
and how to build clean, modular layouts across multiple pages.
"""

# ------------------------------------------------------------------------
# 1. INTRODUCTION TO TEMPLATE INHERITANCE
# ------------------------------------------------------------------------
# - Django allows us to define a "base template" (e.g., base.html).
# - Child templates can inherit from this base using {% extends %}.
# - Inside the base template, we define {% block %} sections.
# - Child templates override these blocks with their own content.
# - This avoids repeating the same HTML structure across pages.

# ------------------------------------------------------------------------
# 2. USING {% extends %} TAG
# ------------------------------------------------------------------------
# - Syntax:
#       {% extends "base.html" %}
#
# - Must be the FIRST tag in the child template.
# - It tells Django: "This file is a child of base.html".
# - Example:
#       {% extends "unique_extend_block.html" %}

# ------------------------------------------------------------------------
# 3. USING {% block %} TAG
# ------------------------------------------------------------------------
# - Syntax:
#       {% block block_name %} ... {% endblock %}
#
# - Blocks are placeholders in the base template.
# - Child templates override them with custom content.
# - Example in base.html:
#       {% block middle %}{% endblock %}
#
# - Example in child.html:
#       {% block middle %}
#           <h2>Registration Form</h2>
#           <form> ... </form>
#       {% endblock %}

# ------------------------------------------------------------------------
# 4. COMBINING {% include %} WITH {% extends %}
# ------------------------------------------------------------------------
# - {% include %} is used for small reusable fragments (header, footer).
# - {% extends %} is used for overall layout inheritance.
# - Best practice:
#       - Put {% include "top_div_header.html" %} and {% include "top_div_footer.html" %}
#         inside the base template.
#       - Child templates only override blocks.
#
# - Example base.html:
#       <!DOCTYPE html>
#       <html>
#       <body>
#           {% include "top_div_header.html" %}
#           {% block middle %}{% endblock %}
#           {% include "top_div_footer.html" %}
#       </body>
#       </html>

# ------------------------------------------------------------------------
# 5. FOLDER STRUCTURE EXAMPLE
# ------------------------------------------------------------------------
# project_root/
# ├── templates/
# │   ├── base.html
# │   ├── top_div_header.html
# │   ├── top_div_footer.html
# │   ├── registration.html
# │   └── about.html
#
# - base.html → defines layout + includes header/footer
# - registration.html → extends base, overrides "middle" block
# - about.html → extends base, overrides "middle" block
# - header/footer → reusable fragments

# ------------------------------------------------------------------------
# 6. ADVANTAGES OF {% extends %} + {% include %}
# ------------------------------------------------------------------------
# - {% extends %} → keeps consistent layout across pages.
# - {% include %} → reuses small fragments like navbars, footers.
# - Together:
#   → DRY code (Don’t Repeat Yourself).
#   → Easy maintenance (update once, reflect everywhere).
#   → Clean modular design.

# ------------------------------------------------------------------------
# 7. BEST PRACTICES
# ------------------------------------------------------------------------
# - Always put {% extends %} at the top of child templates.
# - Use {% include %} only for small reusable sections.
# - Keep base.html as the main layout controller.
# - Organize reusable templates in an "includes/" folder.
# - Avoid mixing {% include %} directly in child templates if using {% extends %}.

# ------------------------------------------------------------------------
# 8. SUMMARY
# ------------------------------------------------------------------------
# - {% extends %} → for parent-child template inheritance.
# - {% block %} → for placeholders overridden by child templates.
# - {% include %} → for reusable fragments like header/footer.
# - Recommended structure:
#       base.html + includes/ + child templates.
#
# ------------------------------------------------------------------------
# <!------------------------------------------------------------------------
# Note VVI (Very Very Important):
#
# - {% extends %} must be the FIRST tag in child templates.
# - {% include %} should be used inside base.html, not mixed in child templates.
# - Example:
#       {% extends "base.html" %}
#       {% block middle %}
#           <h2>Page Content</h2>
#       {% endblock %}
# ------------------------------------------------------------------------->