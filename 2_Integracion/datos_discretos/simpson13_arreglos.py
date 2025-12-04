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
