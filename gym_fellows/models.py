from flask import Flask
from flask_sqlalchemy import SQLAlchemy	


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://baliks:password123@localhost/flask_gym'
database_connection = SQLAlchemy(app)


class Person(database_connection.Model):
    username = database_connection.Column(database_connection.String(10), primary_key=True, unique=True, nullable=False)
    password = database_connection.Column(database_connection.String(10), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


