# Django REST API challenge
REST API for retrieving, creating and updating countries

## Prerequisities
- Python
- Django Rest Framework 

## Migrate and seed database
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py loaddata seed.json`

## Run
- `python manage.py runserver`
- application runs on localhost port 8000

## Usage 
Use following endpoints either with your browser or some suitable tool e.g. Postman 
- http://127.0.0.1:8000/countries/  (GET, POST)
- http://127.0.0.1:8000/countries/≤id>/ (GET, PUT, DELETE)

for more information have a look in `api.yaml`

! Additional notes and comments are available in `DeveloperJournal.txt`
