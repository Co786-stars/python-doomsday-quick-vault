"""
In this module we are discussing:
How to use conditional statements (if/else) in Django templates with professional data examples.
"""
# ------------------------------------------------------------------------
# 1. INTRODUCTION TO CONDITIONALS IN DJANGO TEMPLATES
# ------------------------------------------------------------------------
# - In Python we write conditions like:
#       if x > 10:
#           print("Yes")
#       else:
#           print("No")
#
# - In Django templates, logic is written differently because templates
#   are designed for presentation, not raw Python execution.
# - Control statements are wrapped inside {% ... %} tags.
#   Example: {% if x > 10 %} ... {% else %} ... {% endif %}
#
# - Curly braces {{ ... }} are used only for output (printing values).
#   Example: {{ x }} will display the value of x in HTML.
# - So remember:
#       {% ... %} → logic/control flow
#       {{ ... }} → variable output

# ------------------------------------------------------------------------
# 2. BASIC IF/ELSE USAGE
# ------------------------------------------------------------------------
# - {% if condition %} starts the block.
# - {% else %} handles the alternative case.
# - {% endif %} closes the block.
#
# Example (template side):
#   {% if employee_count > 50 %}
#       Large company
#   {% else %}
#       Small company
#   {% endif %}
#
# Output depends on the value passed from views.py.

# ------------------------------------------------------------------------
# 3. ELIF SUPPORT
# ------------------------------------------------------------------------
# - Django templates also support {% elif %} for multiple branches.
# - Example:
#   {% if score >= 90 %}
#       Excellent
#   {% elif score >= 75 %}
#       Good
#   {% else %}
#       Needs Improvement
#   {% endif %}

# ------------------------------------------------------------------------
# 4. MEMBERSHIP AND COMPARISON
# ------------------------------------------------------------------------
# - You can check if a value exists in a list:
#   {% if "Finance" in departments %}
#       Finance department is available
#   {% endif %}
#
# - Comparisons like {% if salary > 50000 %} are valid too.

# ------------------------------------------------------------------------
# 5. NESTED CONDITIONALS
# ------------------------------------------------------------------------
# - Conditions can be nested inside loops or other conditions.
# - Example:
#   {% for dept in departments %}
#       {% if dept == "Research & Development" %}
#           Highlight: {{ dept }}
#       {% else %}
#           {{ dept }}
#       {% endif %}
#   {% endfor %}
#
# - This allows fine-grained control over how each item is displayed.

# ------------------------------------------------------------------------
# 6. EMPTY CASES
# ------------------------------------------------------------------------
# - When looping, you can combine conditions with {% empty %}.
# - Example:
#   {% for project in projects %}
#       {{ project }}
#   {% empty %}
#       No projects found
#   {% endfor %}

# ------------------------------------------------------------------------
# 7. BEST PRACTICES
# ------------------------------------------------------------------------
# - Keep conditions simple in templates; complex logic belongs in views.py.
# - Use conditions mainly for presentation (e.g., show/hide sections).
# - Always close blocks with {% endif %} to avoid syntax errors.
# - Remember: templates are not Python scripts — they are display logic only.

# ------------------------------------------------------------------------
# 8. SUMMARY
# ------------------------------------------------------------------------
# - Python: if/else uses colons and indentation.
# - Django templates: if/else uses {% %} tags and must end with {% endif %}.
# - {{ }} is for output, {% %} is for control.
# - Supports if, else, elif, membership checks, nested conditions, and empty cases.





# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
# <!------------------------------------------------------------------------
# Note VVI (Very very Important): -
#
# In Django templates, we use special tags to control logic.
# Unlike Python where we write: if x > 10: ... else: ...,
# templates use {% ... %} to mark control statements.
#
# The {% %} symbols tell the template engine "this is logic, not plain HTML".
# Inside these tags we can write conditions like {% if x > 20 %},
# and we must always close them with {% endif %}.
# If we want an alternative branch, we add {% else %} in between.
#
# Curly braces {{ ... }} are different — they are used to print values
# directly into the HTML (for example {{ x }} will show the value of x).
# So remember:
# - {% ... %} → for logic (if, for, etc.)
# - {{ ... }} → for output (variables, expressions)
#
# This separation makes Django templates safe and clean:
# Python code runs in views, while templates only handle display logic.
# --------------------------------------------------------------------------->

