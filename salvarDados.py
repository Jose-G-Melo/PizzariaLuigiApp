def salvarCadastro(ID, typeuser, username, cpf, telefone, email, senha, dadosComplemento):
  try:
    user = open("database/usuarios.txt", "a", encoding="UTF-8")
    if(len(dadosComplemento) == 4):
      dataUser = (f'"id": "{ID}", "typeuser": "{typeuser}", "username": "{username}", "cpf": "{cpf}", "phone": "{telefone}", "email": "{email}", "senha": "{senha}", "registro": "{dadosComplemento["registro"]}", "funcao": "{dadosComplemento["funcao"]}", "periodo_empregado": "{dadosComplemento["periodo"]}", "carga_horaria": "{dadosComplemento["carga"]}"')
    elif(len(dadosComplemento) == 3):
      dataUser = (f'"id": "{ID}", "typeuser": "{typeuser}", "username": "{username}", "cpf": "{cpf}", "phone": "{telefone}", "email": "{email}", "senha": "{senha}", "registro": "{dadosComplemento["registro"]}", "funcao": "{dadosComplemento["funcao"]}", "periodo_empregado": "{dadosComplemento["periodo"]}", "carga_horaria": "{dadosComplemento["carga"]}"')
    jsonUser = ("{", dataUser, "}", "\n")
    user.write(' '.join(jsonUser))
  except FileNotFoundError:
    print("Erro ao tentar abrir o banco de dados!")