"""
# _____________________________________________________________________________________________________
# =======================================================================================================
# ----------------In this module we are discuss Process to create the Superuser------------------------
# =======================================================================================================
# _____________________________________________________________________________________________________
"""
## Why we create a Superuser?
#  When we run the port http://127.0.0.1:8000/ then we see the django page but when we open in root user
#  using http://127.0.0.1:8000/admin then we see login page of django so to get the username and password
#  we create a superuser

## How to create the Superuser in Django ?
#  To create a superuser in Django (the admin account with full privileges), we use the createsuperuser management command.
#  Here’s the proper way to do it steps by steps :-
#  - Open terminal in root directory of our Django project( where manage.py is located )
#  - C:\Users\<YourName>\xyz>python manage.py createsuperuser
#  - Username: admin_name
#  - Email address: admin@example.com
#  - Password: Any321Things32#1@
#  - Password (again): Any321Things32#1@
#  - Superuser created successfully

## How to check the data in DB browser?
#  To check the Username, Password, Email Address from DB browser.
#  Here are the steps given
#  - Open DB browser SQL(lite).
#  - Click on open Database.
#  - Then open db.sqlite3 file
#  - Right click on Tables\auth_user
#  - click on browser table
#  - we see lots of data like encrypted password, username, email address, username, last login ....etc.


