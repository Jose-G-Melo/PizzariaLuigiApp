from controller import gerarId
from controller import salvarDados

class Usuario:
  def __init__(self):
    self.idUser = gerarId.gerar('database/usuarios.txt')
    self.username = None
    self.cpf = None
    self.telefone = None
    self.email = None
    self.senha = None

  def cadastrar(self, typeuser, username, cpf, telefone, email, senha):
    self.username = username
    self.cpf = cpf
    self.telefone = telefone
    self.email = email
    self.senha = senha
    salvarDados.salvarCadastro(self.idUser, typeuser, self.username, self.cpf, self.telefone, self.email, self.senha)