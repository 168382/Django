# Django

## Setting Up the Environment
Create a Virtual Environment and running it:
Creating command: python -m venv .venv 
Activation command: .\.venv\Scripts\Activate.ps1

Installing Django: pip install django
Create Project: django-admin startproject ECommerce 
cd ECommerce

Create App (Customer and order):
                                 python manage.py startapp Customer
                                python manage.py startapp order
Update INSTALLED_APPS in ECommerce/settings.py to include your order and Customer.


##  Running the Project
1. Apply Migrations: python manage.py makemigrations 
                  Create migrations python manage.py migrate 
                  Apply migrations to database

2. Start Development Server:
  python manage.py runserver