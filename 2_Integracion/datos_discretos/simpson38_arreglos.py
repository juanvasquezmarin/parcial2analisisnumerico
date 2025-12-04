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
        raise ValueError(f"x y y deben tener igual longitud")

    n_intervalos = len(x) - 1
    if n_intervalos % 3 != 0:
        raise ValueError(f"Número de intervalos debe ser múltiplo de 3. Tienes {n_intervalos}")

    if len(x) < 4:
        raise ValueError("Se necesitan al menos 4 puntos")

    h = x[1] - x[0]

    print("\n" + "="*105)
    print("SIMPSON 3/8 CON DATOS DISCRETOS")
    print("="*105)
    print(f"\nPuntos: {len(x)} (intervalos: {n_intervalos}, múltiplo de 3 ✓)")
    print(f"Espaciamiento: h ≈ {h:.6f}")

    print("\n" + "─"*105)
    print(f"{'i':>4} | {'x':>12} | {'y':>15} | {'Coef':>6} | {'Contribución':>18}")
    print("─"*105)

    suma = y[0]
    print(f"{0:>4} | {x[0]:>12.6f} | {y[0]:>15.10f} | {'1':>6} | {y[0]:>18.10f}")

    for i in range(1, len(x) - 1):
        if i % 3 == 0:
            coef = 2
            suma += 2 * y[i]
        else:
            coef = 3
            suma += 3 * y[i]
        print(f"{i:>4} | {x[i]:>12.6f} | {y[i]:>15.10f} | {coef:>6} | {coef*y[i]:>18.10f}")

    suma += y[-1]
    print(f"{len(x)-1:>4} | {x[-1]:>12.6f} | {y[-1]:>15.10f} | {'1':>6} | {y[-1]:>18.10f}")

    resultado = (3 * h / 8) * suma

    print("─"*105)
    print(f"\n  I = (3h/8) × Suma = (3×{h}/8) × {suma:.10f} = {resultado:.10f}")
    print(f"\n{'RESULTADO: ' + f'{resultado:.10f}':^105}")
    print("="*105 + "\n")

    return resultado


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # ============================================================================
    # CÓMO USAR ESTE MÉTODO EN TU PARCIAL
    # ============================================================================
    #
    # 1. Define tu función o datos según el método
    # 2. Llama a la función correspondiente con los parámetros necesarios
    # 3. La respuesta se muestra automáticamente y se retorna
    #
    # Consulta el docstring de la función principal para ver ejemplos de uso
    # ============================================================================
    
    # Escribe tu código aquí:
    pass
