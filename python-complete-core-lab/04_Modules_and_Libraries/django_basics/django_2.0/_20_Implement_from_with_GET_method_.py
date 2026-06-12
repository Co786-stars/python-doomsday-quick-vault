"""
In this module we are discussing:
How to implement the GET method in Django,
to capture user input from forms and display it in the system.
"""

# ------------------------------------------------------------------------
# 1. INTRODUCTION TO GET IN DJANGO
# ------------------------------------------------------------------------
# - In Django, when a user submits a form with method="get",
#   the data is sent as query parameters in the URL.
# - Example URL after submission:
#       /search?q1=10&q2=20
# - Django provides request.GET dictionary to access this data.
# - request.GET works like a Python dictionary:
#       request.GET['q1'] → returns the value of q1
#       request.GET.get('q1') → safer, returns None if missing

# ------------------------------------------------------------------------
# 2. VIEW FUNCTION EXAMPLE
# ------------------------------------------------------------------------
# - A simple view to capture two numbers entered by the user
#   and display their sum back in the template.

from django.shortcuts import render

def get_method_example(request):
    detail = {'frmName': 'Practice GET Form'}
    try:
        # Capture values from query string
        num1 = int(request.GET.get('q1', 0))
        num2 = int(request.GET.get('q2', 0))

        # Process data
        result = num1 + num2

        # Pass result to template
        detail['result'] = f"{num1} + {num2} = {result}"
    except:
        detail['result'] = "Please enter valid numbers."

    return render(request, 'Unique_form.html', detail)

# ------------------------------------------------------------------------
# 3. TEMPLATE EXAMPLE (Unique_form.html)
# ------------------------------------------------------------------------
# - A simple form using GET method.
# - When user clicks submit, data is sent via URL query string.

"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ frmName }}</title>
</head>
<body>
    <h2>{{ frmName }}</h2>

    <!-- GET Method Form -->
    <form action="" method="get">
        <label>Enter first number:</label>
        <input type="text" name="q1">

        <label>Enter second number:</label>
        <input type="text" name="q2">

        <button type="submit">Submit (GET)</button>
    </form>

    <!-- Display result -->
    <p><strong>Result:</strong> {{ result }}</p>
</body>
</html>
"""

# ------------------------------------------------------------------------
# 4. HOW IT WORKS
# ------------------------------------------------------------------------
# - User enters two numbers and clicks submit.
# - Browser sends request: /?q1=10&q2=20
# - Django view reads request.GET['q1'] and request.GET['q2'].
# - View calculates sum and passes it to template.
# - Template displays result dynamically.

# ------------------------------------------------------------------------
# 5. BEST PRACTICES
# ------------------------------------------------------------------------
# - Always use request.GET.get('param', default) → safer than request.GET['param'].
# - Validate and convert data types (e.g., int()) before using.
# - Use GET for non-sensitive, small data (search, filters, practice forms).
# - Do not use GET for passwords or confidential information.
# ------------------------------------------------------------------------

