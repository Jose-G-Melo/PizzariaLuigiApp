from pycep_correios import get_address_from_cep as cep

class Endereco:
  def __init__(self):
    self.cep = None
    self.logradouro = None
    self.bairro = None
    self.numero = None
    self.complemento = None
  def alterarEndereco(self):
    print("A gente roda a cidade inteira!")
  def adicionarEndereco(self, cep_cliente, numero):
    cep_user = cep(cep_cliente)
    self.cep = cep_user['cep']
    self.logradouro = cep_user['logradouro']
    self.bairro = cep_user['bairro']
    self.numero = numero
    self.complemento = cep_user['complemento']
  def excluirEndereco(self):
    print("Já eu excluo!")