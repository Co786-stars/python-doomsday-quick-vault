"""
In this module we are discussing:
How to pass data from views.py into template.html using context and {{ }}.
"""

# -------------------------------
# 1. IMPORTS
# -------------------------------
# render → connects a view function with an HTML template.
# It also allows us to send extra data (context) into the template.
from django.shortcuts import render


# -------------------------------
# 2. SIMPLE DATA PASSING
# -------------------------------
# Context is a dictionary. Each key becomes a variable in template.
# Example: {{ name }} in template.html will show "Wizard".
def simple_pass(request):
    context = {
        "name": "Wizard"
    }
    return render(request, "template.html", context)


# -------------------------------
# 3. MULTIPLE VALUES
# -------------------------------
# You can send more than one value at the same time.
# Each key in context can be displayed with {{ key }} in template.
def multiple_pass(request):
    context = {
        "title": "CryptoCore",
        "message": "Learning Django step by step"
    }
    return render(request, "template.html", context)


# -------------------------------
# 4. PASSING LISTS
# -------------------------------
# Lists can be looped in template using {% for %}.
# Example in template.html:
#   {% for item in fruits %}
#       <li>{{ item }}</li>
#   {% endfor %}
def list_pass(request):
    context = {
        "fruits": ["Apple", "Banana", "Cherry"]
    }
    return render(request, "template.html", context)


# -------------------------------
# 5. PASSING DICTIONARIES
# -------------------------------
# Dictionaries can be accessed with dot notation in template.
# Example: {{ user.name }} → "Aditya"
def dict_pass(request):
    context = {
        "user": {
            "name": "Aditya",
            "age": 22,
            "city": "Dadri"
        }
    }
    return render(request, "template.html", context)


# -------------------------------
# 6. EXTRA NOTES
# -------------------------------
# - Context is always a Python dictionary.
# - Keys in context become variables in template.
# - {{ variable }} → replaced with actual value.
# - {% for %} → loops through lists.
# - {% if %} → adds conditions.
# - Flow: URL → urls.py → view function → render() → template.html → browser.


# Straight Forward
"""
Steps to Pass Data from View to Template
----------------------------------------

1. In views.py → create a context dictionary.
   Example: context = {"name": "Aditya"}
2. Use render(request, "template.html", context).
3. In template.html → write {{ name }} to show the value.
4. For lists → use {% for item in fruits %} {{ item }} {% endfor %}.
5. For dictionaries → use {{ user.name }} or {{ user.city }}.
6. Run server → Django replaces {{ }} with actual values in the HTML.
"""