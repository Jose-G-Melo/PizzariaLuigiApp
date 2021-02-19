#controla a entrada de dados (escolha) do usuário na tela inicial
def main():
  while(True):
    try:
      # entra a escolha
      opcao = int(input("Escolha uma opção:\n<<1>> Logar\n<<2>> cadastrar\n<<3>> Sair\nRESPOSTA: "))
      if(opcao > 3):
        print("\nOpção inválida, tente novamente!\n")
        continue
      # retorna a escolha feita
      return opcao
      break
    except ValueError:
      print("\nTivemos um problema com o tipo de dado informado, tente\nnovamente! OBS: informe um dos números inteiros informados\npara cada opção\n")
      continue
  
