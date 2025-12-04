"""
==============================================================================
MÉTODO DE HEUN (EULER MEJORADO) PARA EDOs
==============================================================================

TEORÍA MATEMÁTICA:
-----------------
El método de Heun, también conocido como Euler Mejorado o Euler Modificado,
es un método predictor-corrector de segundo orden.

Dada una EDO: dy/dx = f(x, y) con condición inicial y(x₀) = y₀

El método usa dos evaluaciones de la función:

1. PREDICTOR (Euler simple):
   y*_{n+1} = y_n + h·f(x_n, y_n)

2. CORRECTOR (promedio de pendientes):
   y_{n+1} = y_n + (h/2)·[f(x_n, y_n) + f(x_{n+1}, y*_{n+1})]

Fórmula equivalente usando pendientes:
   m₁ = f(x_n, y_n)
   m₂ = f(x_n + h, y_n + h·m₁)
   y_{n+1} = y_n + (h/2)·(m₁ + m₂)

PRECISIÓN:
---------
- Error local: O(h³)
- Error global: O(h²)
- Es un método de orden 2 (más preciso que Euler)

CUÁNDO USAR:
-----------
✓ Cuando necesitas mejor precisión que Euler sin mucho costo computacional
✓ Es el equilibrio ideal entre simplicidad y precisión
✓ Bueno para la mayoría de problemas de EDOs en cursos básicos
✓ Método recomendado para parciales si no especifican cuál usar

COMPARACIÓN:
-----------
| Método  | Orden | Evaluaciones por paso | Precisión |
|---------|-------|----------------------|-----------|
| Euler   |   1   |          1           |    Baja   |
| Heun    |   2   |          2           |   Media   |
| RK4     |   4   |          4           |    Alta   |

==============================================================================
"""

def heun(f, x0, y0, h, n):
    """
    Resuelve una EDO usando el Método de Heun (Euler Mejorado).

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

    n  : int
         Número de pasos a realizar

    RETORNA:
    --------
    tuple (x_values, y_values)
        x_values : lista con todos los valores de x calculados
        y_values : lista con todos los valores de y calculados

    EJEMPLO DE USO:
    --------------
    # Resolver dy/dx = x + y, y(0) = 1, desde x=0 hasta x=0.5 con h=0.1

    f = lambda x, y: x + y
    x_vals, y_vals = heun(f, x0=0, y0=1, h=0.1, n=5)
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
    print("\n" + "="*100)
    print("MÉTODO DE HEUN (EULER MEJORADO) - SOLUCIÓN PASO A PASO")
    print("="*100)
    print(f"\nProblema: dy/dx = f(x, y)")
    print(f"Condición inicial: y({x0}) = {y0}")
    print(f"Tamaño del paso: h = {h}")
    print(f"Número de pasos: n = {n}")
    print(f"Valor final de x: x_final = {x0 + n*h}")
    print("\n" + "-"*100)
    print(f"{'Paso':>5} | {'x':>10} | {'y':>15} | {'m₁=f(xₙ,yₙ)':>15} | {'m₂=f(xₙ₊₁,y*)':>18} | {'Promedio':>15}")
    print("-"*100)

    # Paso inicial
    print(f"{0:>5} | {x:>10.6f} | {y:>15.10f} | {'(valor inicial)':>15} | {' ':>18} | {' ':>15}")

    # ====================================
    # ITERACIONES DEL MÉTODO
    # ====================================
    for i in range(n):
        # PASO 1: Calcular pendiente inicial m₁
        m1 = f(x, y)

        # PASO 2: Predicción de y usando Euler (y*)
        y_predictor = y + h * m1

        # PASO 3: Calcular pendiente en el punto predicho m₂
        x_next = x + h
        m2 = f(x_next, y_predictor)

        # PASO 4: Corrección - promedio de las dos pendientes
        m_promedio = (m1 + m2) / 2

        # PASO 5: Calcular y_{n+1} usando el promedio
        y_new = y + h * m_promedio

        # Guardar valores
        x_values.append(x_next)
        y_values.append(y_new)

        # Imprimir paso
        print(f"{i+1:>5} | {x_next:>10.6f} | {y_new:>15.10f} | {m1:>15.10f} | {m2:>18.10f} | {m_promedio:>15.10f}")

        # Actualizar para siguiente iteración
        x = x_next
        y = y_new

    # ====================================
    # RESUMEN FINAL
    # ====================================
    print("-"*100)
    print(f"\n{'SOLUCIÓN FINAL:':^100}")
    print(f"{'x = ' + f'{x:.10f}':^100}")
    print(f"{'y = ' + f'{y:.10f}':^100}")
    print("="*100 + "\n")

    return x_values, y_values


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # Ejemplo de uso del método de Heun
    # La función f y los parámetros deben definirse aquí
    f = lambda x, y: x + y  # Definir f en el main
    x_vals, y_vals = heun(f, x0=0, y0=1, h=0.1, n=5)
    print(f"Resultado final: y({x_vals[-1]}) = {y_vals[-1]}")
