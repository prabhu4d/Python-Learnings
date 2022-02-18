# Django

## Fundaments

1. What’s the difference between a project and an app?\
   An app is a web application that does something – e.g., a blog system, a
   database of public records or a small poll app. A project is a collection
   of configuration and apps for a particular website. A project can contain
   multiple apps. An app can be in multiple projects.

2. name value in used to change the urls without changing in it all other
   place, it is like variable, name is variable, url pattern in value

   ```python
   urlpatterns = [
     path('hello/', view.hello, name="Hello")
   ]
   ```

3. makemigrations app_name

   - makemigrations create a file what are changes made in models.py
   - we can tweaks some thing in migrations file to customize it

4. to see SQL DDLs for your models, it will not migrate

   ```bash
   python manage.py sqlmigrate app_name 0001(file_number)
   ```

5. migrate command is only modifing the database according to models

   ```bash
   python manage.py migrate
   ```

6. migrate commands runs against django_migrations tables what to change.
7. Interactive Mode, we normally use to type python, it will show
   interactivemode, it also works in django as well, but django
   settings will not load, to load django settings use this command

   ```bash
   python manage.py shell
   ```

8. Templates

   - By convention DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.

9. Generic Views
   1. ListView
   2. DetailView

## Commands

- To Create a Project

  ```bash
  django-admin startproject project_name
  ```

- To Create a Super User

  ```bash
  python manage.py createsuperuser
  ```

## Configurating apps

- [to connect postgreSQL](https://dev.to/mungaigikure/how-to-set-up-postgres-in-your-django-project-575i)
