# 8. Seja a seguinte série: 1, 4, 9, 16, 25, 36, ... Escreva um programa que gere esta série até o N-ésimo termo, digitado pelo usuário.

# ALTERNATIVA 1
n = int(input("Digite o número: "))
cont = 0
while cont < n:
    cont += 1
    print(cont ** 2)


# ALTERNATIVA 2

n = int(input("Digite o número: "))
for num in range(1, n+1):
    print(num ** 2)


