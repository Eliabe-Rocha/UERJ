## 7. Faça um programa que preencha dois vetores de dez elementos inteiros cada
## um e crie um terceiro vetor resultante da intercalação entre eles.

vetor_1 = []
vetor_2 = []
vetor_3 = []

while len(vetor_1) < 10:
    num_1 = int(input("Digite o valor para a primeira lista: "))
    vetor_1 = vetor_1 + [num_1]

while len(vetor_2) < 10:
    num_2 = int(input("Digite o valor para a segunda lista: "))
    vetor_2 = vetor_2 + [num_2]

for x in range(0, len(vetor_1)):
    vetor_3 = vetor_3 + [vetor_1[x]]
    vetor_3 = vetor_3 + [vetor_2[x]]

print(f"A intercalação dos vetores {vetor_1} e {vetor_2} é {vetor_3}")



        
        
    
