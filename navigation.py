from controller import controlHome
from views import windowHome

def navigation():
  windowHome.window()
  controle = controlHome.main()
  if(controle == 1):
    print("Login")
  elif(controle == 2):
    print("Cadastro")
  else:
    print("Até mais")
  