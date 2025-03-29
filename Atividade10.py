"""Crie uma função que receba uma string e retorne o número de palavras na string."""

def numero_palavras(x):
    y = x.split()
    return len(y)

palavra = input("Digite uma palavra: ")

print(numero_palavras(palavra))