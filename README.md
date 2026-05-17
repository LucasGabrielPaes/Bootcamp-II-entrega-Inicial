## 1. Visão Geral e Problema Real
Muitos microempreendedores, artesãos e freelancers enfrentam dificuldades ao definir o preço de venda dos seus produtos ou serviços. O erro mais comum é ignorar o custo da própria mão de obra, resultando em negócios que não dão lucro.

Este projeto resolve essa demanda através de uma **Calculadora de Precificação**. A aplicação automatiza o cálculo com base em custos de materiais, horas de trabalho e margem de lucro, garantindo uma visão financeira clara para o empreendedor.

---

## 2. Funcionalidades Principais
* **Cálculo de Custo de Produção:** Soma automática de materiais e valor da hora de trabalho.
* **Cálculo de Lucro:** Aplicação de margem percentual sobre o custo total.
* **Integração com API:** Consumo de dados em tempo real via AwesomeAPI para conversão do preço final em Dólar (USD).
* **Tratamento de Erros:** Sistema que impede a entrada de valores negativos ou inválidos.
* **Interface CLI:** Interface de linha de comando simples e funcional.

---

## 3. Tecnologias Utilizadas
* **Linguagem:** [Python 3.12+]
* **Bibliotecas Externas:** [Requests]
* **Testes:** [Pytest] (Garante a fiabilidade dos cálculos)
* **Linting:** [Ruff] (Garante a qualidade e padronização do código)
* **CI/CD:** [GitHub Actions] (Pipeline de integração contínua)

---

##  4. Como Instalar e Executar

### Pré-requisitos
* Ter o Python instalado (v3.10 ou superior).

### Instalação
1. Clone o repositório:
   ```bash
   https://github.com/LucasGabrielPaes/Bootcamp-II-entrega-Inicial.git

### Para iniciar a Calculadora, use o comando:
1. Copie e Cole no Terminal:
   ```bash
   python main.py
### Demonstração do Simulador
<img src="https://github.com/LucasGabrielPaes/Bootcamp-II-entrega-Inicial/blob/main/ScreenShot/teste2.png?raw=true" alt="Texto Alternativo">

### Demonstração do Teste
<img src="https://github.com/LucasGabrielPaes/Bootcamp-II-entrega-Inicial/blob/main/ScreenShot/teste%20codigo.png?raw=true" alt="Texto Alternativo">

### Estrutura 
<img src="https://github.com/LucasGabrielPaes/Bootcamp-II-entrega-Inicial/blob/main/ScreenShot/estrutura2.png?raw=true" alt="Texto Alternativo">

### Instalação de Dependências
Caso mude de Computador, instale as bibliotecas necessárias com:
   ```bash
pip install -r requirements.txt
