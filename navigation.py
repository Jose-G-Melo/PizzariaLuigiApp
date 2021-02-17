from controller import controlHome
from views import windowHome, windowRegister
import os

def navigation():
  windowHome.window()
  controle = controlHome.main()
  if(controle == 1):
    print("Login")
  elif(controle == 2):
    os.system("cls" if os.name == "nt" else "clear")
    windowRegister.window()
  else:
    print("Até mais")
  