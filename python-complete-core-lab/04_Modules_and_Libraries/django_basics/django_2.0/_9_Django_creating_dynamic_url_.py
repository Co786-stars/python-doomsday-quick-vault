"""
In this module we are discussed_______________how to create dynamic routes/url___________________
"""

# In details :-
"""
* In Django, routes (URLs) are defined inside the urls.py file. They map a URL pattern to a view function/class.
  There are two main ways to define routes:
   - Using path() → simpler, modern style (Django 2.0+).
   - Using re_path() → regex-based, older but powerful.

* Django provides built-in converters to capture parts of the URL and pass them as arguments to views.

# Using path() → simpler, modern style (Django 2.0+).:-
    - int → matches only numbers (e.g., /product/15/)
    - str → matches any non‑empty string without slashes (e.g., /user/aditya/)
    - slug → matches “slugified” strings (letters, numbers, hyphens, underscores) — perfect for SEO URLs like /blog/python-basics/
    - path → matches entire path segments including slashes (e.g., /files/images/logo.png/)
    - uuid → matches UUIDs (e.g., /item/550e8400-e29b-41d4-a716-446655440000/)
    example :-
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('product/<int:id>/', views.product_detail),
        path('user/<str:username>/', views.user_profile),
        path('blog/<slug:slug>/', views.blog_post),
        path('files/<path:file_path>/', views.serve_file),
        path('item/<uuid:item_id>/', views.item_detail),
    ]



# Using re_path() → regex-based, older but powerful.
    - (?P<id>[0-9]+) → captures digits as id
    - (?P<slug>[-\w]+) → captures slugs (letters, numbers, hyphens, underscores)
    example :- 
    from django.urls import re_path
    
    urlpatterns = [
        re_path(r'^product/(?P<id>[0-9]+)/$', views.product_detail),
        re_path(r'^user/(?P<username>[a-zA-Z]+)/$', views.user_profile),
        re_path(r'^blog/(?P<slug>[-\w]+)/$', views.blog_post),
    ]
"""

# 👉 So, Aditya, the main ways are :-
#       - path() with converters (int, str, slug, uuid, path)
#       - re_path() with regex
#       - include() for modular routing

