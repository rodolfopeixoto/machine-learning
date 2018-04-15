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
misterioso = [1, 1, 1]
misterioso2 = [0, 0, 1]

teste = [misterioso, misterioso2]

modelo = MultinomialNB()
encaixar = modelo.fit(dados, marcacoes) # adequar - encaixar
preveja = modelo.predict(teste)
print preveja
# print(modelo.predict(misterioso)) # preveja

