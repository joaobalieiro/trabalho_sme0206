import sympy as sp

# Definir a variável simbólica
x = sp.Symbol('x')

# Definir a função simbólica
f_sym = 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

# Calcular as raízes exatas
raizes_exatas = sp.solve(f_sym, x)
print("Raízes exatas de f(x):", raizes_exatas)

