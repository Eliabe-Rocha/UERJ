# 3. Escreva um programa que imprima os 100 primeiros números ímpares.

# ALTERNATIVA 1
x = 0
while x < 100:
    x += 1
    impar = x * 2 - 1
    print(impar)



# ALTERNATIVA 2
for x in range (1, 101):
    print(x * 2 - 1)

