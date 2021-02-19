# importando módulo padrão para trabalhar com json
import json

# funcionalidade de gerar id
def gerar(file):
  try:
    db = open(file, "r", encoding="UTF-8")
    registros = []
    for registro in db:
      r = json.loads(registro)
      registros.append(r)
    id = len(registros)+1
    return id
  except FileNotFoundError:
    print("Erro no banco de dados!")