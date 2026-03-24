import os
os.environ['FLASK_ENV'] = 'testing'

import pytest
from app import app


@pytest.fixture
def client():
    """Configure l'application en mode test et retourne un client de test."""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Désactive CSRF pour les tests
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        yield client


def test_homepage_redirects(client):
    """La page d'accueil doit répondre (200 ou redirection 302 si login requis)."""
    response = client.get('/')
    assert response.status_code in [200, 302]


def test_login_page_accessible(client):
    """La page de login doit être accessible."""
    response = client.get('/login')
    assert response.status_code in [200, 302]


def test_register_page_accessible(client):
    """La page d'inscription doit être accessible."""
    response = client.get('/register')
    assert response.status_code in [200, 302]


def test_invalid_login(client):
    """Une tentative de login invalide doit retourner 200 (formulaire affiché)."""
    response = client.post('/login', data={
        'email': 'faux@email.com',
        'password': 'mauvais_mot_de_passe'
    }, follow_redirects=True)
    assert response.status_code == 200
