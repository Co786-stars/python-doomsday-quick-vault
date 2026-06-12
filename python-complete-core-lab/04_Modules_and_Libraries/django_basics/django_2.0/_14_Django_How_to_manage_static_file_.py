"""
In this module we are discussing:
How to manage static files (CSS, JS, images) in Django projects,
how to link them in HTML templates, and how to debug attachment issues.
"""

# ------------------------------------------------------------------------
# 1. INTRODUCTION TO STATIC FILES
# ------------------------------------------------------------------------
# - Static files = CSS, JavaScript, images used for styling and interactivity.
# - Django separates static files from templates for clean project structure.
# - In settings.py we configure:
#       STATIC_URL = '/static/'
#       STATICFILES_DIRS = [BASE_DIR / "static"]   # dev folder
#       STATIC_ROOT = BASE_DIR / "staticfiles"     # for collectstatic in production
#
# - Folder structure example:
#       project_root/
#       ├── static/
#       │   ├── CSS/
#       │   │   └── style.css
#       │   └── js/
#       │       └── script.js
#       └── templates/
#           └── example.html

# ------------------------------------------------------------------------
# 2. LINKING STATIC FILES IN DJANGO TEMPLATES
# ------------------------------------------------------------------------
# - Always load static at the top of the template:
#       {% load static %}
#
# - CSS link:
#       <link rel="stylesheet" href="{% static 'CSS/style.css' %}">
#
# - JS link:
#       <script src="{% static 'js/script.js' %}"></script>
#
# - This ensures Django resolves the correct path automatically.

# ------------------------------------------------------------------------
# 3. PLAIN HTML METHOD (without Django tags)
# ------------------------------------------------------------------------
# - CSS:
#       <link rel="stylesheet" href="/static/CSS/style.css">
#
# - JS:
#       <script src="/static/js/script.js"></script>
#
# - Works only if the dev server serves /static/ directly.
# - Less portable than Django’s {% static %} method.

# ------------------------------------------------------------------------
# 4. INLINE vs EXTERNAL JS
# ------------------------------------------------------------------------
# - Inline JS:
#       <script>
#           console.log("✅ JS attached");
#           alert("✅ JS attached");
#       </script>
#   → Runs immediately, no path issues.
#
# - External JS:
#       <script src="{% static 'js/script.js' %}"></script>
#   → Preferred for real projects, keeps code organized.

# ------------------------------------------------------------------------
# 5. DEBUGGING STATIC FILES
# ------------------------------------------------------------------------
# - Use browser DevTools (F12):
#       • Console → check for console.log / alert.
#       • Network → confirm CSS/JS files load with status 200.
#
# - Common errors:
#       • Wrong folder name (templates vs templet).
#       • Wrong filename (case-sensitive).
#       • Linking .css file in <script> tag (must be .js).
#       • Forgetting {% load static %} at the top of template.

# ------------------------------------------------------------------------
# 6. BEST PRACTICES
# ------------------------------------------------------------------------
# - Keep CSS in static/CSS/, JS in static/js/.
# - Use {% static %} in Django templates for portability.
# - Test with console.log() or alert() to confirm JS is loaded.
# - Only one homepage route (path('', ...)) should be active at a time.
# - Inline JS is fine for testing, but external JS is better for maintainability.

# ------------------------------------------------------------------------
# 7. SUMMARY
# ------------------------------------------------------------------------
# - Django requires STATIC_URL and STATICFILES_DIRS in settings.py.
# - {% load static %} + {% static '...' %} is the recommended way to link files.
# - Inline JS works instantly, external JS requires correct path setup.
# - Debug with DevTools → Console + Network tabs.
# - Always keep static files organized and use Django’s static tag for reliability.
#
# ------------------------------------------------------------------------
# <!------------------------------------------------------------------------
# Note VVI (Very very Important):
#
# In Django templates, static files must be linked using {% static %}.
# Example:
#   {% load static %}
#   <link rel="stylesheet" href="{% static 'CSS/style.css' %}">
#   <script src="{% static 'js/script.js' %}"></script>
#
# This ensures Django resolves the correct URL for static files.
# Inline JS is useful for quick checks, but external JS is the professional way.
# ------------------------------------------------------------------------->

