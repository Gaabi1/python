#velocidade acima de 100 km/h corresponde a uma 'Multa Grande'
#velocidade acima de 60 km/h e menor que 100 km/h corresponde a uma 'Multa Pequena'
#velocidade abaixo de 60 km/h corresponde a 'Sem Multa'.
while True :
    try:
        valor= int(input("Digite o valor da velocidade em km/h: "))
        break
    except ValueError:
        print("⚠️Digite um número válido!")

if valor >= 100 :
    print("Multa grande")
elif 60 > valor < 100 :
    print("Multa pequena")
else:
    print("Sem multa")


