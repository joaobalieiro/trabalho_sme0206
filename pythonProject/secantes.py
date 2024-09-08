# Nome: João Pedro Pereira Balieiro
# nUSP: 12676615
# Nome: Lucas Fernando Nishida Dias
# nUSP: 8936436

# Método das Secantes
import math
import matplotlib.pyplot as plt
import numpy as np

raiz_exata = 2/3
x0 = 0
x1 = 1

def arredondar(x):
    return round(x, 8)

# Definição da função f(x) e sua derivada f'(x)
def f(x):
    return 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

# Método das Secantes
def secantes(f, x0, x1, max_iter=100):
    iteracoes = []
    x0, x1 = arredondar(x0), arredondar(x1)
    for k in range(max_iter):
        fx0 = arredondar(f(x0))
        fx1 = arredondar(f(x1))
        if fx1 == fx0:  # Evitar divisão por zero
            print("Divisão por zero. Método das Secantes falhou.")
            return None
        x_new = arredondar(x1 - fx1 * (x1 - x0) / (fx1 - fx0))
        erro = x1 - raiz_exata
        iteracoes.append((k, x1, fx1, erro))
        if x1 == x_new:
            iteracoes.append((k + 1, x_new, arredondar(f(x_new)), x_new-raiz_exata))
            break
        x0 = x1
        x1 = x_new
    return iteracoes

# Método das Secantes
secantes_resultados = secantes(f, x0, x1)
if secantes_resultados:
    def print_resultados_secantes(resultados):
        print("\nMétodo das Secantes (Intervalo [0, 1]):")
        print("Iteração |       x_k       |      f(x_k)     |       Erro")
        for it in resultados:
            print(f"{it[0]:>8} | {it[1]:>13.8f} | {it[2]:>13.8f} | {it[3]:>13.10f}")
    print_resultados_secantes(secantes_resultados)

# Calculo da convergencia teorica
def calcular_p(x_k_mais_1, x_k, x_k_menos_1, x):
    # Calcula o numerador e o denominador da fórmula
    numerador = math.log(abs((x_k_mais_1 - x) / (x_k - x)))
    denominador = math.log(abs((x_k - x) / (x_k_menos_1 - x)))
    p = numerador / denominador
    return p
x_k_mais_1 = 0.71102000
x_k = 0.74492121
x_k_menos_1 = 0.77887974
x = 2/3
p = calcular_p(x_k_mais_1, x_k, x_k_menos_1, x)
print(f"Valor de p: {p:.8f}")

def calcular_taxa_convergencia(iteracoes):
    erros = [abs(iteracao[3]) for iteracao in iteracoes if iteracao[3] is not None and iteracao[3] != 0]
    taxas = []
    for i in range(1, len(erros) - 1):
        erro_k = erros[i]
        erro_k_1 = erros[i + 1]
        erro_k_2 = erros[i - 1]

        taxa = np.log(erro_k_1 / erro_k) / np.log(erro_k / erro_k_2)
        taxas.append(taxa)
    if taxas:
        taxa_media = np.mean(taxas)
        return taxa_media
    else:
        return None
iteracoes = secantes(f, x0, x1)
taxa_convergencia = calcular_taxa_convergencia(iteracoes)
print(f"Taxa de Convergência: {taxa_convergencia: .8f}")
