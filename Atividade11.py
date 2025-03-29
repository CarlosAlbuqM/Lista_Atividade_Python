"""Crie uma função que receba uma lista de números e retorne a média."""

def calculo_media(x):
    media = (sum(x) / len(x))
    return media

lista_numeros = []
while True:
    numero = float(input("Digite um número ou '0' para sair: "))
    if numero != 0:
        lista_numeros.append(numero)
    else:
        break

print(f"{calculo_media(lista_numeros)}")