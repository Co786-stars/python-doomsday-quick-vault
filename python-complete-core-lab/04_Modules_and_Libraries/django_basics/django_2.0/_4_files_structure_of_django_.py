"""
# _____________________________________________________________________________________________________
========================================================================================================
In this module we are discuss Django Project Auto-Generated Files – Purpose & Importance
========================================================================================================
# _____________________________________________________________________________________________________

When we run: django-admin startproject MyProjectName
Django automatically creates a set of files and folders.
Each has a specific role in building and running the project.

1. manage.py
   - Command-line utility for interacting with the project.
   - Used for running server, migrations, creating apps, etc.

2. db.sqlite3
   - Default database file (SQLite).
   - Stores all project data (models, users, sessions).
   - Can be replaced with other databases in settings.py.

3. Outer Project Folder (MyProjectName/)
   - Container folder holding manage.py and inner project folder.

4. Inner Project Folder (MyProjectName/)
   - Actual Django project package.
   - Contains core configuration files.

   ├── __init__.py
   │   - Marks folder as a Python package.
   │   - Needed for Python imports.
   │
   ├── settings.py
   │   - Central configuration file.
   │   - Defines database, installed apps, middleware, templates, static files.
   │
   ├── urls.py
   │   - URL dispatcher (routing system).
   │   - Maps URLs to views.
   │
   ├── wsgi.py
   │   - Entry point for WSGI servers (traditional deployment).
   │   - Used with Gunicorn/Apache.
   │
   └── asgi.py
       - Entry point for ASGI servers (async deployment).
       - Supports WebSockets, async features.

===========================================================
Summary:
- manage.py → Remote control for project
- db.sqlite3 → Default database
- settings.py → Brain of the project
- urls.py → Routing map
- wsgi.py/asgi.py → Deployment gateways
- __init__.py → Makes folder a Python package

     simple memo :-
    • manage.py = remote control 📺
    • settings.py = brain 🧠
    • urls.py = map 🗺️
    • db.sqlite3 = storage 📦
    • wsgi/asgi = gateway - 🚪

"""


# ==============================
# Django Project Structure Guide
# ==============================

# 📌 File: manage.py
# ------------------
# This is the command-line utility for your project.
# You use it to runserver, migrate, create apps, etc.
# Example: python manage.py runserver
# Without this file, you cannot interact with your project easily.

# 📌 File: db.sqlite3
# -------------------
# Default database file (SQLite).
# Stores all your project data (users, models, sessions, etc.)
# You can replace it with MySQL/PostgreSQL later in settings.py.

# 📌 Folder: MyProjectName/   (outer folder)
# -----------------------------------------
# This is the container folder for your project.
# It holds manage.py and the inner project folder.

# 📌 Folder: MyProjectName/   (inner folder)
# -----------------------------------------
# This is the actual Django project package.
# It contains the core configuration files for your project.

# Inside the inner folder, you’ll find these important files:

# 📌 File: __init__.py
# --------------------
# Marks this folder as a Python package.
# Without this, Python won’t treat it as a module.

# 📌 File: settings.py
# --------------------
# The heart of your project configuration.
# Contains database settings, installed apps, middleware, templates, static files, etc.
# Example: DEBUG=True/False, DATABASES, INSTALLED_APPS.

# 📌 File: urls.py
# ----------------
# URL dispatcher of your project.
# Maps URLs (like /home, /about) to views (functions/classes).
# Example: path('admin/', admin.site.urls)

# 📌 File: asgi.py
# ----------------
# Entry point for ASGI servers (used for async support).
# Needed if you want WebSockets or async features.
# Example: deployment with Daphne/Uvicorn.

# 📌 File: wsgi.py
# ----------------
# Entry point for WSGI servers (used for traditional deployments).
# Needed when deploying on Apache, Gunicorn, etc.
# Example: deployment with Gunicorn.


# ==============================
# Why are these important?
# ==============================
# - manage.py → Your project’s remote control
# - db.sqlite3 → Default database for development
# - settings.py → Central configuration brain
# - urls.py → Routing system (maps URLs to views)
# - wsgi.py/asgi.py → Deployment entry points
# - __init__.py → Makes the folder a Python package

# Together, these files form the skeleton of a Django project.
# They ensure you can run, configure, and deploy your web application.


