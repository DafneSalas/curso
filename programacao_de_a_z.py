# Calcula o lucro total com base na materia prima, valor final e tempo de trabalho
def calcula_lucro(custo_materia_prima, valor_final, tempo_de_trabalho, tem_fita):
    MAO_DE_OBRA = 7
    CUSTO_EMBALAGEM = 2.14
    CUSTO_DA_FITA = 5.50
    custo_tempo_de_trabalho = tempo_de_trabalho * MAO_DE_OBRA
    custo_total = custo_materia_prima + custo_tempo_de_trabalho + CUSTO_EMBALAGEM
    if tem_fita:
        custo_total = custo_total + CUSTO_DA_FITA
    valor_bruto = valor_final - custo_total
    return round(valor_bruto, 2)

# PSEUDOCODIGO
# - lucro = valor total - custos
#  - custos:
#    - fita: opcional, o cliente pode não querer a fita



lucro_caixa_pequena = calcula_lucro(6.0, 30.0, 2.0, True)
print(lucro_caixa_pequena)


lucro_kit_nene = calcula_lucro(68.50, 200.0, 4.0, False)
print(lucro_kit_nene)

# DAKI PRA BAIXO EH A AULA!


# tamanho = len(st)
# print (tamanho)

# print (st1+st2)

# hora = 14
# minutos = 53
# dia = 26
# mes = 20
# ano = 2023
# saida = str(hora) + ':' + str(minutos)
# saida = str(dia) + '/' + str(mes) + '/' + str(ano) + '' + str(hora) + ':' + str(minutos)