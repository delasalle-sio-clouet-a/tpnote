import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.classes.CDatabase import Database
from src.classes.CMockHandler import MockHandler

@pytest.fixture(scope="session")
def database():

    handler = MockHandler()
    database = Database(handler)

    yield database