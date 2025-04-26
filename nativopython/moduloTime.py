#modulo time

import time
#retorna o número de segundos desde a "época" (1º de janeiro de 1970, também conhecido como "Unix epoch")
print(time.time()) 

#converte o valor retornado por time.time() em uma estrutura de tempo local (ano, mês, dia, etc.).
print(time.localtime())

# armazena o valor atual do tempo em segundos
x= time.time()

#time.ctime(x) converte o valor de x em uma string legível que representa a data e hora local.
print(f'Time local: {time.ctime(x)}') 