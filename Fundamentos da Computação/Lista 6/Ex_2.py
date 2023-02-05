# Escrever uma função chamada DOBRA que multiplique um número inteiro recebido como parâmetro por 2.
# Escrever um programa para ler um valor inteiro e, utilizando a função DOBRA, calcular e exibir o dobro dele.


def dobra(entrada):
    return entrada * 2


while True:
    print("########### Bem vindo!!! ###########")
    num = int(input("Digite o valor que deseja dobrar: "))
    print(dobra(num))
              
    loop = bool(int(input("Deseja realizar outra dobra? (qualquer número - Sim, 0 - Não)\n")))
    if loop == False:
        print("Obrigado por usar a aplicação")
        break
        
    
