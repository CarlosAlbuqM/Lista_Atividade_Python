""" Escreva uma função que receba um número e retorne True se ele for primeiro e falso caso contrário """

def numero_primo(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


numero = int(input("Digite um número: "))

print(f"{numero_primo(numero)}")