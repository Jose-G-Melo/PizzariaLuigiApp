from models import user

def cadastro():
  while(True):
    try:
      tipo_usuario = int(input("Tipo de usuário:\n<<1>> Funcionário\n<<2>> Cliente\n1 ou 2: "))
      break
    except ValueError:
      print("\nTivemos um problema com o tipo de dado informado, tente\nnovamente! OBS: informe um dos números inteiros informados\npara cada opção\n")
      continue
  
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

  usuario = user.Usuario()
  usuario.cadastrar(tipo_usuario, nome, cpf, telefone, email,senha)
