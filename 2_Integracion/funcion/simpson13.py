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
        raise ValueError("ERROR: n debe ser PAR para Simpson 1/3.")
    if n <= 0:
        raise ValueError("n debe ser positivo.")
    if a >= b:
        raise ValueError("El límite inferior a debe ser menor que b.")

    h = (b - a) / n

    # Evaluación inicial
    x = a
    suma = f(x)  # f(x₀)

    print("\n" + "="*80)
    print("PROCEDIMIENTO - SIMPSON 1/3")
    print("="*80)
    print(f"{'i':>5} | {'xᵢ':>10} | {'f(xᵢ)':>15} | {'Coef':>10} | {'Contribución':>15}")
    print("-"*80)

    # Puntos intermedios
    for i in range(1, n):
        x = a + i * h
        coef = 4 if i % 2 != 0 else 2  # Alterna entre 4 y 2
        contrib = coef * f(x)
        suma += contrib
        print(f"{i:>5} | {x:>10.4f} | {f(x):>15.4f} | {coef:>10} | {contrib:>15.4f}")
    x = b
    print(f"{n:>5} | {x:>10.4f} | {f(x):>15.4f} | {'1':>10} | {f(x):>15.4f}")
    suma += f(x)

    # Resultado final
    resultado = (h / 3) * suma
    print("-"*80)
    print(f"Suma total: {suma:.4f}")
    print(f"Resultado final: I = (h/3) * Suma = ({h}/3) * {suma:.4f} = {resultado:.4f}")
    print("="*80 + "\n")
    return resultado


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # Define la función f y los parámetros aquí
    f = lambda x: x**2  # Ejemplo: función f(x)
    a, b = 0, 1  # Límites de integración
    n = 10  # Número de subintervalos (par)
    resultado = simpson13(f, a, b, n)
    print(f"Resultado: {resultado}")

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
