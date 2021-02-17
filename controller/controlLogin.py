from models import user

def conectar():
  email = input("E-mail: ")
  senha = input("Senha: ")
  
  usuario = user.Usuario()
  login = usuario.logar(email, senha)
  print(login)