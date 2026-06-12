"""
In this module we are discussing:
How to highlight active navigation links dynamically in Django,
using CSS classes, template conditions, and the request object.
"""

# ------------------------------------------------------------------------
# 1. INTRODUCTION TO ACTIVE LINKS
# ------------------------------------------------------------------------
# - In plain HTML/CSS, we can set a class="active" manually:
#       <li class="active"><a href="/about">About</a></li>
# - CSS:
#       .active { background: red; }
#
# - Problem: This is static. It does not change automatically when the user
#   navigates to different pages.
# - Solution: Use Django's request object and template logic to apply "active"
#   dynamically.

# ------------------------------------------------------------------------
# 2. USING {{ request.path }}
# ------------------------------------------------------------------------
# - Django provides the current URL path via {{ request.path }} in templates.
# - Example:
#       {{ request.path }} → "/about/"
#
# - We can compare this with the link path to decide if it should be active.

# ------------------------------------------------------------------------
# 3. TEMPLATE CONDITION FOR ACTIVE CLASS
# ------------------------------------------------------------------------
# Example in base.html or navbar.html:
#
# <li class="{% if request.path == '/' %}active{% endif %}">
#     <a href="{% url 'home' %}">Home</a>
# </li>
#
# <li class="{% if request.path == '/about/' %}active{% endif %}">
#     <a href="{% url 'about' %}">About</a>
# </li>
#
# <li class="{% if request.path == '/services/' %}active{% endif %}">
#     <a href="{% url 'services' %}">Services</a>
# </li>
#
# - This way, only the current page link gets the "active" class.

# ------------------------------------------------------------------------
# 4. USING URL NAME INSTEAD OF PATH
# ------------------------------------------------------------------------
# - Sometimes better to compare with view name instead of raw path.
# - Django provides request.resolver_match.view_name.
# - Example:
#   <li class="{% if request.resolver_match.view_name == 'about' %}active{% endif %}">
#       <a href="{% url 'about' %}">About</a>
#   </li>
#
# - Advantage: If you change the path in urls.py, the active logic still works.

# ------------------------------------------------------------------------
# 5. FOLDER STRUCTURE EXAMPLE
# ------------------------------------------------------------------------
# project_root/
# ├── templates/
# │   ├── base.html        → contains navbar with active logic
# │   ├── home.html
# │   ├── about.html
# │   ├── services.html
# │   └── contact.html
#
# - base.html → defines navigation bar
# - child templates extend base.html
# - active class applied dynamically using request.path or view_name

# ------------------------------------------------------------------------
# 6. ADVANTAGES OF DYNAMIC ACTIVE CLASS
# ------------------------------------------------------------------------
# - User always sees which page is currently active.
# - No need to manually set "active" in each template.
# - Works automatically across all pages.
# - Cleaner and more maintainable navigation.

# ------------------------------------------------------------------------
# 7. BEST PRACTICES
# ------------------------------------------------------------------------
# - Use {% url 'name' %} for links instead of hardcoding paths.
# - Prefer request.resolver_match.view_name for active checks (safer).
# - Keep navbar in base.html and extend it in child templates.
# - Define CSS styles for .active class consistently.

# ------------------------------------------------------------------------
# 8. SUMMARY
# ------------------------------------------------------------------------
# - Static "active" class works in plain HTML but is not dynamic.
# - Django provides {{ request.path }} and request.resolver_match.view_name.
# - Use template conditions to apply "active" only on the current page.
# - This ensures a professional, user-friendly navigation bar.
#
# ------------------------------------------------------------------------
# <!------------------------------------------------------------------------
# Note VVI (Very Very Important):
#
# - {{ request.path }} gives the current URL path (e.g., "/about/").
# - {% if request.path == '/about/' %}active{% endif %} → highlights About link.
# - Better: use request.resolver_match.view_name == 'about' → more reliable.
# - Always connect {% url 'about' %} with the name in urls.py.
# ------------------------------------------------------------------------->


""" 
# LOGIC 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇 LOGICS
# ______ EXTRA ROUGH _____________ EXTRA ROUGH _____________ EXTRA ROUGH _____________ EXTRA ROUGH _________

<h2>My Website</h2>
<nav>
  <ul>
    <!-- Home -->
    <li class="{% if request.resolver_match.view_name == 'second_page' %}active{% endif %}">
      <a href="{% url 'second_page' %}">Home</a>
    </li>

    <!-- About (admin site, not usually customized, but shown here) -->
    <li class="{% if request.path == '/admin/' %}active{% endif %}">
      <a href="/admin">About</a>
    </li>

    <!-- Services -->
    <li class="{% if request.resolver_match.view_name == 'newz_fun_practice' %}active{% endif %}">
      <a href="{% url 'newz_fun_practice' %}">Services</a>
    </li>

    <!-- Contact -->
    <li class="{% if request.resolver_match.view_name == 'new_admin' %}active{% endif %}">
      <a href="{% url 'new_admin' %}">Contact</a>
    </li>
  </ul>
</nav>
</header>


# LOGIC 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇 LOGICS
# ______ EXTRA ROUGH _____________ EXTRA ROUGH _____________ EXTRA ROUGH _____________ EXTRA ROUGH ______

<h2>My Website</h2>
<nav>
  <ul>
    <!-- Home -->
    <li class="{% if request.path == '/' %}active{% endif %}">
      <a href="/">Home</a>
    </li>

    <!-- About -->
    <li class="{% if request.path == '/admin/' %}active{% endif %}">
      <a href="/admin">About</a>
    </li>

    <!-- Services -->
    <li class="{% if request.path == '/pqr/' %}active{% endif %}">
      <a href="/pqr/">Services</a>
    </li>

    <!-- Contact -->
    <li class="{% if request.path == '/xyz/' %}active{% endif %}">
      <a href="{% url 'new_admin' %}">Contact</a>
    </li>
  </ul>
</nav>
</header>
"""
