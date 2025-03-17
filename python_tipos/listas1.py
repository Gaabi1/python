#Listas são sequências mutáveis, normalmente usadas para armazenar coleções de itens homogêneos. 

#Criando uma lista
lista= [10, 20, 30, 40, 50]

#Acesso elemento individual da lista
primeiro_elemento= lista[0]
segundo_elemento= lista[1]
#imprimindo elementos
print(f"O primeiro elemento é :{primeiro_elemento}")
print(f"O segundo elemento é: {segundo_elemento}")

#Adicionando um elemento ao final da lista
lista.append(60)
print(f"Lista apos adicionar 60: {lista}")

#Inserindo elemento em uma posição específica
lista.insert(1, 15)
print(f"Lista apos inserir 15 na posição 1: {lista}")#inserindo 15 na posição 1

#Removendo um elemento da lista
lista.remove(15)
print(f"Lista apos remover 15: {lista}")

#Removento o ultimo elemento da lista
lista.pop()
ultimo_elemento= lista.pop()
print(f"Lista apos remover o ultimo elemento: {lista}")
print(f"O ultimo elemento removido foi: {ultimo_elemento}")

#Acessando um subgrupo da lista (fatiamento)
sub_lista= lista[1:4] #acessando os elementos da posição 1 a 3
print(f"Sublista (elementos de indice 1 e 3) : {sub_lista}")

#Ordenado a lista (caso ela esteja desordenada)
lista2=[100, 70, 60, 80, 90]
lista2.sort()
print(f"Lista ordenada: {lista2}")

#Interando sobre os elementos da lista
print("Interando sobre a lista:")
for elemento in lista:
    print(elemento)


 
