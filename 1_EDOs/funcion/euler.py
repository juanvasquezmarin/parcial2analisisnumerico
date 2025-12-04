"""
==============================================================================
MÉTODO DE EULER PARA ECUACIONES DIFERENCIALES ORDINARIAS (EDOs)
==============================================================================

TEORÍA MATEMÁTICA:
-----------------
El método de Euler es el método numérico más simple para resolver EDOs de
primer orden con un valor inicial (Problema de Valor Inicial - PVI).

Dada una EDO: dy/dx = f(x, y) con condición inicial y(x₀) = y₀

El método de Euler aproxima la solución usando la recta tangente:
    y_{n+1} = y_n + h·f(x_n, y_n)

donde:
    - h es el tamaño del paso
    - x_{n+1} = x_n + h
    - f(x_n, y_n) es la pendiente en el punto (x_n, y_n)

PRECISIÓN:
---------
- Error local: O(h²)
- Error global: O(h)
- Es un método de orden 1

CUÁNDO USAR:
-----------
✓ Cuando necesitas una solución rápida y aproximada
✓ Para problemas simples donde la precisión no es crítica
✓ Como primera aproximación antes de usar métodos más precisos
✗ NO usar para problemas rígidos (stiff problems)
✗ NO usar cuando necesitas alta precisión con pasos grandes

==============================================================================
"""

def euler(f, x0, y0, h, n):
    """
    Resuelve una EDO usando el Método de Euler.

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
         Mientras más pequeño h, más preciso pero más cálculos

    n  : int
         Número de pasos a realizar
         El valor final de x será: x_final = x₀ + n·h

    RETORNA:
    --------
    tuple (x_values, y_values)
        x_values : lista con todos los valores de x calculados
        y_values : lista con todos los valores de y calculados

    EJEMPLO DE USO:
    --------------
    # Resolver dy/dx = x + y, y(0) = 1, desde x=0 hasta x=0.5 con paso h=0.1

    f = lambda x, y: x + y
    x_vals, y_vals = euler(f, x0=0, y0=1, h=0.1, n=5)

    # Resultado final
    print(f"Solución en x = {x_vals[-1]}: y = {y_vals[-1]}")
    """

    # Listas para almacenar todos los valores calculados
    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    # ====================================
    # ENCABEZADO DE LA TABLA DE RESULTADOS
    # ====================================
    print("\n" + "="*80)
    print("MÉTODO DE EULER - SOLUCIÓN PASO A PASO")
    print("="*80)
    print(f"\nProblema: dy/dx = f(x, y)")
    print(f"Condición inicial: y({x0}) = {y0}")
    print(f"Tamaño del paso: h = {h}")
    print(f"Número de pasos: n = {n}")
    print(f"Valor final de x: x_final = {x0 + n*h}")
    print("\n" + "-"*80)
    print(f"{'Paso':>6} | {'x':>12} | {'y':>15} | {'f(x,y)':>15} | {'h·f(x,y)':>15}")
    print("-"*80)

    # Paso inicial
    f_val = f(x, y)
    print(f"{0:>6} | {x:>12.6f} | {y:>15.10f} | {f_val:>15.10f} | {'(inicial)':>15}")

    # ====================================
    # ITERACIONES DEL MÉTODO DE EULER
    # ====================================
    for i in range(n):
        # Calcular la derivada en el punto actual
        f_val = f(x, y)

        # Incremento en y
        dy = h * f_val

        # Calcular nuevo valor de y usando la fórmula de Euler
        y_new = y + dy

        # Calcular nuevo valor de x
        x_new = x + h

        # Guardar valores
        x_values.append(x_new)
        y_values.append(y_new)

        # Imprimir paso actual
        print(f"{i+1:>6} | {x_new:>12.6f} | {y_new:>15.10f} | {f_val:>15.10f} | {dy:>15.10f}")

        # Actualizar para el siguiente paso
        x = x_new
        y = y_new

    # ====================================
    # RESUMEN FINAL
    # ====================================
    print("-"*80)
    print(f"\n{'SOLUCIÓN FINAL:':^80}")
    print(f"{'x = ' + str(x):^80}")
    print(f"{'y = ' + str(y):^80}")
    print("="*80 + "\n")

    return x_values, y_values


# ==============================================================================
# EJEMPLOS DE USO
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "╔"+"═"*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "EJEMPLOS DE USO DEL MÉTODO DE EULER".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚"+"═"*78 + "╝")

    # ========================================
    # EJEMPLO 1: dy/dx = x + y, y(0) = 1
    # ========================================
    print("\n\n" + "┌" + "─"*78 + "┐")
    print("│ EJEMPLO 1: dy/dx = x + y con y(0) = 1".ljust(78) + "│")
    print("└" + "─"*78 + "┘")

    # Definir la función derivada
    f1 = lambda x, y: x + y

    # Resolver
    x_vals, y_vals = euler(f1, x0=0, y0=1, h=0.1, n=5)

    # ========================================
    # EJEMPLO 2: dy/dx = -2xy², y(0) = 1
    # ========================================
    print("\n\n" + "┌" + "─"*78 + "┐")
    print("│ EJEMPLO 2: dy/dx = -2xy² con y(0) = 1".ljust(78) + "│")
    print("└" + "─"*78 + "┘")

    f2 = lambda x, y: -2 * x * y**2

    x_vals2, y_vals2 = euler(f2, x0=0, y0=1, h=0.1, n=5)

    # ========================================
    # CÓMO MODIFICAR PARA TU PROBLEMA
    # ========================================
    print("\n\n" + "╔"+"═"*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "CÓMO USAR PARA TU PROBLEMA DEL PARCIAL".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚"+"═"*78 + "╝")
    print("""
    1. Define tu función derivada f(x, y):
       f = lambda x, y: [tu ecuación aquí]
    
    2. Identifica tus condiciones iniciales:
       x0 = [valor inicial de x]
       y0 = [valor inicial de y]
    
    3. Determina el paso h y cuántos pasos necesitas:
       h = [tamaño del paso]
       n = [número de pasos]
    
    4. Llama a la función:
       x_vals, y_vals = euler(f, x0, y0, h, n)
    
    5. El último valor es tu respuesta:
       print(f"Solución: y({x_vals[-1]}) = {y_vals[-1]}")
    
    EJEMPLO COMPLETO:
    ----------------
    # Si te dan: dy/dx = 3x - 2y, y(1) = 2, calcula y(1.5) con h=0.1
    
    f = lambda x, y: 3*x - 2*y
    x_vals, y_vals = euler(f, x0=1, y0=2, h=0.1, n=5)
    print(f"Respuesta: y(1.5) = {y_vals[-1]}")
    """)

