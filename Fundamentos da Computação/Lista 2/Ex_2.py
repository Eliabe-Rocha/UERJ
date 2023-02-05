# Elaborar um programa que solicita a entrada de 3 valores (a, b, c) e verifica se esses valores podem formar ou não um triângulo.
# Você deve considerar que os valores lidos são inteiros e positivos.
# Caso os valores formem um triângulo, exiba essa informação e o valor do perímetro deste triângulo.
# Se não formarem triângulo, apenas exiba uma mensagem com essa informação.
#(Obs.: Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados.)

print("Bem vindo ao verificador de triângulo!")
print('\n')
estado = True

while estado:
    try: 
        lado_1 = int(input("\nPor gentileza, escolha o valor do primeiro lado: "))
        lado_2 = int(input("\nPor gentileza, escolha o valor do segundo lado: "))
        lado_3 = int(input("\nPor gentileza, escolha o valor do terceiro lado: "))
        
        perimetro = lado_1 + lado_2 + lado_3

        if lado_1 > 0 and lado_2 > 0 and lado_3 > 0:
            if lado_1 < (lado_2 + lado_3) and lado_2 < (lado_1 + lado_3) and lado_3 < (lado_2 + lado_1):
                print(f"Isso é um triângulo e possui perímetro {perimetro}.")
            else:
                print(f"Isso não é um triangulo!")

                cont = int(input("\nDeseja tentar novos valores? (1 - Sim e qualquer tecla - Não) "))
                if cont != 1:
                    estado = False
        else:
            print("Não é possível que um triângulo tenha lado menor que 1. \nDigite valores válidos!!")


            
    except:
        
        print("Digite valores válidos! \nNão são permitidas letras ou números qubrados (1.5 ou 3,2)")

        cont = int(input("\nDeseja tentar novos valores? (1 - Sim e qualquer número - Não) "))
        if cont != 1:
            estado = False
            print("Fim do programa!!!")


        
