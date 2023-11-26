# print('Ola mundo!')
# print(10)
# print('Dafne', '29', 'é muito linda', 42.42)

# soma = 4 + float('2.4')
# print(soma)

# print('Escola de Dados Alura!')

# nome = "dafne"
# sobrenome = "salas"
# print(nome, sobrenome)
# print('dafne', 'salas')

# nome = ("D", "A", "F", "N", "E")
# print(nome)
# print(type(nome)) >>>>> #tupla --- lista imutavel
# nome = 'D', 'A', 'F', 'N', 'E'
# print(nome)

#nome = 'D' + 'A' + 'F' + 'N' + 'E'
#print(nome)
# print('D', 'A', 'F', 'N', 'E')

# string_interpolada = f'{4}/setembro/{1994}'
# string_interpolada_2 = str(4) + '/setembro/' + str(1994)
# print(string_interpolada_2)
# print(string_interpolada)
# nascimento = (4, 'setembro', 1994)
# print(nascimento)
# print(4, 'setembro', 1994)

# from math import sqrt

# exerciciof = sqrt ((5 ** (10/5))) + (-8) * float('1.5')
# print(exerciciof)

# ano_atual = (2023)
# print(ano_atual)


# #Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”
# print('Olá, Dafne!')
# #Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
# nome = "DAFNE"
# idade = 29
# print(f'Olá {nome}, você tem {idade} anos.')

# #Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
# print('Olá Dafne, você tem 29 anos e mede 1.50 metros!')

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
# soma = 10 + 5
# print(soma)

# #Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
# numero_1 = 20
# numero_2 = 4
# numero_3 = 0
# numero_4 = 2
# soma = numero_1 + numero_2 + numero_3
# print(soma)

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
# subtracao = numero_1 - numero_2
# print(subtracao)

# #Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
# multi = numero_1 * numero_3
# print(multi)

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. 
#### Deixe claro que o valor do denominador não pode ser `0`<<<<<<<<
# if numero_3 > 0:
#     divisao = numero_1 / numero_3
#     print(divisao)
# else:
# #     print('Não existe divisão por zero!')
# divisao = int(numero_1 / numero_4)
# print(divisao)
# print(int(4.2))

# #crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
# operador = 2
# potencia = 3
# exponenciacao = operador ** potencia
# print(exponenciacao)

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores.
#### Deixe claro que o valor do denominador não pode ser `0`.
# divisao = numero_1 // numero_4
# print(divisao)

# #Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. 
# ####Deixe claro que o valor do denominador não pode ser `0`.
# resto_da_divisao = numero_3 % numero_2
# print(resto_da_divisao)

# ######Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
# aluno_a = 8
# aluno_b = 8
# aluno_c = 6
# media = int((8 + 8 + 6) / 3)
# print(media)

# lista_2 = list((aluno_a, aluno_b, aluno_c))
# print (lista_2)
# lista_aluno = [aluno_a, aluno_b, aluno_c]
# print(lista_aluno)


####Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
# media = ((5 * 1) + (12 * 2) + (20 * 3) + (15 * 4)) / (1 + 2 + 3 + 4)
# print(media)

#Crie uma variável chamada “`frase`” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
# frase = ('Oi Amor!')
# print(frase)

#Crie um código que solicite uma frase e depois imprima a frase na tela.
nome = input('qual seu nome? ')
print(f'Seu nome é {nome.upper()}')

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = input('oi')
print(f'Olá lindo, como está? Oi {frase.upper()}')

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = input('oi')
print(f'Olá lindo, como está? Oi {frase.lower()}')


# #Crie uma variável chamada “`frase`” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
# frase = '      Te amo muito    '.strip()
# print(frase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
# frase = '  TeAmoMuito'  .lower().strip()
# print(frase)

# string_espaco = '      Te amo muito  '.strip()
# string_minuscula = string_espaco.lower()
# print(string_minuscula)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “`e`” trocadas pela letra “`f`”.
# frase = ('Teamomuito')
# def troca(e, f, frase):
#     return frase.replace(quero_trocar, trocar_por)

# print(troca('a', 'b', 'abacate')) # bbbcbte


#crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “`a`” trocadas pela caractere  “`@`”.

#crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “`s`” trocadas pelo caractere  “`$`”.