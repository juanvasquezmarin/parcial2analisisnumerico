"""
==============================================================================
REGLA DEL TRAPECIO PARA INTEGRACIÓN NUMÉRICA
==============================================================================

TEORÍA MATEMÁTICA:
-----------------
La Regla del Trapecio aproxima la integral de una función usando trapecios
en lugar de rectángulos.

PROBLEMA: Calcular ∫[a,b] f(x) dx

MÉTODO:
-------
Divide el intervalo [a, b] en n subintervalos de ancho h = (b-a)/n
y aproxima el área bajo la curva usando trapecios:

   ∫[a,b] f(x) dx ≈ (h/2) · [f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]

Fórmula simplificada:
   I ≈ (h/2) · [f(a) + f(b) + 2·Σf(xᵢ)]  para i = 1 hasta n-1

INTERPRETACIÓN GEOMÉTRICA:
-------------------------
Cada trapecio tiene:
   • Bases: f(xᵢ) y f(xᵢ₊₁)
   • Altura: h = xᵢ₊₁ - xᵢ
   • Área = (h/2)·(f(xᵢ) + f(xᵢ₊₁))

PRECISIÓN:
---------
- Error: O(h²) para cada intervalo
- Error global: O(h²)
- Más preciso que rectángulos, menos que Simpson

CUÁNDO USAR:
-----------
✓ Método simple y rápido
✓ Funciona bien para funciones suaves
✓ Buena opción cuando n es grande
✓ Cuando te dan una función f(x) explícita

COMPARACIÓN:
-----------
┌──────────┬───────┬──────────────────────────────────┐
│ Método   │ Orden │ Cuándo es exacto                 │
├──────────┼───────┼──────────────────────────────────┤
│ Trapecio │  O(h²)│ Funciones lineales               │
│ Simpson  │  O(h⁴)│ Polinomios hasta grado 3         │
└──────────┴───────┴──────────────────────────────────┘

==============================================================================
"""

def trapecio(f, a, b, n):
    """
    Calcula la integral definida usando la Regla del Trapecio.

    PARÁMETROS:
    -----------
    f : función
        Función a integrar f(x)
        Ejemplo: f = lambda x: x**2

    a : float
        Límite inferior de integración

    b : float
        Límite superior de integración

    n : int
        Número de subintervalos (trapecios)
        Mientras más grande n, más preciso el resultado

    RETORNA:
    --------
    float
        Aproximación de la integral ∫[a,b] f(x) dx

    EJEMPLO:
    --------
    # Calcular ∫[0,1] x² dx con 10 subintervalos
    f = lambda x: x**2
    resultado = trapecio(f, a=0, b=1, n=10)
    print(f"∫₀¹ x² dx ≈ {resultado}")  # Resultado exacto: 1/3 ≈ 0.333...
    """

    # Validación
    if n <= 0:
        raise ValueError("El número de subintervalos n debe ser positivo")
    if a >= b:
        raise ValueError(f"El límite inferior a={a} debe ser menor que b={b}")

    # Calcular tamaño del paso
    h = (b - a) / n

    # ====================================
    # ENCABEZADO
    # ====================================
    print("\n" + "="*100)
    print("REGLA DEL TRAPECIO - INTEGRACIÓN NUMÉRICA")
    print("="*100)
    print(f"\nIntegral: ∫[{a}, {b}] f(x) dx")
    print(f"Número de subintervalos: n = {n}")
    print(f"Ancho de cada subintervalo: h = (b-a)/n = ({b}-{a})/{n} = {h}")

    # ====================================
    # EVALUACIÓN EN LOS PUNTOS
    # ====================================
    print("\n" + "─"*100)
    print("EVALUACIÓN DE LA FUNCIÓN EN LOS PUNTOS:")
    print("─"*100)
    print(f"{'i':>5} | {'xᵢ':>15} | {'f(xᵢ)':>20} | {'Multiplicador':>15} | {'Contribución':>20}")
    print("─"*100)

    # Primer punto (extremo izquierdo)
    x = a
    f_val = f(x)
    suma = f_val
    print(f"{0:>5} | {x:>15.8f} | {f_val:>20.12f} | {'×1 (extremo)':>15} | {f_val:>20.12f}")

    # Puntos intermedios
    for i in range(1, n):
        x = a + i * h
        f_val = f(x)
        suma += 2 * f_val
        print(f"{i:>5} | {x:>15.8f} | {f_val:>20.12f} | {'×2 (interior)':>15} | {2*f_val:>20.12f}")

    # Último punto (extremo derecho)
    x = b
    f_val = f(x)
    suma += f_val
    print(f"{n:>5} | {x:>15.8f} | {f_val:>20.12f} | {'×1 (extremo)':>15} | {f_val:>20.12f}")

    # ====================================
    # CÁLCULO FINAL
    # ====================================
    resultado = (h / 2) * suma

    print("─"*100)
    print(f"\n{'CÁLCULO FINAL:':^100}")
    print(f"{'─'*100}")
    print(f"  Suma total de contribuciones: {suma:.12f}")
    print(f"  Fórmula: I = (h/2) × Suma")
    print(f"  I = ({h}/2) × {suma:.12f}")
    print(f"  I = {h/2:.12f} × {suma:.12f}")
    print(f"{'─'*100}")
    print(f"\n{'RESULTADO: ∫[' + str(a) + ', ' + str(b) + '] f(x) dx ≈ ' + f'{resultado:.12f}':^100}")
    print("="*100 + "\n")

    return resultado


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # Define la función f y los parámetros aquí
    f = lambda x: x**2  # Ejemplo: función f(x)
    a, b = 0, 1  # Límites de integración
    n = 10  # Número de subintervalos
    resultado = trapecio(f, a, b, n)
    print(f"Resultado: {resultado}")
