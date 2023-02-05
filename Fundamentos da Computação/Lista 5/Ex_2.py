# 2. Escreva um programa que leia uma matriz 3x3, armazene em um vetor a soma dos 
# elementos por linha e exiba a matriz e o vetor de soma.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(1, len(matriz)+1):
    for y in range(1, 4):
        num = int(input(f"Digite o valor da linha {x} coluna {y}: "))
        matriz[x-1][y-1] = matriz[x-1][y-1] + num

soma_l1 = sum(matriz[0])
soma_l2 = sum(matriz[1])
soma_l3 = sum(matriz[2])
vetor_soma = [soma_l1, soma_l2, soma_l3]


for x in range(0, len(matriz)):
    print(matriz[x])
    

    
print(f"E o vetor da soma das linhas é {vetor_soma}")


