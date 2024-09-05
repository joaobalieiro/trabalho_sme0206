# Nome: João Pedro Pereira Balieiro
# nUSP: 12676615

# Método da Falsa Posição, o método das secantes sai do intervalo [1,2]
import numpy as np

raiz_exata = 12/7

# Definição da função f(x)
def f(x):
    return 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

# Arredondar para 6 casas decimais
def arredondar(x):
    return round(x, 8)

# Método da Falsa Posição
def falsa_posicao(f, a, b, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos. Intervalo fornecido: [{}, {}]".format(a, b))
        return None

    iteracoes = []
    a, b = arredondar(a), arredondar(b)

    for k in range(1, max_iter + 1):
        # Calcula a nova aproximação usando a fórmula da Falsa Posição
        fa = arredondar(f(a))
        fb = arredondar(f(b))
        x_new = arredondar(b - fb * (b - a) / (fb - fa))
        # Calcula o erro em relação à raiz exata
        erro = arredondar(x_new - raiz_exata)
        iteracoes.append((k, a, b, x_new, arredondar(f(x_new)), erro))

        # Critério de parada: se a nova estimativa for igual à anterior (considerando arredondamento)
        if k > 1 and iteracoes[-1][3] == iteracoes[-2][3]:
            # Repetir o último valor para mostrar que o resultado não muda
            iteracoes.append((k + 1, a, b, x_new, arredondar(f(x_new)), erro))
            break

        # Atualiza os extremos a ou b de acordo com o sinal da função
        if fa * f(x_new) < 0:
            b = x_new
        else:
            a = x_new

    return iteracoes

# Aplicação do Método da Falsa Posição no intervalo [1, 2]
falsa_posicao_resultados = falsa_posicao(f, 1, 2)

# Mostrar o resultado do método da Falsa Posição
if falsa_posicao_resultados:
    def print_resultados_falsa_posicao(resultados):
        print("\nMétodo da Falsa Posição (Intervalo [1, 2]):")
        print("Iteração |       a       |       b       |       x_k       |      f(x_k)     |       Erro")
        for it in resultados:
            print(f"{it[0]:>8} | {it[1]:>12.8f} | {it[2]:>12.8f} | {it[3]:>13.8f} | {it[4]:>13.8f} | {it[5]:>13.8f}")
    print_resultados_falsa_posicao(falsa_posicao_resultados)
