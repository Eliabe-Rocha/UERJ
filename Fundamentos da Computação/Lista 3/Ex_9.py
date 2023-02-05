# 9. Faça um programa que leia a média de alunos de uma determinada turma, encontre e exiba o maior valor de média inserida.
# Obs.: Não há informação prévia sobre a quantidade de alunos da turma.


# ALTERNATIVA 1
n = int(input("Digite o número de alunos da turma: "))
cont = 0
lista_notas = []
while cont < n:
    media = float(input("Digite a média do aluno: "))
    lista_notas.append(media)
    cont += 1

max = float('-inf')
for num in lista_notas:
    num = int(num)
    if num > max:
        max = num

print(max)

# ALTERNATIVA 2


