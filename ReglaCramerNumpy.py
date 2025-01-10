import numpy as np
from scipy.optimize import linprog

# Coeficientes del sistema de ecuaciones
A = np.array([[1, 3], [1.5, 2]])
b = np.array([300, 350])

# Resolver el sistema de ecuaciones utilizando la función linprog
x = np.linalg.solve(A, b)

# Imprimir la solución óptima
print("La cantidad óptima de unidades de A es:", int(x[0]))
print("La cantidad óptima de unidades de B es:", int(x[1]))
