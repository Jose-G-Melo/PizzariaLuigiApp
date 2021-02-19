from models import user

def cadastro():
  nome = input("Nome: ")
  cpf = input("CPF: ")
  telefone = input("Telefone: ")
  email = input("E-mail: ")
  senha = None
  while(True):
    senha = input("Senha: ")
    repeatSenha = input("Corfirme a senha: ")
    if(senha == repeatSenha):
      break
    else:
      print("\nAs senhas são diferentes, tente novamente!\n")
      
  while(True):
    try:
      tipo_usuario = int(input("Tipo de usuário:\n<<1>> Funcionário\n<<2>> Cliente\n1 ou 2: "))
      break
    except ValueError:
      print("\nTivemos um problema com o tipo de dado informado, tente\nnovamente! OBS: informe um dos números inteiros informados\npara cada opção\n")
      continue

  if(tipo_usuario == 1):
    registro = int(input("Número de registro: "))
    funcao = input("Função: ")
    entra = input("Horário que entra no trabalho: ")
    sai = input("Horário que sai do trabalho: ")
    anoContratacao = int(input("Ano que foi contratado: "))
    mesContratacao = int(input("Mês que foi contratado: "))
    diaContratacao = int(input("Dia que foi contratado: "))
    funcionario = user.Funcionario()
    funcionario.cadastroFunc(tipo_usuario, nome, cpf, telefone, email,senha, registro, funcao, entra, sai, anoContratacao, mesContratacao, diaContratacao)
  
  elif(tipo_usuario == 2):
    print("Informe o CEP e o número da sua residência para cadastrarmos o seu endereço!\n")
    while(True):
      try:
        cep = input("CEP: ").isnumeric()
        numero = input("Número da casa: ").isnumeric()
        break
      except:
        print("Você informou um tipo de dado errado, tente novamente!")
        continue
    cliente = user.Cliente()
    print(type(cliente.intolerante()))
    print(cliente.intolerante())
    exit()
    cliente.cadastroClient(tipo_usuario, nome, cpf, telefone, email,senha, cep, numero, "intoleranteGluten", "intoleranteLactose")
