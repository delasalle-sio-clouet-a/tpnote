import pytest
from flask.testing import FlaskClient

def test_route_hello(client:FlaskClient):
    # résultat attendu : "Hello !"
    response = client.get("/api/hello")
    assert str(response.json["statut"]) == "1"
    assert "Hello !" in str(response.json["message"])