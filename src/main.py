import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from src.classes.CDatabase import Database
from src.classes.CSqlHandler import SqlHandler
from src.classes.CDataHandler import DataHandler
from src.classes.CSqlHandler import SqlHandler

def create_app(_config) -> Flask:
    app:Flask = Flask(__name__)

    handler:SqlHandler = SqlHandler()
    handler.set_app(app)
    handler.set_connection_data("postgresql+pg8000","localhost","innomop","laval53","tpnote")
    handler.init_db()
    database:Database = Database(handler)

    return app, database