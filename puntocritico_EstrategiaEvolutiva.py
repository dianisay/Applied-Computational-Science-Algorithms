import sympy as sp

# Definir las variables simbólicas
x1, x2, x3 = sp.symbols('x1 x2 x3')

# Definir la función objetivo
f = x1 + 2 * x2 + x2 * x3 - x1 * x1 - x2 * x2 - x3 * x3

# Calcular las derivadas parciales de f
df_dx1 = sp.diff(f, x1)
df_dx2 = sp.diff(f, x2)
df_dx3 = sp.diff(f, x3)

# Resolver el sistema de ecuaciones df/dx = 0
solution = sp.solve((df_dx1, df_dx2, df_dx3), (x1, x2, x3))

# Imprimir la solución
print("Punto crítico (máximo):")
for variable, valor in solution.items():
    print(f"{variable}: {valor.evalf()}")
