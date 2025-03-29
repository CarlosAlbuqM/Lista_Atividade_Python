"""Função autenticação usuário  """

def autenticador_usuario(x, y):
    usuarios = [ 
        {
            'username': 'teste',
            'password': 'admin'
        },

        {
            'username': 'teste2',
            'password': 'admin2'
        },

        {
           'username': 'teste3',
           'password': 'admin3' 
        },

        {
            'username': 'teste4',
            'password': 'admin4'
        },

    ]

    for usuario in usuarios:
        if x == usuario['username'] and y == usuario['password']:
            return 'Usuário Logado'
    return 'Erro de login, tente novamente.'