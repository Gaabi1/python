def mover_discos (origem, destino):
    disco= origem.pop()
    destino.append(disco)
    #numeros = [1, 2, 3, 4]
    #removido = numeros.pop()
    #print(numeros)  # Saída: [1, 2, 3]
    #print(removido)  # Saída: 4

def imprimir_torres (torreA,torreB, torreC):
    print("A", torreA)
    print("B", torreB)
    print("C", torreC)
    print()

def torre_hanoi_recursivo(num_disco, origem, destino, auxiliar):
    if num_disco==1:
        mover_discos(origem, destino)
        imprimir_torres(torreA, torreB, torreC)
    else:
        #Mover os n-1 discos de "origem" para "auxiliar", usando "destino" como auxiliar.
        torre_hanoi_recursivo(num_disco - 1, origem, auxiliar, destino)
    
        #Mover o maior disco diretamente da "origem" para "destino".
        mover_discos(origem, destino)
        imprimir_torres(torreA, torreB, torreC)
        
        #Mover os n-1 discos da "auxiliar" para "destino", usando "origem" como auxiliar.
        torre_hanoi_recursivo(num_disco - 1, auxiliar, destino, origem)
        
        

num_disco= 3

#Inicializando torres e discos
#range(num_disco, 0, -1) gera a sequência [3, 2, 1] (do maior para o menor).
#list(...) converte essa sequência para uma lista.
torreA= list(range(num_disco, 0, -1))
torreB= []
torreC=[]

#Exibindo estado inicial
imprimir_torres(torreA, torreB, torreC)
torre_hanoi_recursivo(num_disco, torreA, torreB, torreC)



