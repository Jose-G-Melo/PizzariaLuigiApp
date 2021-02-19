# importando os modelos de usuários (funcionário e cliente)
from models import user

#responsável pelo controle do login do usuário
def conectar():
  # entra o email e a senha
  email = input("E-mail: ")
  senha = input("Senha: ")
  
  # faz o login
  usuario = user.Usuario()
  login = usuario.logar(email, senha)
  print(login)