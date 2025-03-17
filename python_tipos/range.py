
#Representa uma sequência imutável de números e frequentemente é usado em loops de um número específico de vezes, como o for.

#Varrendo uma sequência de números
for i in range(5):#vai de 0 a 4
    print(i)

#Varrendo uma sequência de números com início e fim específicos
for item in range(20, 25):#vai de 20 a 24
    print(item)

#Varrendo uma sequência de números com início, fim e incremento específicos
for numero in range(0, 10, 2):#vai de 0 a 8, pulando de 2 em 2
    print(numero)

#Convertendo um range em uma lista
lista= list(range(5))
print(lista)

#Convertendo um range em uma lista e especificando o incremento
lista2= list(range(0, 10, 2))
print(lista2)
