## Faça um programa que leia a medida de um raio e crie duas funções:
## uma para calcular a área do círculo e outra para calcular o perímetro da circunferência.
## Ao final, o programa deve exibir o resultado dos cálculos.


def areaCirculo(raio):
    area = 3.14 * raio ** 2
    return area

def perimetroCirculo(raio):
    perimetro = 2 * 3.14 * raio
    return perimetro


while True:
    print("########### Bem vindo!!! ###########")
    raio = int(input("Digite o valor do raio: "))
    print(f"A área do cículo de raio {raio} é {areaCirculo(raio)}")
    print(f"\nO perímetro (circunferência)do cículo de raio {raio} é {perimetroCirculo(raio)}")
              
    loop = bool(int(input("\nDeseja realizar outra consulta? (qualquer número - Sim, 0 - Não)\n")))
    if loop == False:
        print("Obrigado por usar a aplicação")
        break
        
    
