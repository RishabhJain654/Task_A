# Task_A
Task for Learning
This is project is made in Python 3.6 using Django 1.11 in Windows platform.

Pre-Requisites
1. Windows OS.
2. Python 3.6 for Windows.
3. Django 1.11 for Windows.
4. Postgres 9.6 for Windows.
5. A Postgres DB named "task", username "admin" and password "admin".
6. Following Python modules need to be installed additionally:
  a) Django Rest Framework: It can be installed in cmd using command "pip install djangorestframework".
  b) Requests: It can be installed in cmd using command "pip install requests".
  c) Httpie: It can be installed in cmd using command "pip install httpie".

Note:
1. This project is developed in Virtual Environment. It can be installed without it but it is not recommended.
2. This project is developed using Atom software.

Installation
1. Download the files and extract them in a directory.
2. Open the cmd in Windows and go to the location where the above files are stored.
3. Type "python manage.py makemigrations" to create the database structure in PostgreSQL. Then type "python manage.py migrate". Now you      have a database structure for the application.
4. To run the server type "python manage.py runserver". Now go to browser and type 127.0.0.1:8000 as URL.
