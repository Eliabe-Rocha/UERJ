# Faça um programa que leia dois valores representando a base e o expoente de uma potência. 
# Você deve implementar uma função que calcula a potência a^b para valores a e b (assuma números inteiros)
# passados por parâmetro. O programa deve, após a leitura dos dados, executar a função e exibir o resultado da potência.

# Considere bases e expoentes apenas positivos.

# Obs.: Não use o operador ** nem funções de potência da biblioteca.
# Você deve desenvolver o cálculo da potência por meio da multiplicação.
### Função de elevação - Alternativa 1

def eleva(a, b):
    if (type(a) != int) or (type(b) != int) or (a < 0) or (b < 0): # Tratamento para valores inteiro positivos
        return f"Digite um número inteiro positivo!"

    else:
        lista = [a]*b
        resultado = 1
        for num in lista:
            resultado *= num
        return resultado 



### Teste
print(eleva('a', 3))
print(eleva(-3, 3))
print(eleva(3, 2.5))



# Loop para execução do programa com interface para o usuário.
continua = True
while continua:
    
    a = int(input("Digite o valor da base: "))
    b = int(input("Digite o valor do expoente: "))
    if (type(a) != int) or (type(b) != int) or (a < 0) or (b < 0): # Tratamento para valores inteiro positivos
        print( f"Digite um número inteiro positivo!")
    else:
        print(eleva(a, b))
        
    loop = int(input("Deseja tentar novos valores? (1 - Sim; qualquer valor - Não:) "))
    if loop != 1:
       continua = False
       print("Fim da execução")



        
