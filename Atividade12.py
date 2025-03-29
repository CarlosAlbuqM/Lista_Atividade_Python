""" Crie uma função que converta uma temperatura de Celsius para Fahrenheit e vice-versa. """

def conversor_temperaturas(valor, tipo):
    if tipo == 'C':
        return (9/5 * valor) + 32
    elif tipo == 'F':
        return (valor - 32) * 5/9
    else:
        return 'Tipo inválido.'

print("----CONVERSOR DE TEMPERATURAS----")

opcao = int(input("Qual temperatura deseja converter? \n 1. Celsius para Fahrenheit \n 2. Fahrenheit para Celcius \n >> "))

if opcao == 1:
    CtoF = float(input("Digite a temperatura em Celcius: "))
    print(f"A temperatura em fahrenheit é {conversor_temperaturas(CtoF, 'C')}°F")
elif opcao == 2:
    FtoC = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"A temperatura em celcius é {conversor_temperaturas(FtoC, 'F'):.1f}°C")
else: 
    print("Opção inválida. Tente novamente.")