# Nome: João Pedro Pereira Balieiro
# nUSP: 12676615

# Método da Bissecção
import numpy as np

# Definição da função f(x)
def f(x):
    return 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

def arredondar(x):
    return round(x, 8)

# Método da Bisseção
def bissecao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos. Intervalo fornecido: [{}, {}]".format(a, b))
        return None

    iteracoes = []
    a, b = arredondar(a), arredondar(b)
    raiz_exata = 12/7  # Usada apenas para calcular o erro

    for k in range(1, max_iter + 1):
        # Calcula o ponto médio
        c = arredondar((a + b) / 2)
        # Calcula o erro em relação à raiz exata
        erro = abs(c - raiz_exata)
        iteracoes.append((k, a, b, c, arredondar(f(c)), erro))

        # Critério de parada: se o intervalo é suficientemente pequeno
        if f(c) == 0 or b == c or a == c:
            iteracoes.append((k + 1, a, b, c, arredondar(f(c)), erro))
            break

        # Atualiza os extremos a ou b de acordo com o sinal da função
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return iteracoes

# Aplicação do Método da Bisseção no intervalo [0, 1]
bissecao_resultados = bissecao(f, 1, 2)

# Mostrar o resultado do método da Bisseção
if bissecao_resultados:
    def print_resultados_bissecao(resultados):
        print("\nMétodo da Bisseção (Intervalo [0, 1]):")
        print("Iteração |       a       |       b       |       x_k       |      f(x_k)     |       Erro")
        for it in resultados:
            print(f"{it[0]:>8} | {it[1]:>12.8f} | {it[2]:>12.8f} | {it[3]:>13.8f} | {it[4]:>13.8f} | {it[5]:>13.10f}")
    print_resultados_bissecao(bissecao_resultados)



