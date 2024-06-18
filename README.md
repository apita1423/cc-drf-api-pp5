# 🛰️ Cosmo Chronicles - DRF API 🛰️

Cosmos Chronicles is a social media app that brings users who love anything astronomy together in one place. A user can post, comment, like, and follower other users. Events and News happening in the astronomy world are also posted.

*  🪐 [Cosmos Chronicles - Deployed FE](https://cosmoschronicles-pp5-25951ae1934d.herokuapp.com/)

*  🪐 [Cosmos Chronicles - Deployed BE](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/)

*  🪐 [Cosmos Chronicles - Repository FE](https://github.com/apita1423/cosmoschronicles_pp5)

*  🪐 [Cosmos Chronicles - Repository BE](https://github.com/apita1423/cc-drf-api-pp5)

## 🔭 Table of Contents

- [User Stories](#user-stories)

- [Database Schema](#database-schema)

- [Testing](#testing)
    - [PEP8 Validator](#pep8-validator)
    - [BE - Manual Testing](#be-manual-testing)

- [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks and Libraries Used](#frameworks-and-libraries-used)
    - [Database Used](#database-used)

- [Bugs](#bugs)

- [Deployment](#deployment)
    - [Github](#github)
    - [CI Database](#ci-database)
    - [Project Setup](#project-setup)
    - [Django](#django)
    - [Heroku](#heroku)
    
- [Credits](#credits)
    - [Code Used](#code-used)
    - [Acknowledgments](#acknowledgments)


## 🔭 User Stories

- User Stories are stored in Cosmos Chronicles Frontend Repository. [USER STORIES](https://github.com/apita1423/cosmoschronicles_pp5/issues)


## 🔭 Database Relationship Schema

![Database Relationship Schema Diagram](/static/readme-images/pp5-database.png)


## 🔭 Testing

### PEP8 Validator

- Python code was tested using [CI Python Linter](https://pep8ci.herokuapp.com/). The only errors that appeared were the whitespaces, blank lines, and no newline. These were fixed throughout the code.

- CI Python Linter Errors
![CI Python Linter Errors](/static/readme-images/pep8_errors.png)

- CI Python Linter Cleared Errors
![CI Python Linter Cleared Errors](/static/readme-images/pep8_errors_cleared.png)

| App | Comments | Pass/Fail |
| --- | --- | --- |
| comments | All Files Passed | PASS |
| events | All Files Passed | PASS |
| followers | All Files Passed | PASS |
| likes | All Files Passed | PASS |
| news | All Files Passed | PASS |
| posts | All Files Passed | PASS |
| profiles | All Files Passed | PASS |

### BE - Manual Testing

URLs Testing

| URL | Pass/Fail |
| --- | --- |
| [root](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/) | PASS |
| [/comments/](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/comments/) | PASS |
| [/comments/:id](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/comments/3/) | PASS |
| [/events/](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/events/) | PASS |
| [/events/:id](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/events/2/) | PASS |
| [/followers/](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/followers/) | PASS |
| [/followers/:id](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/followers/144/) | PASS |
| [/likes/](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/likes/) | PASS |
| [/likes/:id](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/likes/12/) | PASS |
| [/news/](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/news/) | PASS |
| [/news/:id](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/news/9/) | PASS |
| [/posts/](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/posts/) | PASS |
| [/posts/:id](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/posts/5/) | PASS |
| [/profiles/](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/profiles/) | PASS |
| [/profiles/:id](https://cc-drf-api-pp5-b19f7ab60297.herokuapp.com/profiles/4/) | PASS |

## 🔭 Technologies Used

### Languages Used

- Python

### Frameworks and Libraries Used

- Django Rest Framework
- Heroku
- Cloudinary
- Pillow
- CORS Headers
- DrawSQL - Used for creating the database relationship scheme.

### Database Used

- Code Institute's PostgresSQL Database

##  🔭 Bugs

- I was having issues with the Django admin account not allowing me to login. It was only letting me see the API admin side. I resolved this issue by creating a staticfiles folder. When I ran `python3 manage.py collectstatic` and deleted the `DISABLE_COLLECTSTATIC` in Heroku, it was able to show me the Django Admin for the frontend database.

##  🔭 Deployment

### Github

#### Create Repository

1. Go to [GitHub](https://github.com/) and login with your credentials.
2. Create a new repository by using [CI's Full Template](https://github.com/Code-Institute-Org/ci-full-template).
3. Click on the 'Use this template' dropdown and click on 'Create a new repository'.
4. Add a 'Repository name' (it show if the name is available underneath the input). Make sure the 'Public' radio button is clicked.
5. Click on 'Create repository' button.

#### Fork Repository

1. In the project's GitHub repository, click 'Fork' and then 'Create a Fork'.
2. Change the name and description of the fork.
3. Select to copy only the main branch or all branches.
4. Click 'Create a Fork'.
5. A newly created repository will appear in the GitHub repository. 

### CI PostgresSQL Database

For this project, I decided to use Code Institute's PostgreSQL Database.

1. Go to [CI's PostgreSQL Database](https://dbs.ci-dbs.net/).
2. Input email address (email address should be the one that is used to sign in to CI's LMS), and click Submit.
3. Once the Submit button is clicked, it starts creating a database.
4. When the database is created, it sends a link to the database to the email that was used.
5. In the email, there is the URL link to the database to use for your DATABASE_URL.

##  🔭 Project Setup

* I used VSCode for the frontend and backend.

## Django

1. Create a GitHub repository with the [CI's Full Template](https://github.com/Code-Institute-Org/ci-full-template).
2. Use `pip3 install` to install these packages:
    ```
    'django<4'
    djangorestframwork
    djangorestframework-simplejwt
    django-cors-headers
    django-filter
    dj3-cloudiary-storage
    dj-rest-auth
    dj-database_url psycopg2
    gunicorn
    Pillow
    ```
3. Create a django project with this command: `django-admin startproject project-name .`
4. In the project's Heroku, go to settings and click on 'Reveal Config Vars". Add: (for this project)
    ```
    KEY: ALLOWED HOST VALUE: .herokuapp
    KEY: CLOUDINARY_URL: VALUE: (hidden)
    KEY: DATABASE_URL VALUE: (hidden)
    KEY: SECRET_KEY VALUE: (hidden)
    ```
    To connect the backend to the frontend:
    ```
    KEY: CLIENT_ORIGIN VALUE: https://cosmoschronicles-pp5-25951ae1934d.herokuapp.com
    KEY: CLIENT_ORIGIN_DEV VALUE: (local host)
    ```
5. Remember to remove trailing `/`.
6. Create a env.py file in the root of the project. Add this:
    ```
    import os

    os.environ['CLOUDINARY_URL] = (hidden)
    os.environ['DATABASE_URL] = (hidden)
    os.environ['SECRET_KEY] = (hidden)
    os.environ['DEV'] = '0'
    os.environ['CLIENT_ORIGIN'] = (hidden)
    os.environ['CLIENT_ORIGIN_DEV] = (hidden)
    os.environ.setdefault['SECRET_KEY] = (hidden)
    ```
7. Set up settings.py
   
    - <strong>Imports and Cloudinary:</strong>
    ```
    from pathlib import Path
    import os
    import dj_database_url
    import re

    if os.path.exists('env.py):
        import env
    
    CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
    }
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```
    - <strong>REST_FRAMEWORK:</strong>
    ```
    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
    }
    if 'DEV' not in os.environ:
        REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
            'rest_framework.renderers.JSONRenderer',
        ]
    ```
    - <strong>JSON Web Token</strong>
    ```
    REST_USE_JWT = True
    JWT_AUTH_SECURE = True
    JWT_AUTH_COOKIE = 'my-app-auth'
    JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
    JWT_AUTH_SAMESITE = 'None'

    REST_AUTH_SERIALIZERS = {
        'USER_DETAILS_SERIALIZER': 'drf_api_pp5.serializers.CurrentUserSerializer'
    }
    ```
    - <strong>DEBUG and ALLOWED_HOSTS</strong>
    ```
    DEBUG = 'DEV' in os.environ

    ALLOWED_HOSTS = [
        os.environ.get('ALLOWED_HOST),
        'localhost',
    ]
    ```
     - <strong>Add to `INSTALLED_APPS`:</strong>
    ```
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'django-filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    ```

    - <strong>SITE_ID and MIDDLEWARE</strong>

    Add `SITE_ID = 1` underneath `INSTALLED_APPS` and add
    `'corsheaders.middleware.CorsMiddleware',` to the top of `MIDDLEWARE`.

    - <strong>CORS_ALLOWED</strong>
    Underneath MIDDLEWARE add `CORS_ALLOWED`
    ```
    if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN'),
        'https://cosmoschronicles-pp5-25951ae1934d.herokuapp.com',
        'http://localhost:3000',
    ]

    if 'CLIENT_ORIGIN_DEV' in os.environ:
        extracted_url = re.match(r'^([^.]+)', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)

        CORS_ALLOWED_ORIGIN_REGEXES = [
            rf"{extracted_url}.(eu|us)\d+\.code-institute-ide\.net$",
        ]

    CSRF_TRUSTED_ORIGINS = [os.environ.get('CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN')]

    CORS_ALLOW_CREDENTIALS = True
    ```

    - <strong>Update DATABASES</strong>
    ```
    if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
    ```

8. Create a Procfile in the root of the project and add:
    ```
    release: python3 manage.py makemigrations && python3 manage.py migrate
    web: gunicorn project_name.wsgi
    ```

9. Migrate Database:
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

10. Add to requirements.txt: `pip3 freeze --local > requirements.txt`

11. Add, Commit, and Push to GitHub.
12. Head to Heroku and Deploy Branch

### Heroku

1. Go to [Heroku](https://id.heroku.com/login) and login with your credentials.
2. Sign in with your multifactor pin.
3. Select "New".
4. Create a unique name (it should turn green if the name is available) and select the location.
5. Once the app is created, click on Settings and click on 'Reveal Config Vars'
    - ALLOWED_HOST
    - CLIENT_ORIGIN
    - CLIENT_ORIGIN_DEV
    - CLOUDINARY_URL
    - DATABASE_URL
    - SECRET_KEY
6. Under the 'Deploy' button, connect to your GitHub repository.
7. Once connected, pick the repository that you will want to connect to.
8. Under 'Manual Deploy', click on Deploy Branch.
9. Once manual deployment is successful click on 'View' or scroll up and click on 'Open App'

##  🔭 Credits

### Code Used

- I relied on CI's Django REST Framework Walkthrough, with the addition of two apps: news and events.

### Acknowledgments

- Again, and for the last time, I'm truly grateful for my mentor, Martina. She has been the best mentor someone could ask for. 

- Oisin, John, and Thomas from Tutor Support, who helped with a few issues that came up. 

- My husband who has encouraged me throughout the course, and, of course, my animals who have been okay with me being in front of a computer and not being a bed for them to relax. After this I can go back to being a bed 🤪.
