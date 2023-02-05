# 8. Faça um programa que preencha um vetor de 10 números e leia um número x.
# O programa deve contar os múltiplos desse número x no vetor e mostrar a
# quantidade calculada bem como os múltiplos na tela.

vetor_1 = []
multiplos = []
contador = 0


while len(vetor_1) < 10:
    num_1 = int(input("Digite o valor para a primeira lista: "))
    vetor_1 = vetor_1 + [num_1]

num_comp = int(input("Digite o valor que deseja consultar: "))
for num in vetor_1:
    if num % num_comp == 0:
        multiplos = multiplos + [num]
        contador += 1

print(f"Há {contador} valores que são múltiplos de {num_comp} e estes são {multiplos}.")



        
        
    
