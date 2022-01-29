# Django_Project
## Create and Start 
## django raw project

Use the following command:

```bash

pipenv shell

mkdir storefront

cd storefront

pipenv install django

django-admin startproject

python manage.py runserver
```

--- create new app

```bash
python manage.py startapp playground
```
--- migrations

```bash
python3 manage.py makemigrations ## create migration script

python3 manage.py migrate ## start creating db and run migration scripts

python3 manage.py migrate store 0003 ## revert back to specific migration or undo

```

## MySQL for WSL2

 - Update your Ubuntu packages: sudo apt update
- install MySQL with: sudo apt install mysql-server
- Start a MySQL server: sudo /etc/init.d/mysql start
- Start the security script prompts: sudo mysql_secure_installation
- Open the MySQL prompt: sudo mysql

## mysql driver for django
pipenv install mysqlclient

- if error : 

sudo apt-get install libmysqlclient-dev

# for premission root issue on django 
follow below steps to create new user name and grant privillages

- create user 'django'@'localhost' identified by 'django-user-password';
- grant usage on *.* to 'django'@'localhost';
- grant all privileges on django-database-1.* to 'django'@'localhost';




  