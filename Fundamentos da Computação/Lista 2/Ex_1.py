# Faça um programa que simule uma calculadora com as quatro operações básicas.
# O programa deve apresentar um menu com opções de acordo com cada operação.
# O programa deve ler dois valores e, de acordo com a operação escolhida pelo usuário, ele deve retornar o resultado.

print("Bem vindo a Calculadora!")
print("Por gentileza, escolha uma das quatro operações báscias:")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

estado = True

while estado:
    try:
        operacao = int(input("Por gentileza, escolha uma das quatro operações báscias: "))
        if operacao > 4 or operacao < 1:
            print("Operação inválida!!!\nPor favor, digite uma das opções válidas.")
        else:
            n1 = int(input("Digite o primeiro valor: "))
            n2 = int(input("Digite o segundo valor: "))

            if operacao == 1:
                soma = n1 + n2
                print(f"\nO resultado da soma de {n1} e {n2} é {soma}.")
                
            elif operacao == 2:
                subtracao = n1 - n2
                print(f"\nO resultado da subtração de {n1} e {n2} é {subtracao}.")

            elif operacao == 3:
                multiplicacao = n1 * n2
                print(f"\nO resultado da multiplicação de {n1} e {n2} é {multiplicacao}.")

            else:
                divisao = n1 / n2
                print(f"\nO resultado da divisão de {n1} e {n2} é {divisao}.")

            continua = int(input("Deseja realizar outra operação? (1 - Sim, 2 - Não) "))
            if continua == 2:
                estado = False
    except:
        print("POr favor, digite apenas números entre 1 e 4.\n")
