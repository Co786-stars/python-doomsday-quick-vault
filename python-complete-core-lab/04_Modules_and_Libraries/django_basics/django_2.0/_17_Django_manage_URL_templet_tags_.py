"""
In this module we are discussing:
How Django manages navigation between pages using URL patterns,
how to connect template links (<a href="...">) with urls.py,
and how to use template tags like {% url %} for clean, maintainable code.
"""

# ------------------------------------------------------------------------
# 1. INTRODUCTION TO URL MANAGEMENT
# ------------------------------------------------------------------------
# - In Django, every webpage is connected through a URL pattern.
# - These patterns are defined in urls.py.
# - Templates (HTML files) use <a href="..."> links to navigate.
# - Instead of hardcoding paths ("/about", "/contact"), Django provides {% url %} tag.
# - This ensures links remain correct even if paths change later.

# ------------------------------------------------------------------------
# 2. DEFINING URLS IN urls.py
# ------------------------------------------------------------------------
# Example urls.py:
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('services/', views.services, name='services'),
#     path('contact/', views.contact, name='contact'),
# ]
#
# - Each path connects a URL (like "about/") to a view function.
# - The "name" parameter is very important → used in templates.

# ------------------------------------------------------------------------
# 3. USING <a href="..."> DIRECTLY
# ------------------------------------------------------------------------
# - You can hardcode links:
#   <a href="/about">About</a>
#   <a href="/contact">Contact</a>
#
# - Problem: If you change the URL in urls.py, you must update all templates.
# - Solution: Use {% url %} tag.

# ------------------------------------------------------------------------
# 4. USING {% url %} TEMPLATE TAG
# ------------------------------------------------------------------------
# - Syntax:
#       <a href="{% url 'url_name' %}">Link Text</a>
#
# - Example:
#       <a href="{% url 'home' %}">Home</a>
#       <a href="{% url 'about' %}">About</a>
#       <a href="{% url 'services' %}">Services</a>
#       <a href="{% url 'contact' %}">Contact</a>
#
# - Advantage: If you change path('about/', views.about, name='about'),
#   the template link still works because it uses the "name".

# ------------------------------------------------------------------------
# 5. PASSING PARAMETERS IN {% url %}
# ------------------------------------------------------------------------
# - Some URLs need parameters (like /product/5).
# - urls.py:
#       path('product/<int:id>/', views.product_detail, name='product_detail')
#
# - Template:
#       <a href="{% url 'product_detail' id=5 %}">View Product</a>
#
# - Django automatically builds the correct link.

# ------------------------------------------------------------------------
# 6. FOLDER STRUCTURE EXAMPLE
# ------------------------------------------------------------------------
# project_root/
# ├── myapp/
# │   ├── views.py
# │   ├── urls.py
# │   └── templates/
# │       ├── base.html
# │       ├── home.html
# │       ├── about.html
# │       ├── services.html
# │       └── contact.html
#
# - urls.py → defines paths
# - templates → use {% url %} for navigation
# - views.py → defines logic for each page

# ------------------------------------------------------------------------
# 7. ADVANTAGES OF {% url %}
# ------------------------------------------------------------------------
# - No hardcoding → safer and cleaner.
# - Easy maintenance → change URL once in urls.py, templates auto-update.
# - Supports dynamic parameters.
# - Keeps project DRY (Don’t Repeat Yourself).

# ------------------------------------------------------------------------
# 8. BEST PRACTICES
# ------------------------------------------------------------------------
# - Always use "name" in urls.py and {% url %} in templates.
# - Keep URL names short and meaningful (e.g., 'home', 'about').
# - Use consistent naming across project.
# - Avoid mixing hardcoded paths with {% url %}.

# ------------------------------------------------------------------------
# 9. SUMMARY
# ------------------------------------------------------------------------
# - urls.py defines paths and names.
# - Templates use {% url 'name' %} for navigation.
# - Parameters can be passed easily.
# - This ensures clean, maintainable, and scalable navigation in Django.

# ------------------------------------------------------------------------
# <!------------------------------------------------------------------------
# Note VVI (Very Very Important):
#
# - Hardcoding links (<a href="/about">) works but is risky.
# - Always prefer {% url 'about' %} → safer and future-proof.
# - Remember:
#      {% url %} uses the *name* from urls.py, not the path string itself.
# - Example:
#       <li><a href="{% url 'about' %}">About</a></li>
# ------------------------------------------------------------------------->

