import math

# Definición de la función a integrar
def f(x):
    # Cambiar el comentario para seleccionar la función deseada
    # return math.exp(x**2)
    # return 1 + (math.exp(-x) * math.sin(4 * x))
    # return math.sin(math.pi * x)
    # return 1 + (math.exp(-x) * math.cos(4 * x))
    return math.sin(math.sqrt(x))  # Función actual seleccionada

# Implementación del método de Simpson 3/8 compuesto
def sim38(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 3 != 0:
            s += 3 * f(a + i * h)
        else:
            s += 2 * f(a + i * h)
    S = (3 / 8) * h * s
    return S

def main():
    a = float(input("Ingrese límite inferior de integración: "))
    b = float(input("Ingrese límite superior de integración: "))  # Corregí "inferior" a "superior"
    n = 2
    while n % 3 != 0:  # Validación de que n sea múltiplo de 3
        n = int(input("Ingrese número de intervalos de integración (múltiplo de 3): "))
        if n % 3 != 0:
            print("\nEl valor de n debe ser múltiplo de 3.\n")
    Sim38 = sim38(a, b, n)
    print(f"\nLa integración por método compuesto de Simpson 3/8 es: {Sim38:.7f}")

main()
