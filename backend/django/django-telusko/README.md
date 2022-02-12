# Django Fundamentals

- to create a project
  - django-admin startproject project_name
  - cd project_name
- to create a app in that project
  - python manage.py startapp app_name
- to run the server
  - python manage.py runserver
- to set a static files
  - python manage.py collectstatic
- to create migration files
  - python manage.py makemigrations
- to migrate
  - python manage.py sqlmigrate travello 0001
  - python manage.py migrate