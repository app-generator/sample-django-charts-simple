# [Django Simple Charts](https://django-simple-charts.appseed.us/) - LIVE Demo

> Playground starter to display simple charts in Django using Morris JS: 

- [Charts from JSON](https://django-simple-charts.appseed.us/charts-file) - using this [sample](https://github.com/app-generator/django-simple-charts/blob/master/sample_data/chart_morris.json)
- [Charts from Table](https://django-simple-charts.appseed.us/charts-input) - simple STATS table
- [Charts from DATA chunk](https://django-simple-charts.appseed.us/charts-input) - using this [sample](https://github.com/app-generator/django-simple-charts/blob/master/sample_data/sales_data.csv) file
- UI Kit: **[Datta Able](https://appseed.us/admin-dashboards/django-dashboard-dattaable)** (Lite Version) provided by **[CodedThemes](https://appseed.us/agency/codedthemes)**
- Deployment scripts: Docker, Gunicorn / Nginx
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup) provided by **AppSeed**

<br />

> Links

- [LIVE Demo](https://django-simple-charts.appseed.us/) - project in action
- [Generic Codebase](https://github.com/app-generator/boilerplate-code-django-dashboard)
- [Morris Charts](https://morrisjs.github.io/morris.js/) - Getting started guide

<br />

![Boierplate Code Django Dashboard - Template project provided by AppSeed.](https://raw.githubusercontent.com/app-generator/django-simple-charts/master/media/display.png)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-simple-charts.git
$ cd django-simple-charts
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create app superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a admin user using the `createsuperuser` command

<br />

## Load Data For Chart

In Django admin, you can import data for the **Sales** section. 
To do this just click on ```IMPORT``` button then select your csv, xls or etc file and submit it.

![Import Data](https://raw.githubusercontent.com/app-generator/django-simple-charts/master/media/admin_import.png)

> Sample **[Data](https://github.com/app-generator/django-simple-charts/blob/master/sample_data/sales_data.csv)**

<br>

## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app logic and serve the static assets
   |    |-- settings.py                    # Django app bootstrapper
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                  # Master pages
   |         |    |-- base-fullscreen.html # Used by Authentication pages
   |         |    |-- base.html            # Used by common pages
   |         |
   |         |-- accounts/                 # Authentication pages
   |         |    |-- login.html           # Login page
   |         |    |-- register.html        # Register page
   |         |
   |      index.html                       # The default page
   |     page-404.html                     # Error 404 page
   |     page-500.html                     # Error 404 page
   |       *.html                          # All other HTML pages
   |
   |-- authentication/                     # Handles auth routes (login and register)
   |    |
   |    |-- urls.py                        # Define authentication routes  
   |    |-- views.py                       # Handles login and registration  
   |    |-- forms.py                       # Define auth forms  
   |
   |-- app/                                # A simple app that serve HTML files
   |    |
   |    |-- views.py                       # Serve HTML pages for authenticated users
   |    |-- urls.py                        # Define some super simple routes  
   |
   |-- requirements.txt                    # Development modules - SQLite storage
   |
   |-- .env                                # Inject Configuration via Environment
   |-- manage.py                           # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/django-simple-charts.git
$ cd django-simple-charts
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Django Simple Charts](https://django-simple-charts.appseed.us/) - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
