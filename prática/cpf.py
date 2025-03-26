#Criar uma função que valida um CPF.

def validar_cpf (cpf):
    
    #Removendo caracteres não núméricos
    #str.isdigit é um método que retorna True se o caractere for um número e False caso contrário.
    #A função filter() percorre cada caractere da string cpf e mantém apenas aqueles que são dígitos 
    #''.join(...) junta todos os caracteres filtrados em uma única string, sem espaços ou
    cpf=''.join(filter(str.isdigit, cpf))

    #Verificando se o cpf possui 11 digitos
    if len(cpf)!=11:
        return False
    
    #Verificando se todos os digitos são iguais
    if cpf==cpf[0]*11:
        return False
    
    #Calculando o primeiro digito verificador
    soma= sum(int(cpf[i])* (10 - i) for i in range(9))
    resto= soma % 11
    if resto < 2: 
        digito_verificador1 =0
    else:
        digito_verificador1= 11- resto
    
    #Verificar o primeiro digito verificado
    if cpf[9]!= digito_verificador1:
        return False
    
    #O CPF tem 11 dígitos, sendo que os dois últimos são os dígitos verificadores.
    #Calculando o segundo digito verificador
    soma= sum(int(cpf[i])* (11 - i) for i in range(10))
    resto= soma % 11
    if resto < 2: 
        digito_verificador2 =0
    else:
        digito_verificador2= 11- resto
    
    #Verificar o primeiro digito verificado
    if cpf[10]!= digito_verificador2:
        return False
    
    return True

#Testando a função
cpf=input("Digite o cpf: ")
if validar_cpf(cpf):
    print(f"O cpf {cpf} é válido")
else:
    print(f"O cpf {cpf} é invalido.")



    




