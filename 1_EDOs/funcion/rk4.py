"""
==============================================================================
MÉTODO DE RUNGE-KUTTA DE 4TO ORDEN (RK4) PARA EDOs
==============================================================================

TEORÍA MATEMÁTICA:
-----------------
El método de Runge-Kutta de 4to orden (RK4) es el método numérico más popular
y ampliamente usado para resolver EDOs debido a su excelente balance entre
precisión y costo computacional.

Dada una EDO: dy/dx = f(x, y) con condición inicial y(x₀) = y₀

El método RK4 calcula 4 pendientes en cada paso:

   k₁ = f(xₙ, yₙ)                        ← Pendiente al inicio del intervalo
   k₂ = f(xₙ + h/2, yₙ + (h/2)·k₁)       ← Pendiente en el punto medio (método 1)
   k₃ = f(xₙ + h/2, yₙ + (h/2)·k₂)       ← Pendiente en el punto medio (método 2)
   k₄ = f(xₙ + h, yₙ + h·k₃)             ← Pendiente al final del intervalo

Luego calcula un promedio ponderado:
   yₙ₊₁ = yₙ + (h/6)·(k₁ + 2k₂ + 2k₃ + k₄)

Los pesos 1:2:2:1 dan más importancia a las pendientes en el punto medio.

INTERPRETACIÓN GEOMÉTRICA:
-------------------------
- k₁: Pendiente al inicio
- k₂: Pendiente en el medio usando k₁
- k₃: Pendiente en el medio usando k₂ (refinamiento)
- k₄: Pendiente al final usando k₃
- El promedio ponderado da una aproximación muy precisa

PRECISIÓN:
---------
- Error local: O(h⁵)
- Error global: O(h⁴)
- Es un método de orden 4 (MUY PRECISO)

CUÁNDO USAR:
-----------
✓ Cuando necesitas alta precisión
✓ Cuando puedes permitirte 4 evaluaciones de f por paso
✓ Es el método estándar en aplicaciones científicas e ingenieriles
✓ Problemas donde la solución tiene cambios suaves

COMPARACIÓN DE MÉTODOS:
----------------------
┌─────────┬───────┬──────────────┬────────────┬─────────────────┐
│ Método  │ Orden │ Evaluaciones │ Error O(h) │ Recomendación   │
├─────────┼───────┼──────────────┼────────────┼─────────────────┤
│ Euler   │   1   │      1       │     h      │ Solo ejemplos   │
│ Heun    │   2   │      2       │     h²     │ Bueno/rápido    │
│ RK4     │   4   │      4       │     h⁴     │ Mejor precisión │
└─────────┴───────┴──────────────┴────────────┴─────────────────┘

==============================================================================
"""

def rk4(f, x0, y0, h, n):
    """
    Resuelve una EDO usando el Método de Runge-Kutta de 4to Orden (RK4).

    PARÁMETROS:
    -----------
    f  : función
         La derivada dy/dx = f(x, y)
         Ejemplo: f = lambda x, y: x + y

    x0 : float
         Valor inicial de x (punto de partida)

    y0 : float
         Valor inicial de y en x₀, es decir y(x₀) = y₀

    h  : float
         Tamaño del paso (incremento en x)
         Con RK4 puedes usar pasos más grandes que con Euler

    n  : int
         Número de pasos a realizar
         El valor final será: x_final = x₀ + n·h

    RETORNA:
    --------
    tuple (x_values, y_values)
        x_values : lista con todos los valores de x calculados
        y_values : lista con todos los valores de y calculados

    EJEMPLO DE USO:
    --------------
    # Resolver dy/dx = x + y, y(0) = 1, desde x=0 hasta x=0.5 con h=0.1

    f = lambda x, y: x + y
    x_vals, y_vals = rk4(f, x0=0, y0=1, h=0.1, n=5)
    print(f"Solución: y({x_vals[-1]}) = {y_vals[-1]}")
    """

    # Listas para almacenar resultados
    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    # ====================================
    # ENCABEZADO
    # ====================================
    print("\n" + "="*120)
    print("MÉTODO DE RUNGE-KUTTA DE 4TO ORDEN (RK4) - SOLUCIÓN PASO A PASO")
    print("="*120)
    print(f"\nProblema: dy/dx = f(x, y)")
    print(f"Condición inicial: y({x0}) = {y0}")
    print(f"Tamaño del paso: h = {h}")
    print(f"Número de pasos: n = {n}")
    print(f"Valor final de x: x_final = {x0 + n*h}")
    print("\n" + "-"*120)
    print(f"{'Paso':>5} | {'x':>10} | {'y':>15} | {'k₁':>13} | {'k₂':>13} | {'k₃':>13} | {'k₄':>13} | {'Promedio':>13}")
    print("-"*120)

    print(f"{0:>5} | {x:>10.6f} | {y:>15.10f} | {'(condición inicial)':^13} | {' ':>13} | {' ':>13} | {' ':>13} | {' ':>13}")

    # ====================================
    # ITERACIONES DEL MÉTODO RK4
    # ====================================
    for i in range(n):
        # PASO 1: Calcular k₁ (pendiente al inicio)
        k1 = f(x, y)

        # PASO 2: Calcular k₂ (pendiente en el punto medio usando k₁)
        k2 = f(x + 0.5*h, y + 0.5*h*k1)

        # PASO 3: Calcular k₃ (pendiente en el punto medio usando k₂)
        k3 = f(x + 0.5*h, y + 0.5*h*k2)

        # PASO 4: Calcular k₄ (pendiente al final usando k₃)
        k4 = f(x + h, y + h*k3)

        # PASO 5: Calcular promedio ponderado de las pendientes
        # Pesos: k₁(1/6) + k₂(2/6) + k₃(2/6) + k₄(1/6)
        k_promedio = (k1 + 2*k2 + 2*k3 + k4) / 6

        # PASO 6: Calcular nuevo valor de y
        y_new = y + h * k_promedio

        x_next = x + h

        # Guardar resultados
        x_values.append(x_next)
        y_values.append(y_new)

        # Mostrar paso con todas las k's
        print(f"{i+1:>5} | {x_next:>10.6f} | {y_new:>15.10f} | {k1:>13.8f} | {k2:>13.8f} | {k3:>13.8f} | {k4:>13.8f} | {k_promedio:>13.8f}")

        # Actualizar para siguiente iteración
        x = x_next
        y = y_new

    # ====================================
    # RESUMEN FINAL
    # ====================================
    print("-"*120)
    print(f"\n{'SOLUCIÓN FINAL:':^120}")
    print(f"{'x = ' + f'{x:.10f}':^120}")
    print(f"{'y = ' + f'{y:.10f}':^120}")
    print("="*120 + "\n")

    return x_values, y_values


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # Ejemplo de uso del método RK4
    # La función f y los parámetros deben definirse aquí
    f = lambda x, y: x + y  # Definir f en el main
    x_vals, y_vals = rk4(f, x0=0, y0=1, h=0.1, n=5)
    print(f"Resultado final: y({x_vals[-1]}) = {y_vals[-1]}")
