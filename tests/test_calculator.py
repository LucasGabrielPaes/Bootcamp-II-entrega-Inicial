import pytest
from src.calculator import Precificador

def test_calculo_sucesso():
    app = Precificador()
    # Material: 10, 2h trabalho a 20/h, 50% lucro -> (10 + 40) * 1.5 = 75
    assert app.calcular_preco_final(10, 2, 20, 50) == 75.0

def test_valor_negativo_deve_falhar():
    app = Precificador()
    with pytest.raises(ValueError):
        app.calcular_preco_final(-10, 1, 20, 10)

def test_margem_zero_lucro():
    app = Precificador()
    # Se a margem é 0, o preço é apenas o custo de produção
    assert app.calcular_preco_final(50, 0, 0, 0) == 50.0