#Dicionários
dic = {"NOME": "Pierre", "IDADE": 22, "CIDADE": "Canapi"}
print(dic)
print(dic["CIDADE"])
dic["NOME"] = "Kawane"
print(dic.values())
print(dic.keys())
dic2 = {"NOME": "Filipe", "IDADE": 22, "CIDADE": "Canindé"}

for d in dic.values():
    print(d)

lista = []
lista.append(dic)
lista.append(dic2)
print(lista)
