# Blog app example

``` Bash
1. pip install virtualenv
2. mkdir <PROJECT_NAME>
3. cd <PROJECT_NAME>
4. virtualenv .venv
5. linux way: source .venv/bin/activate
   windows way: .venv/Scripts/activate
6. pip install Django Pillow
7. django-admin startproject <PROJECT_NAME> .
8. python manage.py startapp <APP_NAME>
9. python manage.py makemigrations
10. python manage.py migrate
11. python manage.py createsuperuser
12. python manage.py runserver
13. pip freeze > req.txt
14. git init
15. git remote add origin <REPOSITORY_LINK>
16. git add .
17. git commit -m"Commit message"
18. git push origin master
```