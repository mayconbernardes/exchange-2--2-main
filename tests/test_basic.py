import pytest

def test_basic_arithmetic():
    """Teste simples que sempre passa para validar o CI."""
    assert 1 + 1 == 2

def test_python_version():
    """Verifica se o Python está a funcionar."""
    import sys
    assert sys.version_info.major == 3
