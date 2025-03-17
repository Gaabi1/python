
#Em uma variável do tipo str, é possível armazenar letras, números, espaços, pontuação e diversos símbolos.
#Diferentemente da linguagem C, não existe o tipo char. Cada caractere em Python é uma string.

#Delimitando strings
#Em Python, strings podem ser delimitadas por aspas simples ('), aspas duplas ("), ou aspas triplas (''' ou """).
s1= 'Python'
print(s1)
s2= "é"
print(s2)
s3= '''uma '''
print(s3)
s4= """linguagem de programação"""
print(s4)
print(s1, s2, s3, s4)

#Criando uma string 
texto= "Olá, mundo!"

#Acessando um caractere individual da string
primeiro_caractere= texto[0]
ultimo_caractere= texto[-1]
print(f"O primeiro caractere é: {primeiro_caractere}")
print(f"O segundo caractere é: {ultimo_caractere}")

#Fatiando a string
sub_texto= texto[5:10]
print(f"Subtexto (indice 5 a 9): {sub_texto}")

#Concatenando strings
saudacao= "Olá"
nome= "Gabi"
frase= saudacao+ ", "+ nome+ "!"
print(f"Frase concatenada : {frase}")

#Dividindo uma string em uma lista
lista_palavras= texto.split()
print(f"Lista de palavras: {lista_palavras}")

#Substituindo parte de uma string
texto_modificado= texto.replace("Mundo", "Python")
print(f"Texto modificado: {texto_modificado}")

#Convertendo uma string para maiúsculas e minúsculas
texto_maiusculo= texto.upper()
texto_minusculo= texto.lower()
print(f"Texto em maiúsculas: {texto_maiusculo}")
print(f"Texto em minúsculas: {texto_minusculo}")

#Removendo espaços em branco do início e do final de uma string (trim)
texto_com_espacos= "  Olá, mundo!  "
texto_sem_espacos= texto_com_espacos.strip()
print(f"Texto sem espaços em branco: {texto_sem_espacos}")

#Verificando a presença de uma substring em uma string
if "mundo" in texto:
    print("A substring 'mundo' está presente na string.")
else:
    print("A substring 'mundo' não está presente na string.")

#Formatando strings
idade= 22
cidade= "Barreiras"
nome= "Gabi"
texto_formatado= f"Meu nome é {nome}, tenho {idade} anos e moro em {cidade}."
print(f"Texto formatado: {texto_formatado}")
#O método format() também pode ser usado para formatar strings
texto_formatado2= "Meu nome é {}, tenho {} anos e moro em {}.".format(nome, idade, cidade)
print(f"Texto formatado 2: {texto_formatado2}")

#Verificando o tamanho de uma string
tamanho= len(texto)
print(f"Tamanho da string: {tamanho}")






