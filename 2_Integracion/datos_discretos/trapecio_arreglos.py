"""
==============================================================================
REGLA DEL TRAPECIO PARA DATOS DISCRETOS
==============================================================================

TEORÍA:
-------
Cuando te dan una TABLA de datos (x, y) en lugar de una función f(x),
usas esta versión del trapecio que suma áreas de trapecios entre puntos consecutivos.

FÓRMULA:
--------
Para cada par de puntos consecutivos (xᵢ, yᵢ) y (xᵢ₊₁, yᵢ₊₁):

   Área_trapecio = (yᵢ + yᵢ₊₁)/2 × (xᵢ₊₁ - xᵢ)

Integral total = Σ Área_trapecio

VENTAJA:
--------
✓ Funciona con espaciamiento VARIABLE (h no necesita ser constante)
✓ Ideal para datos experimentales
✓ No necesitas conocer la función f(x)

CUÁNDO USAR:
-----------
✓ Te dan una TABLA de valores (x, y)
✓ Datos experimentales o mediciones
✓ No tienes la función explícita

==============================================================================
"""

def trapecio_datos(x, y):
    """
    Calcula la integral de datos discretos usando trapecio.

    PARÁMETROS:
    -----------
    x : list - valores de x (ordenados)
    y : list - valores de y correspondientes

    RETORNA:
    --------
    float - aproximación de la integral

    EJEMPLO:
    --------
    x = [0, 1, 2, 3]
    y = [0, 1, 4, 9]  # valores de x²
    integral = trapecio_datos(x, y)
    """

    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud.")
    if len(x) < 2:
        raise ValueError("Se necesitan al menos 2 puntos.")

    print("\n" + "="*80)
    print("PROCEDIMIENTO - TRAPECIO PARA DATOS DISCRETOS")
    print("="*80)
    print(f"{'i':>5} | {'xᵢ':>10} | {'yᵢ':>10} | {'h':>10} | {'Área':>15}")
    print("-"*80)

    suma = 0
    for i in range(len(x) - 1):
        h = x[i + 1] - x[i]
        area = (y[i] + y[i + 1]) * h / 2
        suma += area
        print(f"{i:>5} | {x[i]:>10.4f} | {y[i]:>10.4f} | {h:>10.4f} | {area:>15.4f}")

    print("-"*80)
    print(f"Suma total de áreas: {suma:.4f}")
    print("="*80 + "\n")
    return suma


if __name__ == "__main__":
    x = [0, 1, 2, 3]
    y = [0, 1, 4, 9]
    resultado = trapecio_datos(x, y)
    print(f"Resultado: {resultado}")
