#Escreva um programa que calcule o faturamento de um representante comercial que recebe 
#R$ 900,00 fixos e 6% de comissão sobre as vendas do mês. 
#Considere que ele fechou o mês com um valor de R$ 15.295,00 em vendas. 

while True:
    try:
        vendas= float(input("Digite o valor de vendas, apenas o número: "))
        break
    except ValueError:
        print("Valor invalido digite um número valido. Tente novamente ")

valor= vendas * 0.06

salario= valor + 900

print(f"O funcionário vai receber: R${salario:.2f}")