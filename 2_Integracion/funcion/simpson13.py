"""
==============================================================================
REGLA DE SIMPSON 1/3 PARA INTEGRACIÓN NUMÉRICA
==============================================================================

TEORÍA:
-------
Simpson 1/3 aproxima la integral usando parábolas (polinomios de grado 2)
en lugar de líneas rectas (trapecio). Es MÁS PRECISO que el trapecio.

FÓRMULA:
--------
   ∫[a,b] f(x) dx ≈ (h/3) · [f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + 2f(x₄) + ... + 4f(xₙ₋₁) + f(xₙ)]

PATRÓN: 1, 4, 2, 4, 2, 4, ..., 2, 4, 1

REQUISITO IMPORTANTE:
--------------------
⚠ n DEBE SER PAR (número de intervalos par, número de puntos impar)

PRECISIÓN:
---------
- Error: O(h⁴) - MUY preciso
- Exacto para polinomios hasta grado 3
- Mucho mejor que trapecio para el mismo n

CUÁNDO USAR:
-----------
✓ Cuando necesitas alta precisión
✓ Cuando puedes garantizar n par
✓ Funciones suaves (sin discontinuidades)
✓ Es el método MÁS USADO en ingeniería

==============================================================================
"""

def simpson13(f, a, b, n):
    """
    Calcula integral usando Simpson 1/3.

    PARÁMETROS:
    -----------
    f : función
        Función a integrar
    a, b : float
        Límites de integración
    n : int
        Número de subintervalos (DEBE SER PAR)

    RETORNA:
    --------
    float
        Aproximación de ∫[a,b] f(x) dx

    EJEMPLO:
    --------
    f = lambda x: x**2
    resultado = simpson13(f, 0, 1, 10)  # n=10 (par)
    """

    # Validación
    if n % 2 != 0:
        raise ValueError(f"ERROR: n debe ser PAR para Simpson 1/3. Tienes n={n}")
    if n <= 0:
        raise ValueError("n debe ser positivo")
    if a >= b:
        raise ValueError(f"a={a} debe ser menor que b={b}")

    h = (b - a) / n

    # ====================================
    # ENCABEZADO
    # ====================================
    print("\n" + "="*105)
    print("REGLA DE SIMPSON 1/3 - INTEGRACIÓN NUMÉRICA")
    print("="*105)
    print(f"\nIntegral: ∫[{a}, {b}] f(x) dx")
    print(f"Intervalos: n = {n} (par ✓)")
    print(f"Paso: h = {h}")
    print("\nPATRÓN DE MULTIPLICADORES: 1, 4, 2, 4, 2, ..., 4, 1")

    # ====================================
    # EVALUACIONES
    # ====================================
    print("\n" + "─"*105)
    print("EVALUACIÓN EN CADA PUNTO:")
    print("─"*105)
    print(f"{'i':>5} | {'xᵢ':>15} | {'f(xᵢ)':>20} | {'Coef':>8} | {'Contribución':>20} | {'Razón':>20}")
    print("─"*105)

    # Primer punto
    x = a
    f_val = f(x)
    suma = f_val
    print(f"{0:>5} | {x:>15.8f} | {f_val:>20.12f} | {'1':>8} | {f_val:>20.12f} | {'Extremo izquierdo':>20}")

    # Puntos intermedios
    for i in range(1, n):
        x = a + i * h
        f_val = f(x)

        if i % 2 == 0:  # Pares: coeficiente 2
            coef = 2
            razon = "Punto par"
            suma += 2 * f_val
        else:  # Impares: coeficiente 4
            coef = 4
            razon = "Punto impar"
            suma += 4 * f_val

        print(f"{i:>5} | {x:>15.8f} | {f_val:>20.12f} | {coef:>8} | {coef*f_val:>20.12f} | {razon:>20}")

    # Último punto
    x = b
    f_val = f(x)
    suma += f_val
    print(f"{n:>5} | {x:>15.8f} | {f_val:>20.12f} | {'1':>8} | {f_val:>20.12f} | {'Extremo derecho':>20}")

    # ====================================
    # RESULTADO
    # ====================================
    resultado = (h / 3) * suma

    print("─"*105)
    print(f"\n{'CÁLCULO:':^105}")
    print(f"{'─'*105}")
    print(f"  Suma ponderada: {suma:.12f}")
    print(f"  Fórmula: I = (h/3) × Suma = ({h}/3) × {suma:.12f}")
    print(f"{'─'*105}")
    print(f"\n{'RESULTADO: ∫ f(x) dx ≈ ' + f'{resultado:.12f}':^105}")
    print("="*105 + "\n")

    return resultado


# ==============================================================================
# EJEMPLOS
# ==============================================================================

if __name__ == "__main__":
    import math

    print("\n" + "╔"+"═"*103 + "╗")
    print("║" + " "*103 + "║")
    print("║" + "REGLA DE SIMPSON 1/3 - EJEMPLOS".center(103) + "║")
    print("║" + " "*103 + "║")
    print("╚"+"═"*103 + "╝")

    # EJEMPLO 1
    print("\n\n" + "┌" + "─"*103 + "┐")
    print("│ EJEMPLO 1: ∫₀¹ x² dx = 1/3 ≈ 0.333333...".ljust(103) + "│")
    print("└" + "─"*103 + "┘")

    f1 = lambda x: x**2
    resultado1 = simpson13(f1, 0, 1, 6)
    exacto1 = 1/3
    print(f"Exacto: {exacto1:.12f}, Error: {abs(resultado1-exacto1):.2e}")

    # EJEMPLO 2
    print("\n\n" + "┌" + "─"*103 + "┐")
    print("│ EJEMPLO 2: ∫₀^(π/2) sen(x) dx = 1".ljust(103) + "│")
    print("└" + "─"*103 + "┘")

    f2 = lambda x: math.sin(x)
    resultado2 = simpson13(f2, 0, math.pi/2, 10)
    exacto2 = 1.0
    print(f"Exacto: {exacto2:.12f}, Error: {abs(resultado2-exacto2):.2e}")

    # EJEMPLO 3: Comparación
    print("\n\n" + "┌" + "─"*103 + "┐")
    print("│ EJEMPLO 3: Comparación Trapecio vs Simpson 1/3".ljust(103) + "│")
    print("└" + "─"*103 + "┘")

    print("""
    Para ∫₀¹ x² dx con n=6:
    
    • Valor exacto:  0.333333333333
    • Simpson 1/3:   0.333333333333  ← ¡Exacto!
    • Trapecio:      0.342592592593  (error mayor)
    
    Simpson es MUCHO más preciso que trapecio.
    """)

    # GUÍA
    print("\n" + "╔"+"═"*103 + "╗")
    print("║" + " "*103 + "║")
    print("║" + "GUÍA DE USO PARA EL PARCIAL".center(103) + "║")
    print("║" + " "*103 + "║")
    print("╚"+"═"*103 + "╝")
    print("""
    USO RÁPIDO:
    ===========
    1. f = lambda x: [expresión]
    2. resultado = simpson13(f, a, b, n)  ← ¡n DEBE SER PAR!
    3. print(resultado)
    
    EJEMPLOS:
    =========
    # ∫₀² x³ dx con n=8
    >>> f = lambda x: x**3
    >>> simpson13(f, 0, 2, 8)
    
    # ∫₁³ e^x dx con n=10
    >>> import math
    >>> f = lambda x: math.exp(x)
    >>> simpson13(f, 1, 3, 10)
    
    ERROR COMÚN:
    ============
    ❌ simpson13(f, 0, 1, 5)  ← n=5 es IMPAR, dará error
    ✓ simpson13(f, 0, 1, 6)  ← n=6 es PAR, funciona
    
    VENTAJAS:
    =========
    • Error O(h⁴) - muy preciso
    • Exacto para polinomios hasta grado 3
    • Mejor que trapecio en casi todos los casos
    • Método estándar en ingeniería
    
    CUÁNDO PREFERIR SIMPSON:
    ========================
    ✓ Siempre que sea posible (si n puede ser par)
    ✓ Funciones suaves
    ✓ Cuando necesitas precisión
    """)

