# 1) Faça um programa em Python que defina e armazene valores inteiros em uma matriz A
# e gere a respectiva matriz transposta. Ao final, o programa deve imprimir as duas matrizes.
# Você pode definir a dimensão da matriz A.


A = [[0]*3,[0]*3,[0]*3]
linhas = int(input("Digite o número de linhas que a matriz possuirá: "))
colunas = int(input("Digite o número de colunas que a matriz possuirá: "))


for linha in range(0,linhas):
    for coluna in range(0,colunas):
        A[linha][coluna] = int(input(f"o valor da linha {linha} e coluna {coluna}: "))


# Impressão da Matriz
print("_"*50, "\nA Matriz gerada foi:\n")
for linha in range(0, linhas):
    for coluna in range(0, colunas):
        print(f"[{A[linha][coluna]:^5}]", end="")
    print()


# Impressão da Matriz Transposta
print("_"*50, "\nA Matriz transposta gerada foi:\n")
for linha in range(0, linhas):
    for coluna in range(0, colunas):
        print(f"[{A[coluna][linha]:^5}]", end="")
    print()


