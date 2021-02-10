def main():
  while(True):
    try:
      opcao = int(input("Escolha uma opção:\n<<1>> Logar\n<<2>> cadastrar\n<<3>> Sair\nRESPOSTA: "))
      if(opcao > 3):
        print("\nOpção inválida, tente novamente!\n")
        continue
      break
      return opcao
    except ValueError:
      print("\nTivemos um problema com o tipo de dado informado, tente\nnovamente! OBS: informe um dos números inteiros informados\npara cada opção\n")
      continue
  
