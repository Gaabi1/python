#Uma função recursiva é aquela que chama a si mesma.
#Função regressiva que chama sí própria
def regressiva(x):
    print (x)
    if x<0:
        print(x-1)
    else:
        print("Acabou")
regressiva(10)

#Não recursiva
#range(start, stop, step)
for y in range (10, -1, -1):
    print(y)

#Função recursiva fatorial
def fatorial(n):
    if n==1 or n==0:
        return 1
    else:
        #chama a si mesma.
        return n*fatorial(n-1)
vfat= fatorial(5)

print(f"Resultado recursiva: {vfat}")

#Função fatorial não recursiva 
def fatorial (n):
    fat=1
    if n==1 or n==0:
        return fat
    else:
        for x in range(2, (n+1)):
            fat= fat*x
            return fat
vfat= fatorial(5)
print(f"Resultado iterativa: {vfat}")                           
