import sys
import os

def test_app_import():
    """Tenta importar o app e captura o erro exato para o log do GitHub."""
    print("\n--- INÍCIO DO DIAGNÓSTICO DE IMPORTAÇÃO ---")
    try:
        # Tenta importar o Flask app
        from app import app
        print("✅ Sucesso: O aplicativo foi importado corretamente!")
        
        # Verifica a configuração da base de dados
        print(f"DEBUG: SQLALCHEMY_DATABASE_URI = {app.config.get('SQLALCHEMY_DATABASE_URI')}")
        print(f"DEBUG: TESTING = {app.config.get('TESTING')}")
        
    except ImportError as e:
        print(f"❌ ERRO DE IMPORTAÇÃO: {e}")
        print("Dica: Verifique se todas as bibliotecas do requirements.txt estão instaladas.")
        raise e
    except Exception as e:
        print(f"❌ ERRO FATAL AO INICIAR O APP: {e}")
        import traceback
        traceback.print_exc()
        raise e
    print("--- FIM DO DIAGNÓSTICO ---\n")
