"""Crie uma função que receba um email e retorna se ele possui ‘@’
○ Desafio: Para aprimorar pesquise sobre regex e retorne se o e-mail é válido """
import re

def verificador_email(x):

    x = re.search(r"\w+@\w+\.\w+", x)
    if x == None:
        return False
    else:
        return True
    

email = input("Digite seu e-mail: \n >> ")

print(f"{verificador_email(email)}")