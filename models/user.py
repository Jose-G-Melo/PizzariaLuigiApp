# importando os módulos de geração de id, de manipulação do "banco de dados", módulo padrão para trabalho com datas e horários, além do modelo de endereço
from gerarId import gerar
from salvarDados import salvarCadastro
from lerDados import consultarCadastro
from models import endereco
import datetime

# armazena a data atual que nos ajudará nos calculos de datas
data = datetime.datetime.now()
dataAtual = datetime.date(data.year, data.month, data.day)

# modelo (forma) de usuário no sistema, com atributos e métodos
# superclasse
class Usuario:
  def __init__(self):
    self.idUser = gerar('database/usuarios.txt')
    self.username = None
    self.cpf = None
    self.telefone = None
    self.email = None
    self.senha = None

  def cadastrar(self, typeuser, username, cpf, telefone, email, senha, dadosComplementares = {}):
    self.username = username
    self.cpf = cpf
    self.telefone = telefone
    self.email = email
    self.senha = senha
    salvarCadastro(self.idUser, typeuser, self.username, self.cpf, self.telefone, self.email, self.senha, dadosComplementares)
  
  def logar(self, email, senha):
    return consultarCadastro(email, senha)

  def alterarDados(self):
    print("Tô com preguiça de mudar os teus dados!")

# modelo (forma) de cliente no sistema, com atributos e métodos
# subclasse
class Cliente(Usuario):
  def __init__(self):
    Usuario.__init__(self)
    self.endereco = endereco.Endereco()
    self.intoleranciaGluten = None
    self.intoleranciaLactose = None
  
  def cadastroClient(self, typeuser, username, cpf, telefone, email, senha, registro, funcao, entra, sai, ano, mes, dia):
    self.registro = registro
    self.funcao = funcao

    dataContrato = datetime.date(ano, mes, dia)
    self.periodoEmpregado = int((dataAtual - dataContrato).days/365.25)

    segundos = (datetime.datetime.strptime(sai, "%H:%M") - datetime.datetime.strptime(entra, "%H:%M")).total_seconds()
    horas = segundos // 3600
    segs_restantes = segundos % 3600
    minutos = segs_restantes // 60
    self.cargaHoraria = datetime.time(int(horas), int(minutos)).strftime("%H:%M")
    
    self.cadastrar(typeuser, username, cpf, telefone, email, senha, {"registro": self.registro, "funcao": self.funcao, "periodo": self.periodoEmpregado, "carga": self.cargaHoraria})
  def efetuarPedido(self):
    print("Pode pedir cara de osga!")
  def confirmarPedido(self, status):
    print("É isso que tu quer mermo filhote de peixe boi?")
  def informarDadosPagamento(self, pagamento):
    print("Forma de pagamento ok")
  def intolerante(self):
    intolerante = None
    while(intolerante != "Y" or intolerante != "N"):
      intolerante = str(input("Tem alguma intolerância? (Y/N) ")).upper()
      if(intolerante == "Y"):
        intolerante = str(input("Tem intolerância a lactose? (Y/N) ")).upper()
        if(intolerante == "Y"):
          self.intoleranciaLactose = True
          intolerante = str(input("Tem intolerância a glúten? (Y/N) ")).upper()
          if(intolerante == "Y"):
            self.intoleranciaGluten = True
            break
          if(intolerante == "N"):
            self.intoleranciaGluten = False
            break
        if(intolerante == "N"):
          self.intoleranciaLactose = False
          intolerante = str(input("Tem intolerância a glúten? (Y/N) ")).upper()
          if(intolerante == "Y"):
            self.intoleranciaGluten = True
            break
          if(intolerante == "N"):
            self.intoleranciaGluten = False
      if(intolerante == "N"):
        self.intoleranciaLactose = False
        self.intoleranciaGluten = False
        break
    return self.intoleranciaGluten, self.intoleranciaLactose

# modelo (forma) de funcionário no sistema, com atributos e métodos
# subclasse
class Funcionario(Usuario):
  def __init__(self):
    Usuario.__init__(self)
    self.registro = None
    self.funcao = None
    self.cargaHoraria = None
    self.periodoEmpregado = None
  def cadastroFunc(self, typeuser, username, cpf, telefone, email, senha, registro, funcao, entra, sai, ano, mes, dia):
    self.registro = registro
    self.funcao = funcao

    dataContrato = datetime.date(ano, mes, dia)
    self.periodoEmpregado = int((dataAtual - dataContrato).days/365.25)

    segundos = (datetime.datetime.strptime(sai, "%H:%M") - datetime.datetime.strptime(entra, "%H:%M")).total_seconds()
    horas = segundos // 3600
    segs_restantes = segundos % 3600
    minutos = segs_restantes // 60
    self.cargaHoraria = datetime.time(int(horas), int(minutos)).strftime("%H:%M")
    
    self.cadastrar(typeuser, username, cpf, telefone, email, senha, {"registro": self.registro, "funcao": self.funcao, "periodo": self.periodoEmpregado, "carga": self.cargaHoraria})

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