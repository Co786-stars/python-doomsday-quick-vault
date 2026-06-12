# In this module we are discussed_________________what is views_______________what is url_______________
# ___________How to change the url of admin_________How to connect views of url_____How to create url________

"""
1) What is a View?
   - A view is a Python function or class in Django that receives a web request
     and returns a response (such as HTML, JSON, or plain text).
   - Views contain the logic of your application: they decide what data to show
     and how to present it.
   - Example:
       def home(request):
           return HttpResponse("Welcome to the Home Page")

2) What is a URL?
   - A URL pattern maps a specific path (like /home/) to a view.
   - Django uses urls.py to check these patterns and route incoming requests
     to the correct view.
   - Example:
       path("home/", views.home, name="home")


3) How to Change the Admin URL in Django
    - Concept:
      By default, Django provides the admin interface at the path "/admin/".
      For security reasons or branding purposes, you may want to change this path
      to something custom (e.g., "/control-panel/", "/dashboard/", "/secure-admin/").

    - Steps are:
          1. Open your project-level urls.py file (usually located in the project folder).
          2. Locate the line that maps the admin site: path("admin/", admin.site.urls)
          3. Replace "admin/" with your desired custom path.
          4. Save the file and restart the server.

    - Example:
        from django.contrib import admin
        from django.urls import path

        urlpatterns = [
            path("control-panel/", admin.site.urls),  # changed from "admin/"
        ]

    - Simple way to remember :-
      How to Change the Admin URL in Django
        - If you replace:
            path("admin/", admin.site.urls)
        - With:
            path("control-panel/", admin.site.urls)
        - Then the Django admin will no longer be available at:
            http://127.0.0.1:8000/admin/
        - Instead, it will open at:
            http://127.0.0.1:8000/control-panel/ in your browser.
        - Save the file and restart the server to check it  admin

    - Notes:
      * The admin interface is still the same; only the URL path changes.
      * Choose a path that is not easily guessable to add a layer of security.
      * You can also combine this with middleware or authentication checks for extra protection.
      * Remember: if you change the path, you must use the new one to log in (e.g., http://127.0.0.1:8000/control-panel/).

    - Best Practice:
      - Use a unique, non-obvious path (avoid "admin123" or "myadmin").
      - Document the change so your team knows where to access the admin.
      - Consider restricting admin access by IP or using HTTPS in production.
"""

#_____________VVI steps to run url on browser____________VVI steps to run url on browser________________________
#> How to create views connect ?
# create the views.py file under the sub folder of project folder C:\Users\<YourName>\xyz\xyz\views.py
# then import HttpResponse from django.http that is used to give the response on browser
# we create a function inside views.py
# example:
'''
from django.http import HttpResponse

def securepage(request):
    return HttpResponse("This page belongs to cryptoCore")
'''

#> How to create url ?
# open urls.py file under the project folder C:\Users\<YourName>\xyz\xyz\urls.py
# then import views file using (from . import views)
# add path() in urlpatterns list to connect the function
# example:
'''
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('securepage/', views.securepage, name='securepage'),
]
'''
# run the server using: python manage.py runserver
# open browser and type: http://127.0.0.1:8000/securepage/

