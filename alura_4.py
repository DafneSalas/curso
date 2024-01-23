#ESTRUTURA DE REPETIÇAO
'''''
n = 1
while n <= 10:
    print(n)
    n = n + 1

#alunos = [10, 15, 20, 25, 30]
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
contador = 1
while contador <=3:
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))
    print(f'Média: {(nota_1+nota_2)/2}')
    contador += 1

#operadores de atribuição
+= adiciona valor
-= subtrai valor 
*= multiplica valor 
/= divide a variável por um valor 
//= divisão inteira da variável por um valor 
%= calcula o resto da divisão

preco = 2.00
preco += 3
print(preco)
'''''

#for elemento in conjunto:
    # código a ser executado para cada elemento
    
for contador in range (1, 21, 2):
    print(contador)


# para um valor -- comeca em zero e termina no ultimo valor -1
# 02 valore -- primeiro valor é o comeco e o segundo é o final
# for posicao in range(12):
#   print(posicao)

# for posicao in range(3, 12):
#     print(posicao, end=' - ')

total_imoveis = 0
for ano in range(2017,2023):
  quantidade_imoveis = float(input(f'Digite a quantidade de imóveis no ano {ano}: '))
  total_imoveis += quantidade_imoveis
print(f'Total de imóveis construídos: {total_imoveis} imóveis')
