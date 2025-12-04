"""
==============================================================================
MÉTODO DE HEUN (TRAPECIO) PARA RECONSTRUIR y DESDE DATOS DISCRETOS DE dy/dx
==============================================================================

TEORÍA MATEMÁTICA:
-----------------
El método de Heun con datos discretos también se conoce como REGLA DEL TRAPECIO
para resolver EDOs, porque usa el promedio de las derivadas en ambos extremos.

FÓRMULA:
--------
   y[i+1] = y[i] + (h/2) · (dy[i] + dy[i+1])

Donde:
   • h = x[i+1] - x[i]
   • dy[i] = derivada en el punto izquierdo
   • dy[i+1] = derivada en el punto derecho
   • El promedio (dy[i] + dy[i+1])/2 mejora la precisión

INTERPRETACIÓN GEOMÉTRICA:
-------------------------
En lugar de usar solo la pendiente del punto inicial (Euler),
usa el PROMEDIO de las pendientes en ambos extremos del intervalo.

┌─────────────────────────────────────┐
│ Euler:  usa dy[i]                   │
│ Heun:   usa (dy[i] + dy[i+1]) / 2   │
└─────────────────────────────────────┘

PRECISIÓN:
---------
- Error: O(h²) - orden 2
- MÁS PRECISO que Euler para el mismo h
- Requiere conocer dy en ambos extremos del intervalo

DIFERENCIA CON EULER:
--------------------
┌────────┬─────────────────────────┬──────────────────────┐
│ Método │ Fórmula                 │ Precisión            │
├────────┼─────────────────────────┼──────────────────────┤
│ Euler  │ y[i+1] = y[i] + h·dy[i] │ O(h) - menos preciso │
│ Heun   │ y[i+1] = y[i] + (h/2)·  │ O(h²) - más preciso  │
│        │          (dy[i]+dy[i+1])│                      │
└────────┴─────────────────────���───┴──────────────────────┘

CUÁNDO USAR:
-----------
✓ Cuando te dan datos discretos de dy/dx
✓ Cuando necesitas mejor precisión que Euler
✓ Cuando tienes valores de dy en TODOS los puntos (incluyendo extremos)

==============================================================================
"""

def heun_arreglos(x, dy, y0):
    """
    Reconstruye y desde datos discretos de dy/dx usando Heun (Trapecio).

    PARÁMETROS:
    -----------
    x  : list
         Valores de x (ordenados)

    dy : list
         Valores de dy/dx en cada punto x
         DEBE tener la misma longitud que x

    y0 : float
         Valor inicial y(x[0]) = y0

    RETORNA:
    --------
    list
         Valores de y calculados en cada punto x

    EJEMPLO:
    --------
    x = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    dy = [0, 0.4, 0.8, 1.2, 1.6, 2.0]
    y = heun_arreglos(x, dy, y0=0)
    """

    # Validación
    if len(x) != len(dy):
        raise ValueError(f"ERROR: x ({len(x)} elementos) y dy ({len(dy)} elementos) deben tener igual longitud.")

    if len(x) < 2:
        raise ValueError("ERROR: Se necesitan al menos 2 puntos.")

    n = len(x)
    y = [0.0] * n
    y[0] = y0

    # ====================================
    # ENCABEZADO
    # ====================================
    print("\n" + "="*110)
    print("MÉTODO DE HEUN (TRAPECIO) CON DATOS DISCRETOS")
    print("="*110)
    print(f"\nDatos: {n} puntos desde x = {x[0]} hasta x = {x[-1]}")
    print(f"Condición inicial: y({x[0]}) = {y0}")
    print("\nFórmula: y[i+1] = y[i] + (h/2)·(dy[i] + dy[i+1])")

    # ====================================
    # TABLA DE DATOS
    # ====================================
    print("\n" + "─"*110)
    print("DATOS DE ENTRADA:")
    print("─"*110)
    print(f"{'i':>4} | {'x':>10} | {'dy/dx':>15}")
    print("─"*110)
    for i in range(n):
        print(f"{i:>4} | {x[i]:>10.6f} | {dy[i]:>15.10f}")

    # ====================================
    # CÁLCULO
    # ====================================
    print("\n" + "─"*110)
    print("CÁLCULO PASO A PASO:")
    print("─"*110)
    print(f"{'Paso':>4} | {'x[i]':>10} | {'x[i+1]':>10} | {'h':>8} | {'dy[i]':>12} | {'dy[i+1]':>12} | {'Promedio':>12} | {'y[i+1]':>15}")
    print("─"*110)

    for i in range(n - 1):
        h = x[i+1] - x[i]

        # Promedio de las dos derivadas
        dy_promedio = (dy[i] + dy[i+1]) / 2

        # Fórmula de Heun/Trapecio
        y[i+1] = y[i] + h * dy_promedio

        print(f"{i+1:>4} | {x[i]:>10.4f} | {x[i+1]:>10.4f} | {h:>8.4f} | {dy[i]:>12.6f} | {dy[i+1]:>12.6f} | {dy_promedio:>12.6f} | {y[i+1]:>15.10f}")

    # ====================================
    # RESULTADOS
    # ====================================
    print("─"*110)
    print("\n" + "="*110)
    print("RESULTADOS FINALES:")
    print("="*110)
    print(f"{'x':>15} | {'dy/dx (dato)':>20} | {'y (calculado)':>25}")
    print("─"*110)
    for i in range(n):
        print(f"{x[i]:>15.6f} | {dy[i]:>20.10f} | {y[i]:>25.10f}")
    print("="*110)

    print(f"\n{'RESPUESTA FINAL: y(' + str(x[-1]) + ') = ' + str(y[-1]):^110}")
    print("="*110 + "\n")

    return y


# ==============================================================================
# USO DEL ARCHIVO
# ==============================================================================

if __name__ == "__main__":
    # Ejemplo de uso del método Heun con arreglos
    # Los datos x_datos, dy_datos y y0 deben definirse aquí
    x_datos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]  # Definir datos en el main
    dy_datos = [0, 0.4, 0.8, 1.2, 1.6, 2.0]
    y_resultado = heun_arreglos(x_datos, dy_datos, y0=0)
    print(f"Resultado final: y({x_datos[-1]}) = {y_resultado[-1]}")

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
