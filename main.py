from src.calculator import Precificador
# 1. IMPORTAR A FUNÇÃO DA API
from services.currency_api import obter_cotacao_dolar

def menu():
    app = Precificador()
    print(f"--- Simulador de Precificação v{app.versao} ---")
    print("Ajude seu pequeno negócio a prosperar!\n")

    try:
        mat = float(input("Custo dos materiais (R$): "))
        horas = float(input("Horas gastas no trabalho: "))
        v_hora = float(input("Quanto vale sua hora (R$): "))
        lucro = float(input("Margem de lucro desejada (%): "))

        resultado = app.calcular_preco_final(mat, horas, v_hora, lucro)
        
        print(f"\n✅ Sugestão de Preço de Venda: R$ {resultado}")
        print("---------------------------------------")

        # 2. CHAMAR A API E MOSTRAR O VALOR EM DÓLAR
        print("Buscando cotação do dólar para exportação...")
        dolar = obter_cotacao_dolar()
        
        if dolar:
            preco_dolar = resultado / dolar
            print(f"💵 Preço convertido: US$ {preco_dolar:.2f} (Cotação: R$ {dolar})")
        else:
            print("⚠️ Não foi possível converter para dólar no momento.")
        
        print("---------------------------------------")

    except ValueError as e:
        print(f"\n❌ Erro: {e}. Digite apenas números positivos.")

if __name__ == "__main__":
    menu()
    