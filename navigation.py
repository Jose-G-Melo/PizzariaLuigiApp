# Aqui que as funcionalidades se unem e formam o sistema

# importando as telas e os controles de cada parte do sistema e o módulo do sistema
from controller import controlHome, controlRegister, controlLogin
from views import windowHome, windowRegister, windowLogin
import os

# controla a aplicação por inteira
def navigation():
  windowHome.window()
  controle = controlHome.main()
  if(controle == 1):
    os.system("cls" if os.name == "nt" else "clear")
    windowLogin.window()
    controlLogin.conectar()
  elif(controle == 2):
    os.system("cls" if os.name == "nt" else "clear")
    windowRegister.window()
    controlRegister.cadastro()
  else:
    print("Até mais")
  