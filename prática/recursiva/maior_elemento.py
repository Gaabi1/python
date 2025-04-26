#Escreva uma função que busca recursivamente o maior elemento em uma lista de números inteiros.

def maior_elemento(lista):

#Caso tenha apenas um elemento na lista
    if len(lista)==1:
        return lista[0]

    else:
        maior_resto= maior_elemento(lista[1:])
        return maior_resto if maior_resto>lista[0] else lista[0]
    
numero= input("Entre com a lista de números: ")
print(maior_elemento(numero))






