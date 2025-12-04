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
        raise ValueError(f"ERROR: x ({len(x)}) y y ({len(y)}) deben tener igual longitud")
    if len(x) < 2:
        raise ValueError("Se necesitan al menos 2 puntos")

    n = len(x)

    print("\n" + "="*110)
    print("REGLA DEL TRAPECIO CON DATOS DISCRETOS")
    print("="*110)
    print(f"\nNúmero de puntos: {n}")
    print(f"Rango: x ∈ [{x[0]}, {x[-1]}]")

    print("\n" + "─"*110)
    print("DATOS:")
    print("─"*110)
    print(f"{'i':>4} | {'x':>12} | {'y':>15}")
    print("─"*110)
    for i in range(n):
        print(f"{i:>4} | {x[i]:>12.6f} | {y[i]:>15.10f}")

    print("\n" + "─"*110)
    print("CÁLCULO DE ÁREAS:")
    print("─"*110)
    print(f"{'Intervalo':>10} | {'x[i]':>12} | {'x[i+1]':>12} | {'h':>10} | {'y[i]':>12} | {'y[i+1]':>12} | {'Área':>15}")
    print("─"*110)

    suma = 0
    for i in range(n - 1):
        h = x[i+1] - x[i]
        area = (y[i] + y[i+1]) * h / 2
        suma += area
        print(f"{'['+str(i)+','+str(i+1)+']':>10} | {x[i]:>12.6f} | {x[i+1]:>12.6f} | {h:>10.6f} | {y[i]:>12.6f} | {y[i+1]:>12.6f} | {area:>15.10f}")

    print("─"*110)
    print(f"\n{'INTEGRAL TOTAL: ' + f'{suma:.10f}':^110}")
    print("="*110 + "\n")

    return suma


if __name__ == "__main__":
    # ============================================================================
    # CÓMO USAR ESTE ARCHIVO EN TU PARCIAL
    # ============================================================================
    #
    # 1. Copia los datos de tu tabla:
    #    x = [valor1, valor2, valor3, ...]
    #    y = [valor1, valor2, valor3, ...]
    #
    # 2. Llama a la función:
    #    resultado = trapecio_datos(x, y)
    #
    # 3. La respuesta se muestra automáticamente y se retorna en 'resultado'
    #
    # ============================================================================

    # Escribe tu código aquí:
    pass

