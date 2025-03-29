""" Autenticação Usuário """

import Atividade5_controlador_usuario

usuario = input("Digite o nome de usuário: ")
senha = input("Digite sua senha: ")

print(f"{Atividade5_controlador_usuario.autenticador_usuario(usuario, senha)}")

