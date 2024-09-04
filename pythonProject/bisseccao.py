# Método da Bisseção
import math
import matplotlib.pyplot as plt
import numpy as np

def arredondar(x):
    return round(x, 6)

# Entrada
# intervalo [a , b]
a = 0
b = 1
# tolerância
tolerancia = 1e-6
# número máximo de loop
nloop = 1000

def f(x):
    return 63*x**5 - 381*x**4 + 496*x**3 + 204*x**2 - 544*x + 192

# header tabela
print("Método da Bisseção")
print("n a b x f(a) f(x) f(b) f(a)*f(x) erro")

n = arredondar(1)
fa = arredondar(f(a))
fb = arredondar(f(b))
xm2 = arredondar((a + b)/2)
fxm = arredondar(f(xm2))
v = arredondar(fa*fxm)
erro = 0

print("%2d"%n, "%10.6f"%a, "%10.6f"%b, "%10.6f"%xm2, "%10.6f"%fa,
          "%10.6f"%fb, "%10.6f"%fxm, "%10.6f"%v, "%10.6f"%erro)

if v < 0: b = arredondar(xm2)
if v > 0: a = arredondar(xm2)
if v == 0: print("o valor da raiz é %8.6f" %xm2)

xm1 = 0
while(xm2 != xm1):
    xm1 = arredondar(xm2)
    n = arredondar(n + 1.)
    xm2 = arredondar((a + b)/2)
    fxm = arredondar(f(xm2))
    erro = arredondar(math.fabs(xm1 - xm2))
    v = arredondar(fa*fxm)
    if v < 0: b = arredondar(xm2)
    if v > 0: a = arredondar(xm2)
    print("%2d"%n, "%10.6f"%a, "%10.6f"%b, "%10.6f"%xm2, "%10.6f"%fa,
          "%10.6f"%fb, "%10.6f"%fxm, "%10.6f"%v, "%10.6f"%erro)
    if(n == nloop):
        break

print("\nA raiz aproximada é %10.6f" %xm2)

# cria o grafico da funcao
xi = np.linspace(-1, 2, 100)
fig = plt.figure()
plt.plot(xi, f(xi), '-')
plt.grid()
plt.show()

