# 1. Escreva um programa que leia 10 números inteiros e armazene os positivos
# no vetor VETPOS e os negativos no vetor VETNEG. Ao final imprima os dois vetores.


# Alternativa 1
VETPOS = []
VETNEG = []

for x in range(1, 11):

    num = int(input(f"Digíte o {x}º número: "))

    if num >= 0:
        VETPOS.append(num)
    else:
        VETNEG.append(num)

print("\n")
print(f"O vetor de valores positivos é {VETPOS}.\n")
print(f"O vetor de valores negativos é {VETNEG}.")
        
# Alternativa 2 - Sem o uso do append

VETPOS = []
VETNEG = []

for x in range(1, 11):
    num = int(input(f"Digíte o {x}º número: "))

    if num >= 0:
       VETPOS = VETPOS + [num]
    else:
        VETNEG = VETNEG + [num] 

print(f"O vetor de valores positivos é {VETPOS}.\n")
print(f"O vetor de valores negativos é {VETNEG}.")























    
