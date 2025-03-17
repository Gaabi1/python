#Permitem que itens de uma sequência recebam índices definidos pelo usuário. Um dicionário contém pares de (chave, valor).

#Criando um dicionário
dicionario= {"nome":"Gabi", "idade": 22, "cidade": "Barreiras"}

#Acessando e imprimindo valores individuais usando chaves
nome= dicionario["nome"]
idade= dicionario["idade"]
cidade= dicionario["cidade"]
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")

#Adicionando um novo par chave-valor ao dicionário
dicionario["profissao"]= "Engenheira"
print(f"Dicionário após adicionar profissão: {dicionario}") 

#Modificando um valor associado a uma chave
dicionario["cidade"]= "Salvador"
print(f"Dicionário após modificar cidade: {dicionario}")

#Removendo um par chave-valor do dicionário
del dicionario["idade"]
print(f"Dicionário após remover idade: {dicionario}")

#Acessando todas as chaves e valores do dicionário
chaves= dicionario.keys()
valores= dicionario.values()
print(f"Chaves: {list(chaves)}")
print(f"Valores: {list(valores)}")

#Iterando sobre os pares chave-valor do dicionário
print("Iterando sobre o dicionário:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

#Verificando se uma chave está presente no dicionário
if "cidade" in dicionario:
    print("A chave 'cidade' está presente no dicionário.")
else:
    print("A chave 'cidade' não está presente no dicionário.")

#Usando o método get para acessar um valor associado a uma chave
profissao= dicionario.get("profissao", "Não informada") #Caso não tenha valor ele retorna não informada
print(f"Profissão: {profissao}")

#Limpando o dicionário
dicionario.clear()
print(f"Dicionário após limpeza:{dicionario}")

