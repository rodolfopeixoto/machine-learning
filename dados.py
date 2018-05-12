import csv

def carregar_acessos():

    arquivo   = abrir_arquivo()
    leitor    = leia_arquivo(arquivo)
    leitor.next()
    dados, marcacoes = carregar_buscas(leitor)
    fechar_arquivo(arquivo)

    return dados, marcacoes

def abrir_arquivo():
    return open('arquivo.csv', 'rb')

def fechar_arquivo(arquivo_path):
    arquivo_path.close

def leia_arquivo(arquivo):
    return csv.reader(arquivo)

def carregar_buscas(leitor):
    dados = []
    marcacoes = []
    for home, como_funciona, contato, comprou in leitor:
        dados.append([int(home), int(como_funciona), int(contato)])
        marcacoes.append(int(comprou))
    return dados, marcacoes
