#ESTRUTURA DE REPETIÇAO
'''''
n = 1
while n <= 10:
    print(n)
    n = n + 1
'''''
#03 médias de aluno 
'''''
contador = 1
while contador <=3:
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))
    print(f'Média: {(nota_1+nota_2)/2}')
    contador += 1
    '''''

preco = 2.00
preco += 3
print(preco)
