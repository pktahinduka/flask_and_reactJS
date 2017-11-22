# flask_and_reactJS
#### This project is meant to demonstrate the a combination of Python backend and ReactJS frontend coupled with a set of other technologies.
[![Build Status](https://travis-ci.org/pktahinduka/flask_and_reactJS.svg?branch=master)](https://travis-ci.org/pktahinduka/flask_and_reactJS)
[![Coverage Status](https://coveralls.io/repos/github/pktahinduka/shopeasy-flask-rest-api/badge.svg?branch=TravisCI-Test)](https://coveralls.io/github/pktahinduka/shopeasy-flask-rest-api?branch=TravisCI-Test)

#### Installation

Please ensure that development libraries for [PostgreSQL](http://techarena51.com/index.php/flask-sqlalchemy-postgresql-tutorial/) are installed.

#### Step 1: Clone the project to your application folder.

    git clone https://github.com/pktahinduka/flask_and_reactJS

#### Step 2: Install the requirements and add your Database configuration details.

    pip install -r requirements.txt

    vim config.py
    Fill in your database username, password, name, host etc

#### Step 3 : Create the necessary databases along with their tables

     - python manage.py db init
     - python manage.py db migrate
     - python manage.py db upgrade
     

#### Step 4: Run the application 
     
     - python manage.py runserver

#### Step 5: Run tests for the routes and configurations
    
     - python manage.py test

#### Step 5: Run coverage for the routes and configurations
    
     - python manage.py cov