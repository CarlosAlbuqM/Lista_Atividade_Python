""""Crie uma função que receba uma string e retorne o número de vogais presentes na string."""

def contar_vogais(x):
    total = 0
    vogais = ['a','e','i','o','u']

    for letra in x:
        if letra.lower() in vogais:
            total +=1
    return total

palavra = str(input("Digite uma palavra: "))

print(f"{contar_vogais(palavra)}")