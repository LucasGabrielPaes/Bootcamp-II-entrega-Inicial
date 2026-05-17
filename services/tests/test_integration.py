import pytest
from services.currency_api import obter_cotacao_dolar

def test_conexao_api_cotacao():
    """Valida se a API retorna um valor numérico válido."""
    cotacao = obter_cotacao_dolar()
    
    assert cotacao is not None
    assert isinstance(cotacao, float)
    assert cotacao > 0  # O dólar nunca será grátis, infelizmente!