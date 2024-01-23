#ESTRUTURA DE REPETIÇAO
'''''
n = 1
while n <= 10:
    print(n)
    n = n + 1
'''''
 alunos = [10, 15, 20, 25, 30]
# index = 0
# while index < len(alunos):
#     print(alunos[index])
#     index = index + 1

salarios = [33, 21, 30, 45]
soma_salarios = 0.0
index = 0
while index < len(salarios):
    print(salarios)
    print('index', index)
    print('valor', salarios[index])
    soma_salarios += salarios[index]
    print('soma', soma_salarios)
    index += 1
    print('-----------------------')
    
#03 médias de aluno 
'''''
contador = 1
while contador <=3:
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))
    print(f'Média: {(nota_1+nota_2)/2}')
    contador += 1
    '''''

#operadores de atribuição
preco = 2.00
preco += 3
print(preco)
