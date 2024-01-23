#ESTRUTURAS CONDICIONAIS == IF / ELSE
#if condicao:
    #instrucao que seja verdadeira
#else:
    #instrucao que seja falsa

# if 2 < 7:
#     print('condiçao verdadeira')
# if 3 > 7:
#     print('condiçao verdadeira') #por ser uma condicao falsa, nao executa o print

# idade_maria = int(input('Digite a idade da Maria: '))
# idade_beatriz = int(input('Digite a idade da Beatriz: '))
# if idade_maria > idade_beatriz:
#   print('Maria é mais velha que Beatriz.')

# idade_beatriz = 25
# idade_maria = 30
# if idade_maria > idade_beatriz:
#   print('Maria é mais velha que Beatriz.')

# empregados_empresa_1 = int(input('Digite a quantidade de empregados da empresa 1: '))
# empregados_empresa_2 = int(input('Digite a quantidade de empregados da empresa 2: '))
# if empregados_empresa_1 >= empregados_empresa_2:
#   print('Empresa 1 tem uma quantidade de empregados maior ou igual à empresa 2.')

# livro_1 = input('Digite o título do 1° livro: ')
# livro_2 = input('Digite o título do 2° livro: ')
# if livro_1 == livro_2:
#   print('Os livros têm o mesmo título')
# else:
#   print('Os livros têm títulos diferentes')


# media = float(input('Digite a média: '))
# if media >= 6.0:
#   print('Aprovado(a)')
# else:
#   print('Reprovado(a)')

# Agora a nossa instituição de ensino lançou uma nota oficial que pessoas que tenham média entre 4.0 e 6.0 podem fazer os 
# cursos de Recuperação nas férias para poder recuperar a nota.
# media = float(input('Digite a média: '))
# if media >= 6.0:
#   print('Aprovado(a)')
# if 6.0 > media >= 4.0:
#   print('Recuperação')
# if media < 4.0:
#   print('Reprovado(a)')

#O elif é uma palavra-chave em Python que significa "senão, se" e pode ser considerado uma união do else com um if. 
# Ela é usada em conjunto com a palavra-chave if para formar uma estrutura condicional encadeada.
# media = float(input('Digite a média: '))
# if media >= 6.0:
#   print('Aprovado(a)')
# elif 6.0 > media >= 4.0:
#   print('Recuperação')
# else:
#   print('Reprovado(a)')

##OPERADOR IN
# lista = 'José da Silva', 'Maria Oliveira', 'Pedro Martins', 'Ana Souza', 'Carlos Rodrigues', 'Juliana Santos', 'Bruno Gomes', 'Beatriz Costa', 'Felipe Almeida', 'Mariana Fernandes', 'João Pinto', 'Luísa Nascimento', 'Gabriel Souza', 'Manuela Santos', 'Thiago Oliveira', 'Sofia Ferreira', 'Rafael Albuquerque', 'Isabella Gomes', 'Bruno Costa', 'Maria Martins', 'Rafaela Souza', 'Matheus Fernandes', 'Luísa Almeida', 'Beatriz Pinto', 'Mariana Rodrigues', 'Gabriel Nascimento', 'João Ferreira', 'Maria Albuquerque', 'Felipe Oliveira'
# nome_1 = 'Mariana Rodrigues'
# nome_2 = 'Marcelo Nogueira'
# if nome_1 in lista:
#   print(f'{nome_1} está na lista')
# else:
#   print(f'{nome_1} não está na lista')
# if nome_2 in lista:
#   print(f'{nome_2} está na lista')
# else:
#   print(f'{nome_2} não está na lista')

# 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
# numero_impar = int(input('digite um número impar:  '))
# numero_par= int(input('digite um número par:   '))
# if numero_impar > numero_par:
#  print('numero impar é maior do que numero par')
# else:
#   print('numero par é maior do que numero impar')

# 2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe 
# se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
# maior ou menor de zero
# percentual_crescimento = float(input('qual o percentual de crescimento da empresa?  '))
# if percentual_crescimento >= 0:
#   print(f'A empresa apresentou crescimento de {percentual_crescimento} nesse ano')
# else:
#   print('A empresa não cresceu no último ano')

# # 3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
# v= str("a"),("e"),("i"),("o"),("u")
# letra = input('escreva a primeira letra do seu nome:   ')
# if v == "a" or v == "e" or v == "i" or v == "o" or  v == "u":
#   print('seu nome começa com uma vogal')
# else:
#   print('seu nome começa com uma consoante')

# 4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e 
# exiba o valor mais alto e mais baixo entre esses três anos.
# carro_2020 = 2.000
# carro_2021 = 3.500
# carro_2022 = 5.700
# media = (carro_2020 + carro_2021 + carro_2022) / 3
# print(f'a média de valores de carro nos últimos 03 anos foi {media}')
# ?????????????????????????????????

# 5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
sabonete = ('qual o valor do sabonete?  ')
pasta =  ('qual o valor da pasta?   ')
escova = ('qual o valor da escova?   ')
if (pasta > sabonete):
  print(pasta)
if (escova > sabonete):
  print(escova)
  print(input('mais caro: '))

    # # Achando o menor número
    # menor = primeiro

    # if (segundo < menor):
    #     menor = segundo
    # if (terceiro < menor):
    #     menor = terceiro

    # print('Menor: ',menor)



# 6) Escreva um programa que leia três números e os exiba em ordem decrescente.

# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") 
# e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
# turno = input('qual turno voce estuda:  ')
# if turno == 'manhã':
#   print('Bom dia!')
# elif turno == 'tarde':
#   print('boa tarde!')
# elif turno == 'noite':
#   print('boa noite!')

# 8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

# 9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.




hora = 14
# minutos = 53
# dia = 26
# mes = 20
# ano = 2023
# saida = str(hora) + ':' + str(minutos)
# saida = str(dia) + '/' + str(mes) + '/' + str(ano) + '' + str(hora) + ':' + str(minutos)