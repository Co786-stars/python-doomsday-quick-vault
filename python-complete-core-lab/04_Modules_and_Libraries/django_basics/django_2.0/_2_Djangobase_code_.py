"""
_____________________________________________________________________________________________________
# ______________In this module we see Django Installation & Basic CMD Commands Guide_________________#
_____________________________________________________________________________________________________

## 1. Update pip (Python package manager)
> python -m pip install --upgrade pip
- Updates pip to the latest version.

## 2. Check pip version
> pip --version
- Displays the installed pip version.

## 3. Create a Virtual Environment
> python -m venv .venv
- Ensures a virtual environment named `.venv` is created.

## 4. Upgrade/Reinstall Packaging Tools
> pip install --upgrade pip setuptools wheel
- Reinstalls/updates essential Python packaging libraries.

## 5. Check if Django is Installed
> pip show django
- Displays details about Django (version, location, summary, homepage, etc.).

## 6. Locate Python Executable
> where python
- Shows the exact location of the Python executable.
  Example outputs:
    C:\Users\<YourName>\AppData\Local\Microsoft\WindowsApps\python.exe
    C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\Scripts

### Important Note:
- If Python is installed via Microsoft Store:
  Location → C:\Users\<YourName>\AppData\Local\Microsoft\WindowsApps\python.exe
  This does NOT give access to the Scripts folder (where pip.exe and django-admin.exe live).

- If Python is installed via python.org:
  Location → C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\Scripts
  This DOES give access to the Scripts folder (pip.exe and django-admin.exe available).

- The path `C:\Users\<YourName>\AppData\Local\Microsoft\WindowsApps\python.exe`
  is just a Windows Store alias, not the actual Python installation folder.
  That’s why Scripts or Python311 folders aren’t accessible there.

## 7. Install Django
> pip install django
- Installs Django framework (recommended after installing Python from python.org).

## 8. Create a New Django Project
> django-admin startproject myproject
- Creates a new Django project with default settings and structure.

### Example:
1. Create a new directory (e.g., xyz).
2. Open CMD inside that directory:
   C:\Users\<YourName>\xyz>
3. Run:
   django-admin startproject MyProjectName
- This generates:
  - manage.py file
  - A new subfolder (MyProjectName) inside xyz
"""

# Quick Summary:
# python -m pip install --upgrade pip        → updates pip to the latest version
# pip --version                              → checks the installed pip version
# python -m venv .venv                       → creates a virtual environment named .venv
# pip install --upgrade pip setuptools wheel → upgrades/reinstall essential Python packaging tools
# pip show django                            → displays details if Django is installed (version, location, etc.)
# where python                               → shows the exact location of the Python executable
# pip install django                         → installs the Django framework
# django-admin startproject myproject        → creates a new Django project with default settings and structure

