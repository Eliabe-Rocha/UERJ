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
        lista = [a]*b # Cria um vetor de elementos com o número (b) de bases
        resultado = 1 # Variável nula para multiplicação dos elementos
        for num in lista:
            resultado *= num # Multiplica ovalor em resultado pelo próximo valor da lista
        return resultado 



### Teste
print(eleva('a', 3))
print(eleva(-3, 3))
print(eleva(3, 2.5))
print(eleva(5, 5))
print(eleva(2, 10))

