from gerarId import gerar
from salvarDados import salvarCadastro
from lerDados import consultarCadastro
from models import endereco

class Usuario:
  def __init__(self):
    self.idUser = gerar('database/usuarios.txt')
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
    salvarCadastro(self.idUser, typeuser, self.username, self.cpf, self.telefone, self.email, self.senha)
  
  def logar(self, email, senha):
    return consultarCadastro(email, senha)

  def alterarDados(self):
    print("Tô com preguiça de mudar os teus dados!")

class Cliente(Usuario):
  def __init__(self):
    Usuario.__init__(self)
    self.endereco = endereco.Endereco()
    self.intoleranciaGluten = None
    self.intoleranciaLactose = None
  def efetuarPedido(self):
    print("Pode pedir cara de osga!")
  def confirmarPedido(self, status):
    print("É isso que tu quer mermo filhote de peixe boi?")
  def informarDadosPagamento(self, pagamento):
    print("Forma de pagamento ok")
  def intolerante(self):
    self.intoleranciaGluten = False
    self.intoleranciaLactose = False

class Funcionario(Usuario):
  def __init__(self):
    Usuario.__init__(self)
    self.registro = None
    self.funcao = None
    self.cargaHoraria = None
    self.periodoEmpregado = None
  def cadastrarCardapio(self):
    print("Cardápio")
  def excluirCardapio(self):
    print("Sem cardápio")
  def emitirRelatorioGerencial(self):
    print("Está acontecendo isso...")
  def atualizarEstoque(self):
    print("Estoque")
  def consultarCompra(self):
    print("Compras")
  def alterarStatusCompra(self):
    print("Status")