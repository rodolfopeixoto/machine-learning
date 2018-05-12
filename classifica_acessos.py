# minha abordagem inicial foi
# 1. separar 90% para treino e 10% para teste: 88.89%
from dados import carregar_acessos

X,Y = carregar_acessos()

treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)
print("resultado: ", resultado)
print("teste_marcacoes: ", teste_marcacoes)
diferencas = resultado - teste_marcacoes
print("diferencas: ", diferencas)


acertos = [diferenca for diferenca in diferencas if (diferenca == 0).any()]

total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxas_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print("Acertos: ", acertos)
print("Total de acertos: ",total_de_acertos)
print("Total de Elementos: ",total_de_elementos)
print("TAXA DE ACERTOS: ",taxas_de_acerto)