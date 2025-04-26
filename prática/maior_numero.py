#Escreva uma função que busca de forma iterativa o maior elemento em uma lista de números inteiros.

def maior_numero(lista):

    #Se a lista tiver um elemento 
    if len(lista)<=1:
        return lista[0]
    
    maior_elemento= lista[0]
    #começando do índice 1 até o final. Ou seja, pula o primeiro elemento (índice 0).
    for numero in lista[1:]:
        if numero> maior_elemento:
            maior_elemento=numero
    return maior_elemento

lista= input("Entre com os números: ")
maior_elemento= maior_numero(lista)
print(f"O maior número é: {maior_elemento}")

