"""
_____________________________________________________________________________________________________________
# ________________________________Django Project Setup and Execution Guide___________________________________#
 _____________________________________________________________________________________________________________

## 1. Create a New Project
- First, create a folder where you want to store the project.
  Example: xyz
- Navigate to that folder in CMD/Terminal:
    C:\Users\<YourName>\xyz>
- Run the command to create a new Django project:
    django-admin startproject MyProjectName
- This will automatically generate:
    - manage.py file
    - A new subfolder (MyProjectName) inside xyz


## 2. Run the Project
- Open CMD/Terminal inside the project folder (xyz).
- Execute the following command:
    python manage.py runserver
- After successful execution, you will see:
    Starting development server at http://127.0.0.1:8000/
- Copy the IP address (http://127.0.0.1:8000/) and open it in your browser.


## 3. Change the Port Number
- By default, Django runs on port 8000 (http://127.0.0.1:8000).
- If another application (like AngularJS or Node.js) is already using port 8000, a collision occurs.
- To change the port number, run:
    python manage.py runserver 4444
- Now the server will start at:
    Starting development server at http://127.0.0.1:4444/
- Access your project at http://127.0.0.1:4444/


## After Run the server setup own IDE
-  we have many of them like VsCode, Pycharm, Jupiter Notebook...etc
   I think VsCode is better for development then other according to your preference choose your IDE.

"""