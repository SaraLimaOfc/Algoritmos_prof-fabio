import operator
import time

def mostrar_tabuada(numero, operacao):
    print(f"\nTabuada de {operacao} para o número {numero}:")

    operacoes = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    for i in range(1, 11):
        if operacao in operacoes:
            if operacao == "/":
                if i != 0:
                    resultado = operacoes[operacao](numero, i)
                    print(f"{numero} / {i} = {resultado:.2f}")
            else:
                resultado = operacoes[operacao](numero, i)
                print(f"{numero} {operacao} {i} = {resultado}")
   
        time.sleep(0.5)

def tabuada_completa(numero):
    print(f"\nTabuada completa para o número {numero}:")
    for operacao in ["+", "-", "*", "/"]:
        mostrar_tabuada(numero, operacao)

while True:
    print("\nMenu:")
    print("1. Fazer tabuada personalizada")
    print("2. Ver tabuada completa de um número")
    print("3. Sair do programa")

    opcao = input("Escolha uma opção (1, 2, ou 3): ")

    if opcao == "1":
        numero = int(input("Digite o número desejado: "))
        operacao = input("Escolha o operador aritmético desejado (+, -, *, /): ")
        mostrar_tabuada(numero, operacao)
        
    elif opcao == "2":
        numero = int(input("Digite o número para ver a tabuada completa: "))
        tabuada_completa(numero)

    elif opcao == "3":
        print("Fim do programa")
        break
