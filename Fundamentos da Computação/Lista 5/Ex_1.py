# Faça um programa que leia uma matriz 3x3 e ao final imprima a soma de seus elementos.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for x in range(1, len(matriz)+1):
    for y in range(1, 4):
        num = int(input(f"Digite o valor da linha {x} coluna {y}: "))
        soma += num
print(f"A soma dos valores da matriz é: {soma}")
