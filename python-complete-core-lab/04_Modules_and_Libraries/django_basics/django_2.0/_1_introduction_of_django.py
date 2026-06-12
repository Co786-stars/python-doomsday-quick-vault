"""
# _____________________________________________________________________________________________________
In the module we are going to Discuss the topic
- What is Django
- Why we use Django
- Companies that use Django
- Importance of Django
- How Django is different from other Python frameworks
#_____________________________________________________________________________________________________
"""


# ______________________________________________________________________________________________________________________
"""
What is Django
> Django is a Python framework used to build secure, scalable, and dynamic websites quickly.

   What is framework :-
    - A framework is a pre‑built collection of tools, libraries, and rules that provides a standard way to develop applications.
  
   Types of frameworks :- 
    → Web frameworks     → (e.g., Django, Flask, Ruby on Rails) → help build websites/web apps.
    → Mobile frameworks  → (e.g., React Native, Flutter)        → help build mobile apps.
    → Testing frameworks → (e.g., PyTest, JUnit)                → help test code.
    → UI frameworks      → (e.g., Bootstrap, Angular)           → help design user interfaces
   
   Purpose to use framework :-
    → It enforces best practices and a consistent structure.
    → It saves time by giving ready‑made components (instead of writing everything from scratch).
    → It reduces errors by handling common tasks (security, database connections, routing, etc.).

> Django framework works on the MVT architecture, follows the DRY principle, and is used for building web applications. 
  Django organizes your project into Model, View, and Template, reuses code with DRY, and makes web development fast and efficient
  
  What is MVT and DRY : -
  MVT  Model View Template
    → Modal (manage the database)/data management 
    → View (handles the logic)/what to do with data
    → Template (UI to user)/showing result
  
  DRY  Don’t Repeat Yourself
    → It means Don’t write the same code again and again.
    → Avoids repeating code by giving reusable components (like authentication, forms, admin panel)
    → We write less code, get a clear structure, and build secure websites faster.

"""


# ______________________________________________________________________________________________________________________

"""
Why we use Django 
> We use Django because it is fast, secure, scalable, and easy to maintain.
    → Django helps us build websites quickly with less code.
    → It has built‑in security features to protect against common attacks.
    → Django can handle large projects and high traffic easily.
    → It follows the MVT architecture, which keeps code clean and organized.
    → The DRY principle makes code reusable and reduces repetition.
    → Django comes with a ready admin panel to manage data.
    → It supports multiple databases and third‑party packages.
    → A big community and good documentation make learning easier.
    → It is flexible for small apps, big websites, and even APIs.

"""



# ______________________________________________________________________________________________________________________
"""
Companies that use Django
> Example of some company that use Django frameworks to built website quickly
  → Instagram → Social media giant, handles massive traffic and user data.
  → Pinterest → Visual discovery and bookmarking platform.
  → Spotify → Music streaming service, uses Django for backend services.
  → Dropbox → Cloud storage and file sharing.
  → YouTube (parts of it) → Some internal systems rely on Django.
  → Mozilla → Uses Django for many of its web applications.
  → NASA → For managing scientific data and projects.
  → National Geographic → Content-heavy website powered by Django.
  → Disqus → Popular commenting system integrated into millions of sites.
  → Eventbrite → Online event management and ticketing platform
  
"""


# ______________________________________________________________________________________________________________________
"""
Importance of Django
> Django is important because it makes web development fast, secure, scalable, and maintainable with a clean structure 
  and strong community support.
   → Fast Development → Django provides ready-made components (like authentication, admin panel, ORM ), so projects are built quickly.
   → Security → It has built-in protection against common web attacks (SQL injection, XSS, CSRF).
   → Scalability → Handles high traffic and large databases, making it suitable for big companies like Instagram and Pinterest.
   → Clean Architecture (MVT) → Separates data, logic, and presentation, which keeps code organized and easy to maintain.
   → Reusability (DRY Principle) → Encourages writing less code by reusing components, reducing errors and duplication.
   → Versatility → Works for small websites, large enterprise apps, APIs, and even machine learning integrations.
   → Community Support → A huge developer community, extensive documentation, and many third-party packages make Django reliable.
   → Built-in Admin Interface → Saves time by giving a ready dashboard to manage data without extra coding.

"""

# 🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️
# ORM [ Object–Relational Mapping. ] :-
# ORM in Django → It connects your Python code (objects/classes) with the database (tables/rows).
# Instead of writing raw SQL queries, you use Python code, and Django ORM automatically translates it into SQL.
#   ex:-
#   Student.objects.filter(marks__gt=80)

# This line in Python is converted by Django ORM into the SQL query:
# SELECT * FROM students WHERE marks > 80;
# So in simple words : -
# ORM = A tool in Django that lets you work with databases using Python code instead of SQL.Would you like me to rewrite
#       your line smoothly as:


# ______________________________________________________________________________________________________________________# ______________________________________________________________________________________________________________________# ______________________________________________________________________________________________________________________# ______________________________________________________________________________________#

"""
How Django is different from other Python frameworks 
> Django is different from other Python frameworks because it is a full‑stack, “batteries‑included” framework that 
  provides almost everything you need out of the box, while others like Flask or FastAPI are lightweight and require 
  more manual setup.
 |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|  
 |      Key Differences Between Django and Other Frameworks                     Key Differences Between Django and Other Frameworks              Key Differences Between Django and Other Frameworks                                     Key Differences Between Django and Other Frameworks                                     Key Differences Between Django and Other Frameworks                                                                           |                                              
 |--------------------------|---------------------------------------------------------------|--------------------------------|------------------------------------------------|------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------| 
 | Feature / Aspect         |            Django                                             |             Flask              |        FastAPI                                 |        Pyramid                           |                        Numpy                                |                          Pandas                                         |                                       skit-Learn                                            |
 |--------------------------|---------------------------------------------------------------|--------------------------------|------------------------------------------------|------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------| 
 | Type                     | Full‑stack, batteries‑included                                 | Lightweight, micro‑framework   | Modern, async‑friendly                          | Flexible, general‑purpose                | Numerical computing library                                 | Data analysis & manipulation library                                    | Machine learning library                                                                    |              
 | Architecture             | MVT (Model–View–Template)                                     | No fixed architecture          | Based on ASGI, async support                   | Configurable (MVC/MVT)                   | Works with ndarray (N‑dimensional arrays)                   | Works with Series (1D) & DataFrame (2D)                                 | Built on NumPy, SciPy, Pandas; modular ML APIs                                              |
 | Best For                 | Large, complex, scalable apps                                 | Small apps, prototypes         | APIs, microservices, async apps                | Complex apps needing customization       | Fast math, linear algebra, numerical ops                    | Handling structured/tabular data (rows/cols)                            | Training ML models, classification, regression, clustering                                  |
 | Learning Curve           | Moderate (many features to learn)                             | Easy (simple and minimal)      | Moderate (new concepts like async, type hints) | Steeper (more configuration)             | Moderate (need math/array concepts)                         | Easy to moderate (Excel‑like operations)                                 | Moderate to steep (ML concepts required)                                                   |
 | Community & Ecosystem    | Huge, mature, widely used                                     | Large, but smaller than Django | Growing rapidly                                | Smaller compared to Django               | Very large, foundation for SciPy, TensorFlow, PyTorch       | Huge in data science, widely used with Jupyter, Matplotlib, Scikit‑Learn |Strong ML community, widely used in AI/ML research and production                           |
 | Built‑in Features        | ORM, Admin panel, Authentication, Forms, Security, Middleware | Minimal, you add extensions    | Fast performance, validation with Pydantic     | Offers flexibility, but fewer built‑ins   | Vectorized operations, broadcasting, random, linear algebra | Data cleaning, filtering, grouping, merging, I/O (CSV, Excel)           | ML algorithms (SVM, Decision Trees, Random Forests, etc.), preprocessing, model evaluation  |
 |--------------------------|---------------------------------------------------------------|--------------------------------|------------------------------------------------|------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|  
 |--------------------------|---------------------------------------------------------------|--------------------------------|------------------------------------------------|------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|

"""


# ______________________________________________________________________________________________________________________# ______________________________________________________________________________________________________________________
"""
How to install and use Django ?
> Django Installation & Usage Guide
    →  Verify Python and pip
    →  pip is the official package installer (package manager) for Python
           python --version
           python -m pip install --upgrade pip

    → Create a Virtual Environment (recommended)
           python -m venv myenv
           # Activate environment:
           # Windows: myenv\Scripts\activate
           # Linux/Mac: source myenv/bin/activate
    
    → Install Django using pip
           pip install django
           # Verify installation:
           python -m django --version
    
    → Start a New Django Project
           django-admin startproject myproject
           cd myproject
    
    → Run Development Server
           python manage.py runserver
           # Open browser at http://127.0.0.1:8000/
    
    → Create a Django App
           python manage.py startapp myapp
           # Register 'myapp' in settings.py under INSTALLED_APPS
    
    → Database Migrations
           python manage.py makemigrations
           python manage.py migrate
    
    → Create Superuser for Admin Panel
           python manage.py createsuperuser
           # Access admin at http://127.0.0.1:8000/admin
    
    ================================================================
    ⚠️ Notes:
        - Always use virtual environments to avoid conflicts.
        - Built-in server is for development only, not production.
        - Keep Django updated: pip install --upgrade django
    =================================================================
"""
# ______________________________________________________________________________________________________________________

