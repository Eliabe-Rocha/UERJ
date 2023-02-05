# 2) Faça um programa que preencha uma matriz 4 x 4 com números inteiros.
# Em seguida, o programa deve socilitar que o usuário informe um valor a ser procurado na matriz
# e armazene-o em uma variável x. O programa deverá fazer uma busca desse valor na matriz e,
# ao final, informar a localização (linha e coluna) ou uma mensagem informando que o valor não foi encontrado.



linhas = int(input("Digite o número de linhas que a matriz possuirá: "))
colunas = int(input("Digite o número de colunas que a matriz possuirá: "))

# inicializa uma matriz de acordo com o tamanho especificado pelo usuário.
# [x for i in range(...)] é uma list comprehension.
A = [[0 for i in range(0, colunas)] for j in range(0, linhas)] 


# Preenche a matriz com valores especificados
for linha in range(0,linhas):
    for coluna in range(0,colunas):
        A[linha][coluna] = int(input(f"o valor da linha {linha} e coluna {coluna}: "))

# Defini o valor a ser pesquisado na matriz
valor = int(input("Por favor informe o valor que deseja procurar na matriz: "))

vari = 0 # Salva o valor comparado
l_f = 0 # Salva o índice da linha
c_f = 0 # Salva o índice da coluna

for lin in range(0, linhas):
    for col in range(0, colunas):
        if A[lin][col] == valor:
            vari = valor
            l_f = lin
            c_f = col
            print(f"O valor {vari} se encontra na linha {lin+1} coluna {col+1} da matriz {linhas}x{colunas}.")


# Gera a matriz específicando o valor a ser pesquisado
print("_"*50, "\nA Matriz gerada foi:\n")
for linha in range(0, linhas):
    for coluna in range(0, colunas):
        if linha == l_f and coluna == c_f:
            print(f"[->{A[linha][coluna]:^3}<-]", end="")
        else:
            print(f"[{A[linha][coluna]:^7}]", end="")
    print()


print("_"*50, end="")

# Especifica a linha e a coluna onde o valor se encontra, caso exista.
if vari != 0:
    print(f"\nO valor {vari} se encontra na linha {l_f+1} coluna {c_f+1} da matriz {linhas}x{colunas}.")
else:
    print("\nO valor não foi encontrado")
        




