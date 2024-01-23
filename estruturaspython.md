## Estrutura print
- print('Ola mundo!')
- print(10)
- print('Dafne', '29', 'é muito linda', 42.42)

nome = "dafne"

sobrenome = "salas"

print(nome, sobrenome)

print('dafne', 'salas')

## String interpolada
string_interpolada = f'{4}/setembro/{1994}
- print(string_interpolada)

string_interpolada_2 = str(4) + '/setembro/' + str(1994)
- print(string_interpolada_2)


- nascimento = (4, 'setembro', 1994)
- print(nascimento)
- print(4, 'setembro', 1994)

## Format
nome = "DAFNE"

idade = 29

print(f'Olá {nome}, você tem {idade} anos.')


## Método
Função que está associada a objetos em Python
- letras maiúsculas > str.upper()
- letras minúsculas > str.lower()
- remover espaços em branco antes e depois > str.strip()
- substituir caracter antigo pelo novo > str.replace('y', 'z')