import datetime

def login():
    username = input("Usuário: ").strip()
    password = input("Senha: ").strip()
    if username == "Sara Lima" and password == "2468":
        print("Acesso Permitido")
        return True
    else:
        print("Acesso Negado")
        return False

def calcular_idade():
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de Nascimento: "))
    ano_atual = datetime.datetime.now().year  # Obtendo o ano atual
    if ano_nascimento > ano_atual:
        print("Por favor, insira um ano de nascimento válido.")
        return
    idade = ano_atual - ano_nascimento
    print(f"{nome}, sua idade é {idade} anos.")

def calcular_imc():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    if altura <= 0:
        print("Por favor, insira valores válidos.")
        return
    imc = peso / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}.")
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Classificação: Peso ideal")
    elif 25 <= imc < 30:
        print("Classificação: Acima do peso")
    else:
        print("Classificação: Acima do peso")

def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))
    
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            print("Erro: Divisão por zero.")
            return
        resultado = num1 / num2
    else:
        print("Operador inválido.")
        return

    print(f"O resultado é: {resultado}")

def main():
    if login():
        while True:
            print("\nMenu:")
            print("1. Calculadora")
            print("2. Cálculo de IMC")
            print("3. Cálculo de Idade")
            print("4. Sair")

            escolha = input("Escolha uma opção (1-4): ")
            if escolha == '1':
                calculadora()
            elif escolha == '2':
                calcular_imc()
            elif escolha == '3':
                calcular_idade()
            elif escolha == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
