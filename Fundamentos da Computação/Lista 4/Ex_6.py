# 6. Escreva um programa que leia um vetor de 15 elementos reais e calcule a
# diferença entre o maior e o menor elemento existente, assim como as posições
# que os mesmos ocupam.
import math

vetor_1 = []
lista_order = []



while True:
    for cont in range(1, 7):
        num_1 = int(input(f"Digite o {cont}º valor: "))
        vetor_1 = vetor_1 + [num_1]

    max_num = float('-inf')
    for num in vetor_1:
        if num > max_num:
            max_num = num
        lista_order = lista_order + [num]

    min_num = float('inf')
    for num in vetor_1:
        if num  < min_num:
            min_num = num

    posi_min = 0
    posi_max = 0
    for x in range(0, len(vetor_1)):
        if vetor_1[x] == min_num:
            posi_min = x
        elif vetor_1[x] == max_num:
            posi_max = x
        

        

    print(f"A diferença entre os valores {max_num} e {min_num} é {abs(max_num - min_num)}.")
    print(f"A posição de {max_num} e {min_num} é {posi_max} e {posi_min}, respectivamente")
    break
