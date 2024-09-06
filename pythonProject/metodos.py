# Nome: João Pedro Pereira Balieiro
# nUSP: 12676615

import numpy as np
import matplotlib.pyplot as plt

# Definição da função f(x) e sua derivada f'(x)
def f(x):
    return 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

def df(x):
    return 315*x**4 - 1524*x**3 + 1488*x**2 + 408*x - 544

# Arredondar para 6 casas decimais
def arredondar(x):
    return round(x, 10)

f = arredondar(63*0.66666831**5 - 381*0.66666831**4 + 496*0.66666831**3 + 204*0.66666831**2 - 544*0.66666831 + 192)
f = arredondar(12/7)
print(12/7)
# Método da Bisseção
def bissecao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos. Intervalo fornecido: [{}, {}]".format(a, b))
        return None
    iteracoes = []
    a, b = arredondar(a), arredondar(b)
    c_old = None
    for k in range(1, max_iter + 1):
        c = arredondar((a + b) / 2)
        erro = abs(c - (c_old if c_old is not None else c))
        iteracoes.append((k, a, b, c, arredondar(f(c)), erro))
        if erro < tol:
            # Repetir o último valor para mostrar que o resultado não muda
            iteracoes.append((k+1, a, b, c, arredondar(f(c)), erro))
            break
        c_old = c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return iteracoes

# Método de Newton
def newton(f, df, x0, tol=1e-6, max_iter=100):
    iteracoes = []
    x = arredondar(x0)
    for k in range(max_iter):
        fx = arredondar(f(x))
        dfx = arredondar(df(x))
        if dfx == 0:  # Evitar divisão por zero
            print("Derivada zero. Método de Newton falhou.")
            return None
        x_new = arredondar(x - fx / dfx)
        erro = abs(x_new - x)
        iteracoes.append((k, x, fx, dfx, erro))
        if erro < tol:
            # Repetir o último valor para mostrar que o resultado não muda
            iteracoes.append((k+1, x_new, arredondar(f(x_new)), arredondar(df(x_new)), erro))
            break
        x = x_new
    return iteracoes

# Método das Secantes
def secantes(f, x0, x1, tol=1e-6, max_iter=100):
    iteracoes = []
    x0, x1 = arredondar(x0), arredondar(x1)
    for k in range(max_iter):
        fx0 = arredondar(f(x0))
        fx1 = arredondar(f(x1))
        if fx1 == fx0:  # Evitar divisão por zero
            print("Divisão por zero. Método das Secantes falhou.")
            return None
        x_new = arredondar(x1 - fx1 * (x1 - x0) / (fx1 - fx0))
        erro = abs(x_new - x1)
        iteracoes.append((k, x1, fx1, erro))
        if erro < tol:
            # Repetir o último valor para mostrar que o resultado não muda
            iteracoes.append((k+1, x_new, arredondar(f(x_new)), erro))
            break
        x0 = x1
        x1 = x_new
    return iteracoes

# Aplicação dos métodos nos intervalos [0, 1] e [1, 2]
# Método da Bisseção
bissecao_resultados = bissecao(f, 0, 1)
if bissecao_resultados:
    def print_resultados_bissecao(resultados):
        print("Método da Bisseção (Intervalo [0, 1]):")
        print("Iteração |       a       |       b       |       x_k       |      f(x_k)     |       Erro")
        for it in resultados:
            print(f"{it[0]:>8} | {it[1]:>12.6f} | {it[2]:>12.6f} | {it[3]:>13.6f} | {it[4]:>13.6f} | {it[5]:>13.6f}")
    print_resultados_bissecao(bissecao_resultados)

# Método de Newton
newton_resultados = newton(f, df, 1.5)
if newton_resultados:
    def print_resultados_newton(resultados):
        print("\nMétodo de Newton (Intervalo [1, 2]):")
        print("Iteração |       x_k       |      f(x_k)     |      f'(x_k)    |       Erro")
        for it in resultados:
            print(f"{it[0]:>8} | {it[1]:>13.6f} | {it[2]:>13.6f} | {it[3]:>13.6f} | {it[4]:>13.6f}")
    print_resultados_newton(newton_resultados)

# Método das Secantes
secantes_resultados = secantes(f, 1, 2)
if secantes_resultados:
    def print_resultados_secantes(resultados):
        print("\nMétodo das Secantes (Intervalo [1, 2]):")
        print("Iteração |       x_k       |      f(x_k)     |       Erro")
        for it in resultados:
            print(f"{it[0]:>8} | {it[1]:>13.6f} | {it[2]:>13.6f} | {it[3]:>13.6f}")
    print_resultados_secantes(secantes_resultados)


