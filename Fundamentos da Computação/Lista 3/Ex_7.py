# 7. Escreva um programa que lê um valor n inteiro e positivo e que calcula a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.

# ALTERNATIVA 1
n = int(input("Digite o número: "))
S = 0
if n < 0:
    print("operação inválida")
    n = int(input("Digite o número que deseja ver o fatorial: "))
else:
    while n > 0:
        S = S + (1 / n)
        n -= 1
    print(S)


# ALTERNATIVA 2


n = int(input("Digite o número: "))
S = 0
if n < 0:
    print("operação inválida")
    n = int(input("Digite o número que deseja ver o fatorial: "))
else:
    for x in range(n, 0, -1):
        S = S + (1 / x)
    print(S)

