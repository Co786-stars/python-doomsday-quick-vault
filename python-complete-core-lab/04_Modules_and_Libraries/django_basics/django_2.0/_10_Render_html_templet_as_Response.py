"""
_10_Render_html_templet_as_Response.py

In this module we are discussing step by step:
1. How Django connects Python code (views) to HTML templates.
2. Why we use 'render()' instead of 'HttpResponse' when we want to show a webpage.
3. What each parameter in render() means.
4. How URL routing works with views.
5. How Django internally finds and loads the template.
"""

# -------------------------------
# 1. IMPORTS
# -------------------------------
# HttpResponse → used to send plain text or HTML directly.
# render → used to load an HTML file (template) and return it as a response.
from django.http import HttpResponse
from django.shortcuts import render


# -------------------------------
# 2. STATIC ROUTES (fixed URLs)
# -------------------------------
# These functions return simple text/HTML directly using HttpResponse.
# Example: visiting /securepage/ will show plain text.
def securepage(request):
    return HttpResponse("This page belongs to cryptoCore")


def new_admin(request):
    return HttpResponse("<h2>This.................cryptoCore</h2>")


# -------------------------------
# 3. DYNAMIC ROUTES (URLs with variables)
# -------------------------------
# Django can capture values from the URL and pass them into the function.
# Example: /xyz/15/ → dynamic_route = 15
def new_admin_details(request, dynamic_route):
    return HttpResponse(f"This is routing 1st, value = {dynamic_route}")


# Example: /dynamic_route/aditya/ → wizard = "aditya"
def d2fill_in_depth(request, wizard):
    return HttpResponse(f"This is routing 2nd, value = {wizard}")


# Example: /fill/99/ → id = 99
def d3nothing_fill(request, id):
    return HttpResponse(f"{id} This is routing 3rd")


# -------------------------------
# 4. BASIC PRACTICE FUNCTION
# -------------------------------
# Just a loop example to show how Python logic works inside a view.
# Visiting /pqr/ will run the loop and return the last value (2).
def new_fun(request):
    for i in range(1, 3):
        x = i
    return HttpResponse(x)   # Output will be 2


# -------------------------------
# 5. HOMEPAGE (Rendering HTML template)
# -------------------------------
# This is the most important part: connecting Python to an HTML file.
# Instead of HttpResponse, we use render().
#
# render() takes:
#   - request → the HTTP request object (browser info, user data, etc.)
#   - template_name → the HTML file we want to show (e.g., "index.html")
#   - context (optional) → a dictionary of data to send into the template
#
# Example: render(request, "index.html", {"name": "Aditya"})
# In index.html, you can use {{ name }} to display "Aditya".
#
# Internally:
#   1. Django looks into the 'templates/' folder defined in settings.py.
#   2. It finds "index.html".
#   3. It replaces any {{ variables }} with values from context.
#   4. It returns the final HTML as an HttpResponse to the browser.
def homepage(request):
    # Example context dictionary (optional)
    context = {
        "title": "NcryCore Homepage",
        "message": "This page is rendered using Django's render() function."
    }
    return render(request, "index.html", context)


# -------------------------------
# 6. EXTRA NOTES
# -------------------------------
# - Why we use '.' in "from . import views":
#   The dot means "current package". It imports views.py from the same folder.
#
# - Why request is needed:
#   It carries all info about the browser request (method, headers, user, etc.).
#   Django uses it to build the response properly.
#
# - Why two parameters in render():
#   request → required to attach session/cookies and build response.
#   template_name → tells Django which HTML file to load.
#   (third parameter context is optional, used for dynamic data).
#
# - What happens internally:
#   URL → urls.py → view function → render() → template loader → HttpResponse → Browser.


#  Straight Forward
"""
Steps to Render HTML template in Django
--------------------------------------

1. Create a folder named 'templates' in your project root.
2. Inside 'templates', add your HTML file (example: index.html).
3. In settings.py → TEMPLATES → set DIRS = [BASE_DIR / "templates"].
4. In views.py → create a function homepage(request) and use render(request, "index.html").
5. In urls.py → map path('', views.homepage) for homepage route.
6. Run server → open http://127.0.0.1:8000/ → your HTML will display.
"""