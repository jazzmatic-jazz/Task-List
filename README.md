# Basic Project Setup and Configuration:

1. Create virtual environment to store the dependecies
    **py -m venv env**

2. Install dependencies: **pip install django, django-environ**

3. Start project:
    **django-admin startproject tasks**

4. Create Applicaton:
    **py manage.py startapp app**

5. Make **requirements.txt** file for displaying all the dependencies and for easy installation

6. Add the **"app"** in the INSTALLED_APPS of settings.py file in project directory

7. Create **.env** to store the secret credentials, configuration settings, environment variables

8. create **.gitignore** to ignore files and they will not get tracked

9. Run migrations to setup the database
    **py manage.py makemigrations**
    **py manage.py migrate**

10. Create Superuser:
    **py manage.py createsuperuser**
    