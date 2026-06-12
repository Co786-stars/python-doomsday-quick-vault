"""
# _____________________________________________________________________________________________________
=======================================================================================================
----------In this module we are discuss Django Development Server URLs – Purpose & Usage---------------
=======================================================================================================
# _____________________________________________________________________________________________________
When you run: python manage.py runserver
Django starts a local development server at:
http://127.0.0.1:8000/

1. http://127.0.0.1:8000/
   - This is the default homepage of your Django project.
   - If no custom app or view is connected yet, you’ll see
     the Django welcome page ("The install worked successfully!").
   - It confirms your project is running correctly.

2. http://127.0.0.1:8000/admin
   - This is the Django Admin interface.
   - A powerful built-in dashboard to manage your database models.
   - You can add, edit, and delete records (like users, posts, products).
   - To access it, you need a **superuser account**.

   Steps to create superuser:
   --------------------------------
   python manage.py createsuperuser
   # Enter username, email, and password
   # After creation, use these credentials to log in at /admin

===========================================================
Summary:
- 127.0.0.1 → Localhost (your own computer).
- :8000 → Port number where Django server runs.
- / → Root URL → shows project homepage.
- /admin → Admin dashboard → requires superuser login.
===========================================================
"""


# """
# ===========================================================
# Django Command: python manage.py migrate
# ===========================================================
#
# 📌 What it does:
# - Applies database migrations (changes) to your database.
# - Creates or updates tables according to your models and Django’s built-in apps.
# - Ensures your database structure matches your project code.
#
# 📌 When we use it:
# - Right after starting a new project (to set up initial tables like auth_user).
# - After creating new models in an app.
# - After modifying existing models (adding fields, deleting fields, etc.).
# - Anytime Django or your apps need to sync changes with the database.
#
# 📌 Why we use it:
# - Without migrations, your models (Python code) and database (tables) won’t match.
# - It keeps database schema updated automatically.
# - Saves you from manually writing SQL commands.
#
# 📌 What it is used for:
# - Creates tables for Django’s built-in apps:
#   - Authentication (users, groups, permissions)
#   - Sessions
#   - Admin interface
#   - Content types
# - Creates tables for your custom models (defined in models.py).
# - Updates schema when you change models.
#
# 📌 Typical workflow:
# 1. python manage.py makemigrations
#    - Generates migration files based on changes in models.py.
#    - These files describe what changes should happen in the database.
#
# 2. python manage.py migrate
#    - Actually applies those migration files to the database.
#    - Creates/updates tables, columns, constraints, etc.
#
# ===========================================================
# Summary:
# - makemigrations → Prepares migration files (blueprint of changes).
# - migrate → Applies those changes to the database.
# ===========================================================
# """