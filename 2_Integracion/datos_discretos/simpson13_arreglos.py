"""
    Simpson 1/3 para datos discretos.
    ================================

    ✓ 5 puntos → 4 intervalos (PAR) → OK
    ❌ 4 puntos → 3 intervalos (IMPAR) → Error

    ============
    ERROR COMÚN:
    - El número de intervalos debe ser par (número de puntos impar).
    - El espaciamiento entre puntos debe ser constante.

    ====================
    EJEMPLO DEL PARCIAL:
    • Si tienes 7 puntos → 6 intervalos (PAR ✓)
    • Si tienes 5 puntos → 4 intervalos (PAR ✓)
    • Espaciamiento: CONSTANTE
    • Número de puntos: IMPAR (3, 5, 7, 9, ...)
"""

def simpson13_arreglos(x, y):
    """
    Simpson 1/3 para datos discretos.

    PARÁMETROS:
    -----------
    x, y : lists
        x: valores de x (ordenados y con espaciamiento constante)
        y: valores de y correspondientes a x

    RETORNA:
    --------
    float
        Aproximación de la integral.

    REQUISITOS:
    -----------
    - Número de puntos debe ser impar (número de intervalos par).
    - Espaciamiento entre puntos debe ser constante.
    """

    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud.")
    if len(x) < 3:
        raise ValueError("Se necesitan al menos 3 puntos.")
    if (len(x) - 1) % 2 != 0:
        raise ValueError("El número de intervalos debe ser par (número de puntos impar).")

    # Verificar que el espaciamiento sea constante
    h = x[1] - x[0]
    if not all(abs((x[i + 1] - x[i]) - h) < 1e-6 for i in range(len(x) - 1)):
        raise ValueError("El espaciamiento entre puntos debe ser constante.")

    # Aplicar la regla de Simpson 1/3
    suma = y[0] + y[-1]  # f(x₀) + f(xₙ)
    for i in range(1, len(x) - 1):
        coef = 4 if i % 2 != 0 else 2  # Alterna entre 4 y 2
        suma += coef * y[i]

    resultado = (h / 3) * suma
    return resultado


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # Define los datos x e y aquí
    x = [0, 0.25, 0.5, 0.75, 1.0]  # Ejemplo: valores de x
    y = [0.0, 0.0625, 0.25, 0.5625, 1.0]  # Ejemplo: valores de y (y = x²)
    resultado = simpson13_arreglos(x, y)
    print(f"Resultado: {resultado}")
