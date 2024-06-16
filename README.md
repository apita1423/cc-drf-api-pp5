# 🛰️ Cosmo Chronicles - DRF API 🛰️

Cosmos Chronicles is a social media app that brings users who love anything astronomy together in one place. A user can post, comment, like, and follower other users. Events and news happening in the astronomy world are also posted.

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

- [Project Setup](#project-setup)

- [Deployment](#deployment)
    - [Github](#github)
    - [Heroku](#heroku)
    - [CI Database](#ci-database)

- [Credits](#credits)
    - [Code Used](#code-used)
    - [Acknowledgments](#acknowledgments)


## 🔭 User Stories


## 🔭 Database Relationship Schema

![Database Relationship Schema Diagram](/static/readme-images/pp5-database.png)


## 🔭 Testing

### PEP8 Validator

- Python code was tested using ![CI Python Linter](https://pep8ci.herokuapp.com/). The only errors that appeared were the whitespaces, blank lines, and no newline. These were fixed throughout the code.

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

##  🔭 Project Setup

##  🔭 Deployment

### Github

### Heroku

### CI Database

##  🔭 Credits

### Code Used

- I relied on CI's Django REST Framework Walkthrough, with the addition of two apps: news and events.

### Acknowledgments

- Again, and for the last time, I'm truly grateful for my mentor, Martina. She has been the best mentor someone could ask for. 

- Oisin, John, and Thomas from Tutor Support, who helped with a few issues that came up. 

- My husband who has encouraged me throughout the course, and, of course, my animals who have been okay with me being in front of a computer and not being a bed for them to relax. After this I can go back to being a bed. 


