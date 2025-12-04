"""
==============================================================================
REGLA DE SIMPSON 3/8 PARA INTEGRACIÓN NUMÉRICA
==============================================================================

TEORÍA:
-------
Simpson 3/8 es una variante de Simpson que usa intervalos de 3 subintervalos.
También usa aproximación parabólica pero con diferente distribución.

FÓRMULA:
--------
   ∫[a,b] f(x) dx ≈ (3h/8) · [f(x₀) + 3f(x₁) + 3f(x₂) + 2f(x₃) + 3f(x₄) + ... + f(xₙ)]

PATRÓN: 1, 3, 3, 2, 3, 3, 2, ..., 3, 3, 1

REQUISITO:
----------
⚠ n DEBE SER MÚLTIPLO DE 3

PRECISIÓN:
---------
- Error: O(h⁴) - igual que Simpson 1/3
- Ligeramente menos eficiente que Simpson 1/3
- Se usa cuando n debe ser múltiplo de 3

CUÁNDO USAR:
-----------
✓ Cuando n debe ser múltiplo de 3 por requisito del problema
✓ Para combinar con Simpson 1/3 en intervalos grandes
✗ Si puedes elegir, Simpson 1/3 es más eficiente

==============================================================================
"""

def simpson38(f, a, b, n):
    """
    Calcula integral usando Simpson 3/8.

    PARÁMETROS:
    -----------
    f : función
    a, b : float (límites)
    n : int (DEBE SER MÚLTIPLO DE 3)

    RETORNA:
    --------
    float - aproximación de la integral
    """

    if n % 3 != 0:
        raise ValueError(f"ERROR: n debe ser múltiplo de 3. Tienes n={n}")
    if n <= 0:
        raise ValueError("n debe ser positivo")
    if a >= b:
        raise ValueError(f"a={a} debe ser < b={b}")

    h = (b - a) / n

    print("\n" + "="*105)
    print("REGLA DE SIMPSON 3/8 - INTEGRACIÓN NUMÉRICA")
    print("="*105)
    print(f"\nIntegral: ∫[{a}, {b}] f(x) dx")
    print(f"Intervalos: n = {n} (múltiplo de 3 ✓)")
    print(f"Paso: h = {h}")
    print("\nPATRÓN: 1, 3, 3, 2, 3, 3, 2, ..., 3, 3, 1")

    print("\n" + "─"*105)
    print(f"{'i':>5} | {'xᵢ':>15} | {'f(xᵢ)':>20} | {'Coef':>8} | {'Contribución':>20} | {'Posición':>20}")
    print("─"*105)

    x = a
    f_val = f(x)
    suma = f_val
    print(f"{0:>5} | {x:>15.8f} | {f_val:>20.12f} | {'1':>8} | {f_val:>20.12f} | {'Inicio':>20}")

    for i in range(1, n):
        x = a + i * h
        f_val = f(x)

        if i % 3 == 0:
            coef = 2
            pos = "Múltiplo de 3"
            suma += 2 * f_val
        else:
            coef = 3
            pos = "No múltiplo de 3"
            suma += 3 * f_val

        print(f"{i:>5} | {x:>15.8f} | {f_val:>20.12f} | {coef:>8} | {coef*f_val:>20.12f} | {pos:>20}")

    x = b
    f_val = f(x)
    suma += f_val
    print(f"{n:>5} | {x:>15.8f} | {f_val:>20.12f} | {'1':>8} | {f_val:>20.12f} | {'Final':>20}")

    resultado = (3 * h / 8) * suma

    print("─"*105)
    print(f"\n  Suma: {suma:.12f}")
    print(f"  I = (3h/8) × Suma = (3×{h}/8) × {suma:.12f}")
    print(f"\n{'RESULTADO: ' + f'{resultado:.12f}':^105}")
    print("="*105 + "\n")

    return resultado


if __name__ == "__main__":
    # Define la función f y los parámetros aquí
    f = lambda x: x**2  # Ejemplo: función f(x)
    a, b = 0, 1  # Límites de integración
    n = 6  # Número de subintervalos (múltiplo de 3)
    resultado = simpson38(f, a, b, n)
    print(f"Resultado: {resultado}")
