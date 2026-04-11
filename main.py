from src.calculator import Precificador

def menu():
    app = Precificador()
    print(f"--- Calculadora de Precificação v{app.versao} ---")
    print("Ajude seu pequeno negócio a prosperar!\n")

    try:
        mat = float(input("Custo dos materiais (R$): "))
        horas = float(input("Horas gastas no trabalho: "))
        v_hora = float(input("Quanto vale sua hora (R$): "))
        lucro = float(input("Margem de lucro desejada (%): "))

        resultado = app.calcular_preco_final(mat, horas, v_hora, lucro)
        
        print(f"\n✅ Sugestão de Preço de Venda: R$ {resultado}")
        print("---------------------------------------")
    except ValueError as e:
        print(f"\n❌ Erro: {e}. Digite apenas números positivos.")

if __name__ == "__main__":
    menu()
