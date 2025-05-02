# 🍋 Little Lemon – Full Stack Django Web App
A professional restaurant reservation system built with Django. Includes booking, menu browsing, and embedded Google Maps, all wrapped in a responsive design.

## Features
**Dynamic Homepage** – Hero banner, promo section, and call-to-action links

**Booking System** – Django form with CSRF protection and Google Maps integration

**Menu Pages** – Dynamic menu listing and individual item pages

**Responsive Design** – Mobile-friendly layout using custom media queries

## Tech Stack
**Backend:** Django, Python

**Frontend:** HTML5, CSS3

**Templating:** Django Template Language ({% url %}, {% static %}, {% csrf_token %})

## Getting Started
**Prerequisites**

Python 3

Pipenv (Python package manager)

**Installation**


1. Clone the repository:

```git  clone https://github.com/hasanm4-6/littlelemon.git```

```cd littlelemon```

2. Install dependencies and create virtual environment

```pipenv install```

3. Activate the Pipenv shell

```pipenv shell```

4. Install Django 

```pip install django```

5. Install mysqlclient

```pip install mysqlclient```

6. Apply database migrations

```python manage.py migrate```

7. Start the development server

```python manage.py runserver```



Visit http://127.0.0.1:8000 to view the app in your browser.

## Contributing
Contributions are welcome! Feel free to fork the repo, open issues, or submit pull requests.
