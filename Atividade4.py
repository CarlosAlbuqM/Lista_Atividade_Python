"""Refatorar 
    a. Feita a questão 3 crie uma função calcular que recebe 3 parâmetros:
        i. numero1, numero2 e operação (pode ser somar; subtrair; multiplicar e dividir)"""

def calculadoraPro(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    elif z == '/':
        return x / y

try:
    print("\n\n----------CALCULADORA---------\n\n")
    while True:
        opcao = input(("Escolha a operação ou 0 para sair:\n +. Soma\n -. Subtracao\n *. Multiplicacao\n /. Divisao\n >> "))

        if opcao == '0':
            print("Até mais")
            break

        elif opcao != '+' and opcao != '-' and opcao != '*' and opcao != '/':
            print("Operação inválida")

        else: 
            numero1 = float(input("Digite um número: "))
            numero2 = float(input("Digite outro número: "))
            print(calculadoraPro(numero1, numero2, opcao))

except ZeroDivisionError:
    print("Não é possível dividir por 0.")