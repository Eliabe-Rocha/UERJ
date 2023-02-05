import math
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

def delta(a, b, c):
    valor_delta = b**2 - 4*a*c
    return valor_delta

def raizes():
    delta_1 = delta(a,b,c)

    if delta_1 < 0:
        return print(f'Não há raizes para os valores {a}, {b} e {c}')
    elif delta_1 == 0:
        x_1 = (b*(-1)+ math.sqrt(delta_1))/2*a
        return print(f'O delta da raiz é 0, portanto a raíz da equação é  {x_1}')
    else:
        x_1 = (b*(-1)+ math.sqrt(delta_1))/2*a
        x_2 = (b*(-1)- math.sqrt(delta_1))/2*a

        return print(f'As raizes da equção são {x_1} e {x_2}')
    

raizes()
