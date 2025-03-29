""""Faça um programa, com uma função que necessite de um parâmetro “número”. A função retorna o valor de
caractere ‘P’, se seu valor for positivo, e ‘N’, se seu valor for zero ou negativo."""

def classifica_numero(x):
    if x > 0:
        return 'P'
    elif x <= 0:
        return 'N'

numero = int(input("Digite um número: "))

print(classifica_numero(numero))