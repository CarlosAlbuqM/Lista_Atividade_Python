"""Escreva uma função que calcule o fatorial de um número inteiro não-negativo."""

def factorial(x):
    import math
    return math.factorial(x)

numero = int(input("Digite um número: "))
print(f"{factorial(numero)}")