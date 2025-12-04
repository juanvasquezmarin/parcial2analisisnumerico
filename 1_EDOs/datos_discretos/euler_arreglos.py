"""
==============================================================================
MÉTODO DE EULER PARA RECONSTRUIR y DESDE DATOS DISCRETOS DE dy/dx
==============================================================================

TEORÍA MATEMÁTICA:
-----------------
Este método se usa cuando NO tienes una función f(x, y), sino DATOS DISCRETOS
de la derivada dy/dx en puntos específicos.

PROBLEMA TÍPICO:
"Te dan una tabla con valores de x y dy/dx. Encuentra y usando el método de Euler."

┌─────────────────────────────────────────────────────────────┐
│  x  │ 0.0 │ 0.2 │ 0.4 │ 0.6 │ 0.8 │ 1.0 │                  │
│─────┼─────┼─────┼─────┼─────┼─────┼─────┤                  │
│dy/dx│ 0.0 │ 0.4 │ 0.8 │ 1.2 │ 1.6 │ 2.0 │                  │
└─────────────────────────────────────────────────────────────┘

MÉTODO:
-------
Euler usa la derivada del punto ACTUAL para avanzar:

   y[i+1] = y[i] + h · dy/dx[i]

donde h = x[i+1] - x[i]

DIFERENCIA CON EULER NORMAL:
----------------------------
• Euler normal: evalúas f(x, y) en cada paso
• Euler con datos: usas directamente el valor de dy/dx de la tabla

PRECISIÓN:
---------
- Error: O(h) (orden 1) - igual que Euler normal
- Limitado por la precisión de los datos proporcionados

CUÁNDO USAR:
-----------
✓ Cuando te dan TABLAS de datos discretos
✓ Cuando NO tienes una función explícita f(x, y)
✓ Datos experimentales o mediciones
✓ El profesor te da un Excel o tabla de valores

==============================================================================
"""

def euler_arreglos(x, dy, y0):
    """
    Reconstruye y a partir de datos discretos de dy/dx usando el Método de Euler.

    PARÁMETROS:
    -----------
    x  : list o array
         Lista de valores de x (deben estar ordenados)
         Ejemplo: x = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

    dy : list o array
         Lista de valores de la derivada dy/dx en cada punto x
         Debe tener la MISMA LONGITUD que x
         Ejemplo: dy = [0, 0.4, 0.8, 1.2, 1.6, 2.0]

    y0 : float
         Valor inicial de y en x[0]
         Es la condición inicial: y(x[0]) = y0

    RETORNA:
    --------
    list
         Lista de valores de y calculados en cada punto x

    EJEMPLO DE USO:
    --------------
    # Datos de la tabla
    x_datos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    dy_datos = [0, 0.4, 0.8, 1.2, 1.6, 2.0]

    # Calcular y con condición inicial y(0) = 0
    y_resultado = euler_arreglos(x_datos, dy_datos, y0=0)

    # Ver resultado final
    print(f"y(1.0) = {y_resultado[-1]}")
    """

    # Validación
    if len(x) != len(dy):
        raise ValueError(f"ERROR: x tiene {len(x)} elementos pero dy tiene {len(dy)} elementos. Deben ser iguales.")

    if len(x) < 2:
        raise ValueError("ERROR: Se necesitan al menos 2 puntos de datos.")

    n = len(x)
    y = [0.0] * n  # Inicializar lista para y
    y[0] = y0      # Condición inicial

    # ====================================
    # ENCABEZADO
    # ====================================
    print("\n" + "="*95)
    print("MÉTODO DE EULER CON DATOS DISCRETOS - RECONSTRUCCIÓN DE y DESDE dy/dx")
    print("="*95)
    print(f"\nDatos proporcionados: {n} puntos")
    print(f"Condición inicial: y({x[0]}) = {y0}")
    print(f"Rango: x ∈ [{x[0]}, {x[-1]}]")

    # Mostrar datos de entrada
    print("\n" + "─"*95)
    print("DATOS DE ENTRADA:")
    print("─"*95)
    print(f"{'Índice':>7} | {'x':>12} | {'dy/dx (dado)':>20}")
    print("─"*95)
    for i in range(n):
        print(f"{i:>7} | {x[i]:>12.6f} | {dy[i]:>20.10f}")

    # ====================================
    # CÁLCULO CON EULER
    # ====================================
    print("\n" + "─"*95)
    print("CÁLCULO PASO A PASO:")
    print("─"*95)
    print(f"{'Paso':>5} | {'x[i]':>10} | {'x[i+1]':>10} | {'h':>10} | {'dy/dx[i]':>12} | {'y[i]':>15} | {'y[i+1]':>15}")
    print("─"*95)

    # Paso inicial
    print(f"{'0':>5} | {x[0]:>10.4f} | {'-':>10} | {'-':>10} | {dy[0]:>12.6f} | {y[0]:>15.10f} | {'(inicial)':>15}")

    # Aplicar Euler para cada intervalo
    for i in range(n - 1):
        # Calcular tamaño del paso (puede ser variable)
        h = x[i+1] - x[i]

        # Fórmula de Euler: y[i+1] = y[i] + h * dy[i]
        y[i+1] = y[i] + h * dy[i]

        # Mostrar paso
        print(f"{i+1:>5} | {x[i]:>10.4f} | {x[i+1]:>10.4f} | {h:>10.4f} | {dy[i]:>12.6f} | {y[i]:>15.10f} | {y[i+1]:>15.10f}")

    # ====================================
    # RESUMEN FINAL
    # ====================================
    print("─"*95)
    print("\n" + "="*95)
    print("TABLA DE RESULTADOS FINALES:")
    print("="*95)
    print(f"{'x':>15} | {'dy/dx (dato)':>20} | {'y (calculado)':>25}")
    print("─"*95)
    for i in range(n):
        print(f"{x[i]:>15.6f} | {dy[i]:>20.10f} | {y[i]:>25.10f}")
    print("="*95)

    print(f"\n{'SOLUCIÓN FINAL:':^95}")
    print(f"{'y(' + str(x[-1]) + ') = ' + str(y[-1]):^95}")
    print("="*95 + "\n")

    return y


# ==============================================================================
# EJEMPLOS DE USO
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "╔"+"═"*93 + "╗")
    print("║" + " "*93 + "║")
    print("║" + "EJEMPLOS DE USO - EULER CON DATOS DISCRETOS".center(93) + "║")
    print("║" + " "*93 + "║")
    print("╚"+"═"*93 + "╝")

    # ========================================
    # EJEMPLO 1: Derivada lineal dy/dx = 2x
    # ========================================
    print("\n\n" + "┌" + "─"*93 + "┐")
    print("│ EJEMPLO 1: Datos de dy/dx = 2x, y(0) = 0".ljust(93) + "│")
    print("│ (Solución exacta: y = x²)".ljust(93) + "│")
    print("└" + "─"*93 + "┘")

    x_datos1 = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    dy_datos1 = [0, 0.4, 0.8, 1.2, 1.6, 2.0]  # dy/dx = 2x

    y_resultado1 = euler_arreglos(x_datos1, dy_datos1, y0=0)

    # Comparar con solución exacta
    print(f"\nComparación con solución exacta y = x²:")
    print(f"  y_numérica(1.0) = {y_resultado1[-1]:.6f}")
    print(f"  y_exacta(1.0)   = {1.0**2:.6f}")
    print(f"  Error           = {abs(y_resultado1[-1] - 1.0):.6f}")

    # ========================================
    # EJEMPLO 2: Paso variable
    # ========================================
    print("\n\n" + "┌" + "─"*93 + "┐")
    print("│ EJEMPLO 2: Datos con paso variable (no uniforme)".ljust(93) + "│")
    print("└" + "─"*93 + "┘")

    x_datos2 = [0, 0.1, 0.3, 0.7, 1.0]  # Pasos: 0.1, 0.2, 0.4, 0.3
    dy_datos2 = [1, 1.2, 1.6, 2.4, 3.0]

    y_resultado2 = euler_arreglos(x_datos2, dy_datos2, y0=2)

    # ========================================
    # GUÍA DE USO PARA EL PARCIAL
    # ========================================
    print("\n\n" + "╔"+"═"*93 + "╗")
    print("║" + " "*93 + "║")
    print("║" + "GUÍA PARA USAR EN TU PARCIAL".center(93) + "║")
    print("║" + " "*93 + "║")
    print("╚"+"═"*93 + "╝")
    print("""
    ┌───────────────────────────────────────────────────────────────────────────────────────────┐
    │ SITUACIÓN: Te dan una TABLA con valores de x y dy/dx                                     │
    └───────────────────────────────────────────────────────────────────────────────────────────┘
    
    PASOS A SEGUIR:
    ===============
    
    1. TRANSCRIBIR los datos de la tabla a listas de Python:
    
       x_datos = [x₀, x₁, x₂, ..., xₙ]
       dy_datos = [dy₀, dy₁, dy₂, ..., dyₙ]
    
    2. IDENTIFICAR la condición inicial y₀:
       • Busca en el problema: "y(x₀) = ..." 
       • Si no está explícita, suele ser y₀ = 0
    
    3. EJECUTAR el método:
    
       y_resultado = euler_arreglos(x_datos, dy_datos, y0=y₀)
    
    4. OBTENER la respuesta:
       • Si preguntan por y en el último punto: y_resultado[-1]
       • Si preguntan por y en un punto intermedio: y_resultado[índice]
    
    
    EJEMPLO COMPLETO DEL PARCIAL:
    =============================
    
    PROBLEMA:
    "Dada la siguiente tabla de datos y la condición inicial y(0) = 1,
     use el método de Euler para calcular y(0.6):"
    
    ┌───────┬──────┬──────┬──────┬──────┐
    │   x   │ 0.0  │ 0.2  │ 0.4  │ 0.6  │
    ├───────┼──────┼──────┼──────┼──────┤
    │ dy/dx │ 1.0  │ 1.5  │ 2.0  │ 2.5  │
    └───────┴──────┴──────┴──────┴──────┘
    
    SOLUCIÓN:
    
    >>> x_datos = [0.0, 0.2, 0.4, 0.6]
    >>> dy_datos = [1.0, 1.5, 2.0, 2.5]
    >>> y_resultado = euler_arreglos(x_datos, dy_datos, y0=1)
    >>> print(f"RESPUESTA: y(0.6) = {y_resultado[-1]}")
    
    
    TIPS IMPORTANTES:
    =================
    • Los arreglos x y dy DEBEN tener la misma longitud
    • El orden de los datos importa (deben estar ordenados por x creciente)
    • Si el paso h no es constante, ¡no hay problema! El método lo maneja automáticamente
    • Puedes copiar los datos directo del Excel/tabla del examen
    
    
    ERRORES COMUNES A EVITAR:
    =========================
    ❌ NO confundir dy (derivada) con y (función)
    ❌ NO olvidar la condición inicial y0
    ❌ NO usar dy[i+1] en lugar de dy[i] en la fórmula de Euler
    ✓ Euler usa la derivada del punto ACTUAL (izquierdo)
    """)

