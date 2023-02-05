# Elabore um programa que leia uma temperatura em graus Fahrenheit e
# faça uma função que receba esse valor informado e converta de graus Fahrenheit para graus centígrados.


def conversorCF(Celsius):
    Fahrenheit = (Celsius * 1.8) + 32
    return Fahrenheit


def conversorFC(temperatura):
    Celsius = (5/9) * (temperatura - 32)
    return Celsius


while True:
    print("########### Bem vindo ao conversor de de temperaturas ###########")
    menu = int(input("Qual escala de conversão deseja usar? (1 - Celsius para Fahrenheit, 2 - Fahrenheit para Celsius)\n"))
    if menu == 1:
        temp = float(input("Informe a temperatura em Celsius que deseja converter: "))
        print(f"{conversorCF(temp)}F")
    elif menu == 2:
        temp_F = float(input("Informe a temperatura em fahrenheit que deseja converter: "))
        print(f"{conversorCF(temp)}ºC")
    else:
        print("Informe um valor válido")

    loop = bool(int(input("Deseja realizar outra conversão? (qualquer número - Sim, 0 - Não)\n")))
    if loop == False:
        print("Obrigado por usar o conversor")
        break
        
    
