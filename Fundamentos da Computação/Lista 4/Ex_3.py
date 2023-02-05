# 3. Faça um programa que declare um vetor de 10 posições, o preencha com os
# 10 primeiros números inteiros ímpares e o imprima.

vetor_pos = []

while True:

    if len(vetor_pos) < 10:
        num = int(input("Digite um valor: "))


        if num % 2 == 1 and num >= 0:
            vetor_pos = vetor_pos + [num] # Se puder e quiser, é possível usar o method append  aqui (vetor_pos.append(num))
        
    else:
        print(f"O vetor dos 10 primeiroos impares digitados é {vetor_pos}")
        break
