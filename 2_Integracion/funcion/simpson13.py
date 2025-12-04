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
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # ============================================================================
    # CÓMO USAR ESTE MÉTODO EN TU PARCIAL
    # ============================================================================
    #
    # 1. Define tu función:
    #    f = lambda x: [tu_expresión]
    #
    # 2. Llama a la función (⚠️ n DEBE SER PAR):
    #    resultado = simpson13(f, a=límite_inferior, b=límite_superior, n=num_intervalos_par)
    #
    # 3. La respuesta se muestra automáticamente
    #
    # EJEMPLO:
    # f = lambda x: x**2
    # resultado = simpson13(f, a=0, b=1, n=10)  # n=10 es PAR ✓
    #
    # IMPORTANTE: n debe ser PAR (2, 4, 6, 8, 10, 12...)
    # ============================================================================

    # Escribe tu código aquí:
    pass

