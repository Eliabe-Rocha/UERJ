# 2. Escreva um programa que imprima todos os números no intervalo de 1 a 100, em ordem decrescente, utilizando estrutura de repetição.

# ALTERNATIVA 1
x = 100
while x > 0:
    print(x)
    x = x - 1 # é a mesma coisa que (x -= 1)


# ALTERNATIVA 2
for x in range(100, 0, -1): # range(inicio, fim, saltono valor)
    print(x)
