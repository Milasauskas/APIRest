from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
import metrics


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:////database/storage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


manager = APIManager(app, flask_sqlalchemy_db=db)

