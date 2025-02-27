import pytest

from src.classes.CDatabase import Database
from src.classes.CMockHandler import MockHandler


# a faire : fixtures
@pytest.fixture(scope="session")
def database():

    handler = MockHandler()
    db = Database(handler)

    yield db