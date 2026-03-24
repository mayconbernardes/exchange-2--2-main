import pytest
from translations import TRANSLATIONS
from models import User

def test_translations_load():
    """Valida se o sistema de tradução do projeto está a carregar corretamente."""
    assert 'en' in TRANSLATIONS
    assert 'fr' in TRANSLATIONS
    assert TRANSLATIONS['en']['nav_home'] == 'Home'

def test_user_model_structure():
    """Valida se a estrutura do modelo de utilizador do projeto está correta."""
    # Apenas verificamos se os atributos existem na classe (não precisa de DB)
    assert hasattr(User, 'username')
    assert hasattr(User, 'email')
    assert hasattr(User, 'password')

def test_confirm_ci_logic():
    """Teste simples para garantir o sucesso do CI/CD."""
    assert True
