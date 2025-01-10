# Matriz de coeficientes
A = np.array([[1, 3], [1.5, 2]])

# Vector de términos independientes
b = np.array([300, 350])

# Determinante de la matriz de coeficientes
detA = np.linalg.det(A)

# Determinantes de las matrices obtenidas al reemplazar cada columna por b
detA1 = np.linalg.det(np.column_stack((b, A[:, 1])))
detA2 = np.linalg.det(np.column_stack((A[:, 0], b)))

# Solución del sistema
x = detA1 / detA
y = detA2 / detA

# Imprimir resultados
print("La empresa puede fabricar {:.2f} unidades del tipo A y {:.2f} unidades del tipo B al mes".format(round(x, 2), round(y, 2)))
