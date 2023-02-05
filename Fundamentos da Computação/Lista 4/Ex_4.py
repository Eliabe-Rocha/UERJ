# 4. Faça um programa que preencha um vetor de 15 posições com números
# inteiros e, após a leitura, atribua valor 0 para todos os elementos que possuírem
# valores negativos. Ao final, o programa deve imprimir o vetor resultante.

vetor_pos = []

while True:

    if len(vetor_pos) < 5:
        num = int(input("Digite um valor: "))

        if num >= 0:
            vetor_pos = vetor_pos + [num]# Se puder e quiser, é possível usar o method append  aqui (vetor_pos.append(num))
        else: 
            vetor_pos = vetor_pos + [0]# Se puder e quiser, é possível usar o method append  aqui (vetor_pos.append(num))

    else:
        print(f"O vetor dos 10 primeiroos impares digitados é {vetor_pos}")
        break
