# Import necessary Django modules
from django.http import HttpResponse       # Used to return plain text or HTML directly
from django.shortcuts import render        # Used to render HTML templates

# -------------------------------
# STATIC ROUTES (fixed URLs)
# -------------------------------

def securepage(request):
    """
    A simple static route.
    When user visits /securepage/, this function runs.
    """
    return HttpResponse("This page belongs to cryptoCore")


def new_admin(request):
    """
    Another static route.
    When user visits /xyz/, this function runs.
    """
    return HttpResponse("<h2>This.................cryptoCore</h2>")


# -------------------------------
# DYNAMIC ROUTES (URLs with variables)
# -------------------------------

def new_admin_details(request, dynamic_route):
    """
    Example of capturing an integer from the URL.
    URL: /xyz/15/ → dynamic_route = 15
    """
    return HttpResponse(f"This is routing 1st, value = {dynamic_route}")


def d2fill_in_depth(request, wizard):
    """
    Example of capturing a string from the URL.
    URL: /dynamic_route/aditya/ → wizard = "aditya"
    """
    return HttpResponse(f"This is routing 2nd, value = {wizard}")


def d3nothing_fill(request, id):
    """
    Example of capturing another integer from the URL.
    URL: /fill/99/ → id = 99
    """
    return HttpResponse(f"{id} This is routing 3rd")


# -------------------------------
# BASIC PRACTICE FUNCTION
# -------------------------------

def new_fun(request):
    """
    Just a simple loop example.
    It runs a loop from 1 to 2, and finally returns 2.
    URL: /pqr/
    """
    for i in range(1, 3):
        x = i
    return HttpResponse(x)   # Output will be 2


# ---------------------------------------------------------------
#          -----------------------------------------
# -------HOMEPAGE (Rendering HTML template)---(((VVI)))-----------
#          -----------------------------------------
# ---------------------------------------------------------------

def homepage(request):
    """
    Example of rendering an HTML template.
    It looks for 'index.html' inside your templates folder.
    URL: /
    """
    return render(request, "index.html")   # render(request, template_name)/link the function homepage


def main_page(request):
    """try to pass the data from view to templates/file.html"""
    context={
        'title':'Wizard', # simply how to pass value from views to templates files
        'variable':'This is a simple homepage layout. You can customize it with your own content.',
        'tab':["Python", "java", "c++"], # given an example how for loop is use in django to pass views data to templates
        'details':[
            {'Email':'xyz1246@gmail.com', 'Phone':9123654729},
            {'Email':'pqr6521@gmail.com', 'Phone':8463175315},
            {'Email':'abc8976@gmail.com', 'Phone':2143569841}
        ]
    }

    return render(request, 'Homepage.html', context) # return django/views data to templates/html web file



def next_page(request):
    """try to display the data from view to templates"""
    detail={
        'var':'In this module we discussed How we use if and els using django module',
        'lst':[10, 20, 30, 40, 50]
    }
    return render(request, 'otherPage.html', detail)


def static_practic(request):
    return render(request, 'otherpage1_.html')


def static_practic_1(request):
    return render(request, 'unique_extend_block.html')




# ---------GET METHOD :-----
# def linkHttpPage(request):
#     detail = {
#         'frmName': 'Practice Form',
#         'lst': [10, 20, 30, 40, 50]
#     }
#
#     try:
#         getdata1st = int(request.GET.get('q1', 0))   # safer with .get()
#         getdata2nd = int(request.GET.get('q2', 0))
#         result = getdata1st + getdata2nd
#         detail['result'] = f"{getdata1st} + {getdata2nd} = {result}"
#     except:
#         detail['result'] = "Pls enter valid numbers."
#

# --------: POST METHOD :-------------
def linkHttpPage(request):
    detail = {
        'frmName': 'Practice Form',
        'lst': [10, 20, 30, 40, 50]
    }

    try:
        postdata1st = str(request.POST.post('username'))  # safer with .get()
        postdata2nd = str(request.POST.post('Password'))
        result = postdata1st +  postdata2nd
        detail['result'] = f"{postdata1st} + {postdata2nd} = {result}"
    except:
        detail['result'] = "Pls enter valid numbers."

    return render(request, 'Unique_from.html', detail)
# __________________________________________________________________________________________________________________




# Example to explain :---------#
# _____________________________#
def inside_admin(request, unknown):

    return HttpResponse(f"<h1>{unknown}</h1>") # unknown return  dynamic url/value


