# Nome: João Pedro Pereira Balieiro
# nUSP: 12676615
# Nome: Lucas Fernando Nishida Dias
# nUSP: 8936436

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Definir a variável simbólica
x = sp.Symbol('x')

# Definir a função simbólica
f_sym = 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

# Calcular as raízes exatas
raizes_exatas = sp.solve(f_sym, x)
print("Raízes exatas de f(x):", raizes_exatas)

# Definir a função numérica
f = sp.lambdify(x, f_sym, "numpy")

# Criar os intervalos de x para os gráficos
x_interval_1 = np.linspace(0, 1, 400)
x_interval_2 = np.linspace(1, 2, 400)

# Calcular os valores de f(x) nos intervalos
y_interval_1 = f(x_interval_1)
y_interval_2 = f(x_interval_2)

# Criar o primeiro gráfico para o intervalo [0, 1]
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_interval_1, y_interval_1, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(2/3, color='red', linestyle='--', label='Raiz: x = 2/3')
plt.title('Gráfico de f(x) no intervalo [0, 1]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()

# Criar o segundo gráfico para o intervalo [1, 2]
plt.subplot(1, 2, 2)
plt.plot(x_interval_2, y_interval_2, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(12/7, color='red', linestyle='--', label='Raiz: x = 12/7')
plt.title('Gráfico de f(x) no intervalo [1, 2]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()


