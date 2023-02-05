# 6. Faça um programa que calcule o fatorial de um número positivo informado pelo usuário. O fatorial de um número, positivo,
# é calculado pela multiplicação sucessiva dos seus antecessores, até alcançar o valor 1.
# Obs.: Fatorial de 1 = 1 e Fatorial de 0 = 1
# Exemplo: Fatorial de 4 = 4 * 3 * 2 * 1


# ALTERNATIVA 1
x = int(input("Digite o número que deseja ver o fatorial: "))
valor  = x
y = 1

if x < 0:
    print("operação inválida")
else:
    while x > 0:
        y = y * x
        x = x - 1
    print(f"O  de {valor} é {y}")


# ALTERNATIVA 2
x = int(input("Digite o número que deseja ver o fatorial: "))
y = 1
if x < 0:
    print("operação inválida")
else:
    for num in range(x, 1, -1):
        y *= num
    print(y)
    
        

