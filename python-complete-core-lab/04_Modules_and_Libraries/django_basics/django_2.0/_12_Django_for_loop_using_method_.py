"""
In this module we are discussing:
How to use for loops in Django templates with professional data examples.
"""


from django.shortcuts import render

# -------------------------------
# 1. PASSING A LIST OF DEPARTMENTS
# -------------------------------
# Instead of fruits, we use department names.
# In template.html → loop through and display each department.
def department_list(request):
    context = {
        "departments": ["Human Resources", "Finance", "Research & Development", "Information Technology"]
    }
    return render(request, "template.html", context)


# -------------------------------
# 2. TEMPLATE SIDE (HTML EXAMPLE)
# -------------------------------
# Example template.html:
#
# <html>
#   <body>
#     <h2>Company Departments</h2>
#     <ul>
#       {% for dept in departments %}
#         <li>{{ dept }}</li>
#       {% endfor %}
#     </ul>
#   </body>
# </html>
#
# Explanation:
# - {% for dept in departments %} → starts the loop.
# - {{ dept }} → shows each department name.
# - {% endfor %} → closes the loop.
#
# Output:
# Company Departments
# - Human Resources
# - Finance
# - Research & Development
# - Information Technology


# -------------------------------
# 3. EXTRA NOTES
# -------------------------------
# - You can replace "departments" with any professional dataset:
#   Example: ["Project Alpha", "Project Beta", "Project Gamma"]
# - {% for %} works the same way regardless of the list content.
# - Use {{ variable }} inside the loop to show each item.
# - {% empty %} can be used to handle empty lists.




# ------------------------------------------------------------------------
# 4. VVI Django Notes : - Predefined Loop Variables in Django Templates
# ------------------------------------------------------------------------
# Description:
# Django provides special predefined variables inside the {% for %} loop
# to help track the iteration state. These are not functions but built-in
# context variables that make template logic easier.
#
# Examples:
# - forloop.counter      → 1-based index (starts at 1)
# - forloop.counter0     → 0-based index (starts at 0)
# - forloop.revcounter   → Reverse 1-based index (ends at 1)
# - forloop.revcounter0  → Reverse 0-based index (ends at 0)
# - forloop.first        → True if first iteration
# - forloop.last         → True if last iteration


