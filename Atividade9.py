""" Crie uma função que receba uma lista de números e retorne a soma de todos os elementos da lista. """
def somar_lista(x):
    return sum(x)

lista = []
while True:
    numero = int(input("Digite um número ou '0' para sair: "))
    if numero != 0:
        lista.append(numero)
    else:
        break

print(f"{somar_lista(lista)}")