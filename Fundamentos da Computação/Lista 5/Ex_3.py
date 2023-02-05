#  Construa um programa que leia uma matriz 4x4 e calcule e imprima a soma da diagonal principal.


matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
diag_p = 0
vetor_diag = []

for x in range(1, len(matriz)+1):
    for y in range(0, 4):
        num = int(input(f"Digite o valor da linha {x} coluna {y}: "))
        matriz[x-1][y-1] = matriz[x-1][y-1] + num

# Soma os valores da daigonal
for x in range(0, len(matriz)):
    diag_p += matriz[x][x]
    vetor_diag = vetor_diag + [matriz[x][x]]

# Exibe a matriz
for x in range(0, len(matriz)):
    print(matriz[x])    


# Imprime o vetor principal
print(f"\nOs valores na diagonal principal são {vetor_diag}")
    
print(f"\nA soma dos valores da diagonal da matriz é: {diag_p}")
