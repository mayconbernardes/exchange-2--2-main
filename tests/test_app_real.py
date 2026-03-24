import os
os.environ['FLASK_ENV'] = 'testing'

import pytest
from app import app, db

@pytest.fixture
def client():
    # Forçamos o modo de teste e base de dados em memória
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_home_page(client):
    """Verifica se a página inicial do projeto carrega."""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Verifica se a página de login do projeto carrega."""
    response = client.get('/login')
    assert response.status_code == 200
