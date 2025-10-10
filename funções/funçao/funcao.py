def calcula_imc(peso, altura):
    imc = peso*100 / altura ** 2 #pes0 multiplica por 100 pra não ter problema com ponto flutuante
    return imc #retorna o valor do imc

peso=eval(input("Digite o peso: "))
altura=eval(input("Digite a altura: "))
calcula_imc(peso, altura) #chamada da função
imc=calcula_imc(peso, altura) #atribuição do valor do imc a variável imc
print("Seu IMC é: ", imc) #imprime o valor do imc


#Exemplo 2
def taximetro(distancia, multiplicador): #valor def se não for passado ele assumi que é 1
    largada=3
    km=2
    valor(largada + distancia * km) * multiplicador
    return valor

pagamento=taximetro(3.5)#passa a distancia e o multiplicador 
print("Valor a ser pago: ", pagamento)

#Exemplo 3



    