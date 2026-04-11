class Precificador:
    def __init__(self, versao="1.0.0"):
        self.versao = versao

    def calcular_preco_final(self, custo_material, horas_trabalhadas, valor_hora, margem_lucro):
        """
        Calcula o preço final baseado em custos, tempo e lucro.
        Fórmula: (Material + (Horas * Valor/Hora)) * (1 + Margem/100)
        """
        if custo_material < 0 or horas_trabalhadas < 0 or valor_hora < 0:
            raise ValueError("Os valores de entrada não podem ser negativos.")
            
        custo_producao = custo_material + (horas_trabalhadas * valor_hora)
        preco_final = custo_producao * (1 + (margem_lucro / 100))
        
        return round(preco_final, 2)