"""
    """)
    ✓ 5 puntos → 4 intervalos (PAR) → OK
    ❌ 4 puntos → 3 intervalos (IMPAR) → Error
    ============
    ERROR COMÚN:

    resultado = simpson13_arreglos(x, y)
    y = [1, 2, 5, 10, 17, 26, 37]
    x = [0, 1, 2, 3, 4, 5, 6]
    Tabla con 7 puntos:
    ====================
    EJEMPLO DEL PARCIAL:

    • Si tienes 7 puntos → 6 intervalos (PAR ✓)
    • Si tienes 5 puntos → 4 intervalos (PAR ✓)
    • Espaciamiento: CONSTANTE
    • Número de puntos: IMPAR (3, 5, 7, 9, ...)
    ===========
    REQUISITOS:

    resultado = simpson13_arreglos(x, y)
    y = [...]
    x = [...]  # número IMPAR de puntos
    ====
    USO:
    print("""
    print("╚" + "═"*103 + "╝")
    print("║" + "GUÍA".center(103) + "║")
    print("\n╔" + "═"*103 + "╗")
    
    print(f"Exacto: {exacto:.10f}, Error: {abs(resultado-exacto):.2e}")
    exacto = 1/3
    resultado = simpson13_arreglos(x, y)
    
    y = [0.0, 0.0625, 0.25, 0.5625, 1.0]
    x = [0.0, 0.25, 0.5, 0.75, 1.0]
    
    print("└" + "─"*103 + "┘")
    print("│ EJEMPLO: Datos de y = x² con 5 puntos (4 intervalos = PAR ✓)".ljust(103) + "│")
    print("\n┌" + "─"*103 + "┐")
    
    print("╚" + "═"*103 + "╝")
    print("║" + "SIMPSON 1/3 CON DATOS - EJEMPLOS".center(103) + "║")
    print("\n╔" + "═"*103 + "╗")
if __name__ == "__main__":


    return resultado
    
    print("="*105 + "\n")
    print(f"\n{'RESULTADO: ' + f'{resultado:.10f}':^105}")
    print(f"\n  I = (h/3) × Suma = ({h}/3) × {suma:.10f} = {resultado:.10f}")
    print("─"*105)
    
    resultado = (h / 3) * suma
    
    print(f"{len(x)-1:>4} | {x[-1]:>12.6f} | {y[-1]:>15.10f} | {'1':>6} | {y[-1]:>18.10f}")
    suma += y[-1]
    
        print(f"{i:>4} | {x[i]:>12.6f} | {y[i]:>15.10f} | {coef:>6} | {coef*y[i]:>18.10f}")
            suma += 4 * y[i]
            coef = 4
        else:
            suma += 2 * y[i]
            coef = 2
        if i % 2 == 0:
    for i in range(1, len(x) - 1):
    
    print(f"{0:>4} | {x[0]:>12.6f} | {y[0]:>15.10f} | {'1':>6} | {y[0]:>18.10f}")
    suma = y[0]
    
    print("─"*105)
    print(f"{'i':>4} | {'x':>12} | {'y':>15} | {'Coef':>6} | {'Contribución':>18}")
    print("\n" + "─"*105)
    
    print(f"Rango: [{x[0]}, {x[-1]}]")
    print(f"Espaciamiento: h ≈ {h:.6f}")
    print(f"\nPuntos: {len(x)} (intervalos: {n_intervalos}, PAR ✓)")
    print("="*105)
    print("SIMPSON 1/3 CON DATOS DISCRETOS")
    print("\n" + "="*105)
    
            print(f"ADVERTENCIA: Espaciamiento no constante en intervalo {i}")
        if abs(h_actual - h) > 1e-6:
        h_actual = x[i+1] - x[i]
    for i in range(len(x) - 1):
    # Verificar espaciamiento constante
    
    h = x[1] - x[0]
    # Calcular h (asumiendo espaciamiento constante)
    
        raise ValueError("Se necesitan al menos 3 puntos")
    if len(x) < 3:
    
        raise ValueError(f"Número de intervalos debe ser PAR. Tienes {n_intervalos} intervalos ({len(x)} puntos)")
    if n_intervalos % 2 != 0:
    n_intervalos = len(x) - 1
    
        raise ValueError(f"x y y deben tener igual longitud")
    if len(x) != len(y):
    
    """
    float - aproximación integral
    --------
    RETORNA:

    x, y : lists (misma longitud, número impar de puntos)
    -----------
    PARÁMETROS:

    Simpson 1/3 con datos discretos.
    """
def simpson13_arreglos(x, y):

"""
==============================================================================

PATRÓN: 1, 4, 2, 4, 2, ..., 4, 1

⚠ Espaciamiento h debe ser CONSTANTE
⚠ Número de intervalos (n-1) debe ser PAR
-----------
REQUISITOS:

   I ≈ (h/3) × [y₀ + 4y₁ + 2y₂ + 4y₃ + ... + 4yₙ₋₁ + yₙ]
--------
FÓRMULA:

número de intervalos PAR.
Simpson 1/3 con datos discretos. Requiere espaciamiento CONSTANTE y
-------
TEORÍA:

==============================================================================
SIMPSON 1/3 PARA DATOS DISCRETOS
==============================================================================

