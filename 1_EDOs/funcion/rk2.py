"""
==============================================================================
MÉTODO DE RUNGE-KUTTA DE 2DO ORDEN (RK2) PARA EDOs
==============================================================================

TEORÍA MATEMÁTICA:
-----------------
El método de Runge-Kutta de 2do orden (RK2) es una familia de métodos que
incluye al método de Heun. La versión clásica de RK2 usa el punto medio.

Dada una EDO: dy/dx = f(x, y) con condición inicial y(x₀) = y₀

VERSIÓN PUNTO MEDIO (Midpoint Method):
   k₁ = f(x_n, y_n)
   k₂ = f(x_n + h/2, y_n + (h/2)·k₁)
   y_{n+1} = y_n + h·k₂

VERSIÓN HEUN (implementada aquí por compatibilidad):
   k₁ = f(x_n, y_n)
   k₂ = f(x_n + h, y_n + h·k₁)
   y_{n+1} = y_n + (h/2)·(k₁ + k₂)

Ambas versiones son de orden 2 pero dan resultados ligeramente diferentes.

PRECISIÓN:
---------
- Error local: O(h³)
- Error global: O(h²)
- Es un método de orden 2

CUÁNDO USAR:
-----------
✓ Cuando el profesor específicamente pide RK2
✓ Alternativa equivalente a Heun en la mayoría de casos
✓ Cuando necesitas un método de orden 2

NOTA: En la práctica, Heun y RK2 se usan indistintamente en cursos básicos.

==============================================================================
"""

def rk2(f, x0, y0, h, n):
    """
    Resuelve una EDO usando el Método de Runge-Kutta de 2do Orden (RK2).

    PARÁMETROS:
    -----------
    f  : función
         La derivada dy/dx = f(x, y)
         Ejemplo: f = lambda x, y: x + y

    x0 : float
         Valor inicial de x

    y0 : float
         Valor inicial de y en x₀

    h  : float
         Tamaño del paso

    n  : int
         Número de pasos a realizar

    RETORNA:
    --------
    tuple (x_values, y_values)
        x_values : lista con valores de x
        y_values : lista con valores de y

    EJEMPLO DE USO:
    --------------
    f = lambda x, y: x + y
    x_vals, y_vals = rk2(f, x0=0, y0=1, h=0.1, n=5)
    """

    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    # ====================================
    # ENCABEZADO
    # ====================================
    print("\n" + "="*100)
    print("MÉTODO DE RUNGE-KUTTA DE 2DO ORDEN (RK2) - SOLUCIÓN PASO A PASO")
    print("="*100)
    print(f"\nProblema: dy/dx = f(x, y)")
    print(f"Condición inicial: y({x0}) = {y0}")
    print(f"Tamaño del paso: h = {h}")
    print(f"Número de pasos: n = {n}")
    print(f"Valor final de x: x_final = {x0 + n*h}")
    print("\n" + "-"*100)
    print(f"{'Paso':>5} | {'x':>10} | {'y':>15} | {'k₁':>15} | {'k₂':>15} | {'(k₁+k₂)/2':>15}")
    print("-"*100)

    print(f"{0:>5} | {x:>10.6f} | {y:>15.10f} | {'(valor inicial)':>15} | {' ':>15} | {' ':>15}")

    # ====================================
    # ITERACIONES
    # ====================================
    for i in range(n):
        # Paso 1: Calcular k₁ en el punto actual
        k1 = f(x, y)

        # Paso 2: Calcular k₂ en el punto final del intervalo
        k2 = f(x + h, y + h * k1)

        # Paso 3: Calcular nuevo y usando promedio de k₁ y k₂
        k_promedio = (k1 + k2) / 2
        y_new = y + h * k_promedio

        x_next = x + h

        # Guardar resultados
        x_values.append(x_next)
        y_values.append(y_new)

        # Mostrar paso
        print(f"{i+1:>5} | {x_next:>10.6f} | {y_new:>15.10f} | {k1:>15.10f} | {k2:>15.10f} | {k_promedio:>15.10f}")

        # Actualizar
        x = x_next
        y = y_new

    # ====================================
    # RESUMEN
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
