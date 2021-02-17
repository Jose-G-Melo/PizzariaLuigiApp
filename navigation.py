from controller import controlHome
from views import windowHome, windowRegister

def navigation():
  windowHome.window()
  controle = controlHome.main()
  if(controle == 1):
    print("Login")
  elif(controle == 2):
    windowRegister.window()
  else:
    print("Até mais")
  