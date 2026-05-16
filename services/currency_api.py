import requests

def obter_cotacao_dolar():
    """Busca a cotação atual do Dólar para Real via AwesomeAPI."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Levanta erro se a API falhar
        dados = response.json()
        # O campo 'bid' é o valor de compra atual
        return float(dados["USDBRL"]["bid"])
    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
        return None

# Exemplo de uso na sua precificação:
# preco_dolar = obter_cotacao_dolar()
# se custo_materia_prima for em dólar:
#    custo_em_reais = custo_materia_prima * preco_dolar