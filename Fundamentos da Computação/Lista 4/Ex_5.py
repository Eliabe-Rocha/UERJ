## 5. Construa um programa que leia dois vetores com 10 elementos inteiros cada
## um e armazene em um terceiro vetor a interseção dos dois vetores. Ao final, o
## programa deve imprimir o vetor de interseção.

vetor_1 = []
vetor_2 = []
intersec_vetor = []


while True:
    print("Primeira Lista")
    for cont in range(1, 11):
        num_1 = int(input(f"Digite o {cont}º valor para a PRIMEIRA lista: "))
        vetor_1 = vetor_1 + [num_1]

    print("\nSegunda Lista")
    for cont in range(1, 11):
        num_1 = int(input(f"Digite o {cont}º valor para a SEGUNDA lista: "))
        vetor_2 = vetor_2 + [num_1]

    
    for x in vetor_1:
        for y in vetor_2:
            if x == y:
                intersec_vetor = intersec_vetor + [y]


    print(f"\nA intercção da lista {vetor_1} e a listab {vetor_2} é a lista {intersec_vetor}")
    break
