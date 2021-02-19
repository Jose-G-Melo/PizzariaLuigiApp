# importando módulo padrão para trabalhar com json
import json

# consulta no "banco de dados" se o usuário está cadastrado no sistema
def consultarCadastro(email, senha):
  user = open("database/usuarios.txt", "r", encoding="UTF-8")
  for pessoa in user:
    usuario = json.loads(pessoa)
    email_pessoa = usuario["email"]
    senha_pessoa = usuario["senha"]
    if(email == email_pessoa):
      if(senha == senha_pessoa):
        return usuario["typeuser"]
      else:
        return "erro na senha"
    else:
      return "erro no email"