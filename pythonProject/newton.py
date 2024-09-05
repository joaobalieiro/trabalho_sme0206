# Nome: João Pedro Pereira Balieiro
# nUSP: 12676615

# Método de Newton
import math
import matplotlib.pyplot as plt
import numpy as np

raiz_exata = 12/7

def arredondar(x):
    return round(x, 8)

# Definição da função f(x) e sua derivada f'(x)
def f(x):
    return 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

def df(x):
    return 315*x**4 - 1524*x**3 + 1488*x**2 + 408*x - 544

# Método de Newton
def newton(f, df, x0, max_iter=100):
    iteracoes = []
    x = arredondar(x0)
    for k in range(max_iter):
        fx = arredondar(f(x))
        dfx = arredondar(df(x))
        # Evitar divisão por zero
        if dfx == 0:
            print("Derivada zero. Método de Newton falhou.")
            return None
        x_new = arredondar(x - fx / dfx)
        erro = arredondar(x - raiz_exata)
        iteracoes.append((k, x, fx, dfx, erro))
        if x == x_new:
            iteracoes.append((k + 1, x_new, arredondar(f(x_new)), arredondar(df(x_new)), erro))
            break
        x = x_new

    return iteracoes

# Tabela do Método de Newton
newton_resultados = newton(f, df, 2) # Trocar 2 para 1 quando o intervalo for [0,1]
if newton_resultados:
    def print_resultados_newton(resultados):
        print("\nMétodo de Newton (Intervalo [1, 2]):")
        print("Iteração |       x_k       |      f(x_k)     |      f'(x_k)    |       Erro")
        for it in resultados:
            print(f"{it[0]:>8} | {it[1]:>13.8f} | {it[2]:>13.8f} | {it[3]:>13.8f} | {it[4]:>13.8f}")
    print_resultados_newton(newton_resultados)
