# Project Title

A brief description of your project and what it does.

## Prerequisites

- Python 3.6+
- Django 3.2+
- Recommended to use a virtual environment.

## Set Up a Virtual Environment

```
python3 -m venv venv

source venv/bin/activate

```

```
Linux
venv\Scripts\activate
```

## Install Dependencies
Make sure a requirements.txt file is present with the required dependencies:



### Install dependencies using:

```
pip install -r requirements.txt
```

## Running the Project

### Database Setup

Run migrations to set up the database:

```
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (for Admin Access)

To create a superuser, run:

```
python manage.py createsuperuser
```

### Start the Development Server

Run the server:

```
python manage.py runserver
```

The project should now be accessible at 

```
http://127.0.0.1:8000/.
```

## Static Files
Collect Static Files (for production)

```
python manage.py collectstatic
```

Ensure the STATIC_URL and STATICFILES_DIRS settings are configured correctly in settings.py for proper handling of CSS, JS, and image files.

