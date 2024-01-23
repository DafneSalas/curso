# nome_aluno = 'Fabricio Daniel'
# idade_aluno = 15
# media_semestre = 8.45
# aprovação = True
# print(nome_aluno,idade_aluno,media_semestre,aprovação)

# q_seguranca = 5
# s_seguranca = 3000

# q_docente = 16
# s_docente = 6000

# q_diretoria = 1
# s_diretoria = 12500
# # # A quantidade total de empregados;
# # # A diferença entre o salário mais baixo e mais alto; e
# # # A média ponderada da faixa salarial da escola.

# total_empregados = q_seguranca + q_docente + q_diretoria
# print(total_empregados)

# diferenca_salario = s_diretoria - s_seguranca
# print(diferenca_salario)

# media = (q_seguranca * s_seguranca + q_docente * s_docente + q_diretoria * s_diretoria) / (total_empregados)
# print(media)

# #exponenciacao
# exp = 2 ** 3
# print(exp)
# operador = 2
# potencia = 3
# exp = operador ** potencia
# print(exp)

# #modulo
# modulo = 7 % 3
# print(modulo)
# dividendo = 7
# divisor = 3
# modulo = dividendo % divisor
# print(modulo)

# #divisao inteira
# divisao = 7 // 3
# print(divisao)
# numerador = 7
# denominador = 3
# divisao = numerador // denominador
# print(divisao)

#string
# string1 = 'alura'
# string2 = "aula"
# print (type(string1), type (string2))

# texto = '  Geovana Alessandra dias Sanyos '
# #todo texto deve estar em letras maiusculas
# print(texto.upper())
# print(texto.lower())
# print(texto.strip())
# print(texto.replace('y','t'))
# #nos itens acima apenas fizemos a transformacao, mas o texto original continua 'errado'. 
# texto = texto.strip().replace('y', 't'). upper()
# print(texto)

#tabela unicode ---- chr(numero_do_caractere)
#import unicodedata
# char = chr(64)
# print(char)
# char1 = chr(79)
# char2 = chr(108)
# char3 = chr(225)
# texto = (char1 + char2 + char3)
# print(texto)


# nome = input('Escreva seu nome: ')
# print(f'bem vindo/a {nome}')


# cadastro de cliente

# nome = 'alguem'
# idade = 23
# sexo = 'F'
# email = 'alguem@email.com'
# telefone = '41999554176'

# nome = input('nome: ')
# idade = int(input('idade: '))
# # sexo = input('sexo: ')
# # email = input('email: ')
# # telefone = input('telefone')

# print('SALVANDO NO BANCO DE DADOS...')


# print('nome: %s\nidade: %d' %(nome, idade))


# Inteiros: int(dado_para_conversao)
# Float: float(dado_para_conversao)
# String: str(dado_para_conversao)
# Booleano: bool(dado_para_conversao)
# ano_entrada = input('Escreva o ano de ingresso do(a) estudante:  ')
# print(ano_entrada)
# print(type(ano_entrada))

# ano_entrada = int(input('Escreva o ano de ingresso do(a) estudante:  ')) <<<<<<<<<<<
# print(ano_entrada)
# print(type(ano_entrada))

#nota_entrada = float(input('Digite a nota do teste de ingresso: '))
# print(nota_entrada)
# print(type(nota_entrada))
#print(f'Ano de entrada {ano_entrada} - nota do teste de ingresso {nota_entrada}')

nome_aluno = input('nome: ')
idade_aluno = input('idade: ')
media_aluno = input('media: ')

# print('Nome do aluno: %s' %(nome_aluno))
print(f'O nome da aluna é {nome_aluno} e sua idade é {idade_aluno}.')
print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, int(idade_aluno), float(media_aluno)))
print('Nome do aluno é {}, ele tem {} anos e sua média é {}.'.format(nome_aluno, idade_aluno, media_aluno))
# print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))

# ##Uma observação: os operadores de formatação de strings com % não funcionam diretamente com valores booleanos. 
# # Uma maneira de lidar com isso é convertendo o valor booleano para uma string antes de usá-lo na formatação com a função str(). Por exemplo:s
# x = True
# print("Valor de x: %s" % str(x))

# print('Nome do aluno: {}'.format(nome_aluno))


