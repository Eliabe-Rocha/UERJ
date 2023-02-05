# 5. Escreva um programa que gera números entre 1000 e 1999 e mostra aqueles que divididos por 11 dão resto 5.

# ALTERNATIVA 1
x = 1000
while x < 1999:
    x += 1 # mesma coisa que x = x + 1
    if x % 11 == 5:
        print(x)

# ALTERNATIVA 2
for x in range (1000, 1999):
    if x % 11 == 5:
        print(x)

