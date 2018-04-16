# -*- coding: utf-8 -*-
# é gordinho? tem perninha curta? se faz au au?

from sklearn.naive_bayes import MultinomialNB

porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
marcacoes = [1, 1 , 1, -1, -1, -1]

modelo = MultinomialNB()
encaixar = modelo.fit(dados, marcacoes) # adequar - encaixar


misterioso = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [1, 0, 1]

testes = [misterioso, misterioso2, misterioso3]


marcacoes_teste = [ -1, 1 , 1  ]

resultado = modelo.predict(testes)
print resultado
# print(modelo.predict(misterioso)) # preveja



diferencas = resultado - marcacoes_teste # Se acertou imprime 0 se não qualquer outro valor

print(diferencas)

total_de_erros = [erro for erro in diferencas if erro != 0]

print(total_de_erros)
acertos = [ diferenca for diferenca in diferencas if diferenca == 0 ]
total_de_acertos = len(acertos)
total_de_elementos = len(testes)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print(taxa_de_acerto)

#http://bit.ly/alura_analise_entrada