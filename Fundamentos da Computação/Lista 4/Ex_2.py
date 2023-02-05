# 2. Elabore um programa que leia 10 números inteiros em um vetor e imprima os na ordem inversa. ,

# Alternativa 1 - Usando method append
lista = []
lista_inversa = []
for x in range(1, 11):
    num = int(input(f"Digíte o {x}º valor: "))

    lista.append(num)

for x in range(len(lista)-1, -1, -1):
    lista_inversa.append(lista[x])

print(lista_inversa)


# Alternativa 2 - Sem usar method append

lista = []
lista_inversa = []
for x in range(1, 4):
    num = int(input(f"Digíte o {x}º valor: "))

    lista = lista + [num]

for x in range(len(lista)-1, -1, -1):
    lista_inversa = lista_inversa + [lista[x]]

print(lista_inversa)
    
    

    
