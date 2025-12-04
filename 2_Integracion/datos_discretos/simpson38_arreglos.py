"""
==============================================================================
SIMPSON 3/8 PARA DATOS DISCRETOS
==============================================================================

TEORÍA:
-------
Simpson 3/8 con datos discretos. Requiere espaciamiento CONSTANTE y
número de intervalos múltiplo de 3.

FÓRMULA:
--------
   I ≈ (3h/8) × [y₀ + 3y₁ + 3y₂ + 2y₃ + 3y₄ + 3y₅ + 2y₆ + ... + yₙ]

REQUISITOS:
-----------
⚠ Número de intervalos debe ser MÚLTIPLO DE 3
⚠ Espaciamiento h debe ser CONSTANTE

PATRÓN: 1, 3, 3, 2, 3, 3, 2, ..., 3, 3, 1

==============================================================================
"""

def simpson38_arreglos(x, y):
    """
    Simpson 3/8 con datos discretos.

    PARÁMETROS:
    -----------
    x, y : lists (número de intervalos múltiplo de 3)

    RETORNA:
    --------
    float
    """

    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud.")
    if (len(x) - 1) % 3 != 0:
        raise ValueError("El número de intervalos debe ser múltiplo de 3.")
    if len(x) < 4:
        raise ValueError("Se necesitan al menos 4 puntos.")

    h = x[1] - x[0]

    print("\n" + "="*80)
    print("PROCEDIMIENTO - SIMPSON 3/8 PARA DATOS DISCRETOS")
    print("="*80)
    print(f"{'i':>5} | {'xᵢ':>10} | {'yᵢ':>10} | {'Coef':>10} | {'Contribución':>15}")
    print("-"*80)

    suma = y[0] + y[-1]
    print(f"{0:>5} | {x[0]:>10.4f} | {y[0]:>10.4f} | {'1':>10} | {y[0]:>15.4f}")
    for i in range(1, len(x) - 1):
        coef = 2 if i % 3 == 0 else 3
        contrib = coef * y[i]
        suma += contrib
        print(f"{i:>5} | {x[i]:>10.4f} | {y[i]:>10.4f} | {coef:>10} | {contrib:>15.4f}")
    print(f"{len(x)-1:>5} | {x[-1]:>10.4f} | {y[-1]:>10.4f} | {'1':>10} | {y[-1]:>15.4f}")

    resultado = (3 * h / 8) * suma
    print("-"*80)
    print(f"Suma total: {suma:.4f}")
    print(f"Resultado final: I = (3h/8) * Suma = (3*{h}/8) * {suma:.4f} = {resultado:.4f}")
    print("="*80 + "\n")
    return resultado


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [1, 2, 5, 10, 17, 26, 37]
    resultado = simpson38_arreglos(x, y)
    print(f"Resultado: {resultado}")
