"""Crie uma calculadora utilizando funções
    a. Obrigatoriamente você deve ter funções: somar; subtrair; multiplicar e dividir
        i. Todas recebem 2 números como parâmetro de entrada"""

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

print("\n\n----------CALCULADORA---------\n\n")
while True:
    opcao = input(("Escolha a operação:\n 1. Soma\n 2. Subtracao\n 3. Multiplicacao\n 4. Divisao\n >> "))

    if opcao == '1':
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite um número: "))
        print(soma(numero1, numero2))

    elif opcao == '2':
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite um número: "))
        print(subtracao(numero1, numero2))

    elif opcao == '3':
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite um número: "))
        print(multiplicacao(numero1, numero2))

    elif opcao == '4':
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite um número: "))
        if numero2 == 0:
            print("Não é possível dividir por 0.")
        else:
            print(divisao(numero1, numero2))
    opcao2 = input("Para continuar digite 0 ou 1 para encerrar.\n >> ")
    if opcao2 == '0':
        continue
    else:
        break


