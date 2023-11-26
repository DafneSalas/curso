numeros = [10,20,30,40,50,60,70]
# print(list_1)
# print(list_1 * 5)
print(len(numeros))

tamanho = len(numeros)
print(tamanho)

#indentacao --- aniha os comandos -- py é obrigatório
# for numero in numeros:
#     resultado = numero * 5
#     print(resultado)

# for indice in range(0, 50, 2):
#     # resultado = numero * 5
#     print(indice, end=' -  ')

# range 
# para um valor -- comeca em zero e termina no ultimo valor -1
# 02 valore -- primeiro valor é o comeco e o segundo é o final
# for posicao in range(12):
#   print(posicao)

# for posicao in range(3, 12):
#     print(posicao, end=' - ')

for posicao in range(len(numeros)):
    print(posicao)

#indentacao --- aniha os comandos -- py é obrigatório
list_1 = [10, 20, 30]
lista_2 = [100, 200, 300]

for indice in range(len(list_1)):
    valor_1 = list_1[indice]
    valor_2 = lista_2[indice]
    soma = valor_1 + valor_2
    print(f'{valor_1} + {valor_2} = {soma}')

for pos_valor in enumerate (lista_saida):
    print(pos_valor)

lista = [a * 10 for a in range (10)]
#????????
