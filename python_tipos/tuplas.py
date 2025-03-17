
#Tuplas são sequências imutáveis, tipicamente usadas para armazenar coleções de itens heterogêneos.

#Criando uma tupla
tupla_heterogenea= (10, "Python", 3.14, [1, 2, 3], True, {"chave": "valor"})

#Acessando elementos individuais da tupla
print(f'Inteiro: {tupla_heterogenea[0]}')
print(f'String: {tupla_heterogenea[1]}')
print(f'Float: {tupla_heterogenea[2]}')
print(f'Lista: {tupla_heterogenea[3]}')
print(f'Booleano: {tupla_heterogenea[4]}')
print(f'Dicionário: {tupla_heterogenea[5]}')

#Modifificando a lista dentro da tupla
tupla_heterogenea[3].append(40)
print(f'Tupla após modificar a lista: {tupla_heterogenea[3]}')

#Acessando um valor do dicionário dentro da tupla
valor_dict= tupla_heterogenea[5]["chave"]
print(f'Valor do dicionário: {valor_dict}')

#Interando sobre a tupla
print("Iterando sobre a tupla:")
for item in tupla_heterogenea:
    print(f"Item: {item}, Tipo: {type(item)}")

#Tuplas são imutáveis, então não é possível adicionar, remover ou modificar elementos após a criação da tupla.
# tupla_heterogenea[0]= 20 #Erro: tuplas são imutáveis
