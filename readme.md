# Messaging App - backend service

instructions:
open up the terminal.

    git clone https://github.com/UrielYair/MessagingApp.git
    cd MessagingApp
    pip install -r requirements.txt

database creation/deletion - database already created - but if needed:
in terminal:

    python
    from app import create_app
    from models.Database import db
    db.create_all(app=create_app()) # in order to set up new database
    db.drop_all(app=create_app()) # in order to delete existing database
    exit()

## start server:

#### Option A:

in terminal:

    FLASK_APP=app.py
    flask run

#### Option B:

in terminal:

    python app.py

After running the server, open your browser and navigate to:
[Swagger Documentation](http://127.0.0.1:5000/apidocs/)

TECH Stack:

Python, Flask, SQLAlchemy, SQLite, Marshmallow, flassger(swagger)

Full list of endpoints are written in swagger documentation:
http://127.0.0.1:5000/apidocs/

feel free to use your favorite way of submitting http request:

-   cURL
-   postman
-   swagger UI

![alt text](https://github.com/UrielYair/MessagingApp/blob/master/swagger_apidocs.png?raw=true)
