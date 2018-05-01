import csv

def carregar_acessos():

  arquivo   = abrir_arquivo()
  leitor    = leia_arquivo(arquivo)
  marcacoes = agrupar_marcacoes(leitor)
  fechar_arquivo(arquivo)

  arquivo2   = abrir_arquivo()
  leitor2    = leia_arquivo(arquivo2)
  dados     = agrupar_dados(leitor2)
  fechar_arquivo(arquivo2)

  print("Dados: ", dados)
  print("Marcacoes: ", marcacoes)

def abrir_arquivo():
  return open('arquivo.csv', 'rb')

def fechar_arquivo(arquivo_path):
  arquivo_path.close

def leia_arquivo(arquivo):
  return csv.reader(arquivo)

def agrupar_dados(leitor):
  dados = []
  for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:
    dados.append([acessou_home, acessou_como_funciona, acessou_contato])
  return dados

def agrupar_marcacoes(leitor):
  
  marcacoes = []
  
  for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:
    marcacoes.append([comprou])
  return marcacoes

carregar_acessos()