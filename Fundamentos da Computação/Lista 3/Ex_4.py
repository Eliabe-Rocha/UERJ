# 4. Escreva um programa que imprima todos os números pares compreendidos entre 85 a 907. O algoritmo deve também calcular a soma destes valores

# ALTERNATIVA 1
x = 85
while x < 907:
    x += 1 # mesma coisa que x = x + 1
    if x % 2 == 0:
        print(x)

# ALTERNATIVA 2
for x in range (85, 907):
    if x % 2 == 0:
        print(x)

# ALTERNATIVA 3
for x in range(86, 907, 2):
    print(x)
