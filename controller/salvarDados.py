def salvarCadastro(ID, typeuser, username, cpf, telefone, email, senha):
    user = open("database/usuarios.txt", "a", encoding="UTF-8")
    dataUser = (f'"id": "{ID}", "typeuser": "{typeuser}", "username": "{username}", "cpf": "{cpf}", "phone": "{telefone}", "email": "{email}", "senha": "{senha}"')
    jsonUser = ("{", dataUser, "}", "\n")
    user.write(' '.join(jsonUser))