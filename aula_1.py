import math

#Inteiros (int)
# var1 = 150
# var2 = 227

# var3 = var1 + var2
# print(var3)
# #
# print(var3 * 3)

# #Ponto Flutuante ou Reais (float)
# var4 = var3 / 2.7
# print(var4)
# var5 = round(var4, 2)

# print("Ceil:", math.ceil(var4))
# print("Floor:", math.floor(var4))
# print(var5)

# #Sequências (String)
# st = 'meu amor'
# print(st)
# # começa a contagem de 0

# tamanho = len(st)
# print(tamanho)
# print(st[4])
# print(st[0:4])
# print(st[3:4])
# print(st[len(st) - 1])
# print(st[-1])

# print('--------------------')

# concatenacao = 'te ' + 'amo'
# mais_texto = 'muito!'
# interpolacao = f'{concatenacao}, {mais_texto} kansdlkansdlkasnd '
# print(concatenacao)
# print(interpolacao)

# st1 = '235a'
# st2 = '3'

# print(st1 + st2)	# concatenção != soma
# print(int(st1[0:3]) + float(st2))	# soma numérica
# print(st1*5)
# print(int(st1[0:3])*5)

# print('--------------------')

hora = 14
minutos = 53
dia = 26
mes = 10
ano = 2023

saida = str(dia) + '/' + str(mes) + '/' + str(ano) + ' ' + str(hora) + ':' + str(minutos)
saida = f'{dia}/{mes}/{ano} {hora}:{minutos}'

print(type(hora))
print(saida)
print(type(saida))

# CHAGAMOS ATE AKI!


'''
nova_st = """fdsf
sfds
dfsfjks
fdskf
"""
# docstring
# print (nova_st)

hms1 = '21:37:45.7'
hms2 = '20:55:33.35'
#
hora1 = hms1[0:2]
hora2 = hms2[0:2]
#
seg1 = hms1[6:]
seg2 = hms2[6:]
#
print (hora1,seg1)
print (hora2,seg2)
#
quebra1 = hms1.split(':')
quebra2 = hms2.split(':')
#
print (quebra1)
print (quebra2)

lista1 = ['lucas',25,[],[1,2,3,['a','b','c']]]
print (len(lista1))
print (lista1[0])
print (lista1[1])
print (lista1[3][2])

#Lógicas (Boolean)

#Listas (list)

#Tuplas (tuple)

#Dicionários (dict)



#Complexos (complex)
'''