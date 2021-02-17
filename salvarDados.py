def salvarCadastro(ID, typeuser, username, cpf, telefone, email, senha):
  try:
    user = open("database/usuarios.txt", "a", encoding="UTF-8")
    dataUser = (f'"id": "{ID}", "typeuser": "{typeuser}", "username": "{username}", "cpf": "{cpf}", "phone": "{telefone}", "email": "{email}", "senha": "{senha}"')
    jsonUser = ("{", dataUser, "}", "\n")
    user.write(' '.join(jsonUser))
  except FileNotFoundError:
    print("Erro ao tentar abrir o banco de dados!")