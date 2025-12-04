def trapecio_datos(x, y):
    """
    Implementación del método del Trapecio para datos discretos (arreglos).
    
    Parámetros:
    x : arreglo de valores de x (debe estar ordenado)
    y : arreglo de valores de y correspondientes a x
    """
    n = len(x)
    if len(y) != n:
        raise ValueError("Los arreglos x e y deben tener la misma longitud")
    
    suma = 0
    
    for i in range(n - 1):
        # Área del trapecio entre x[i] y x[i+1]
        # Área = (base_mayor + base_menor) * altura / 2
        # altura = x[i+1] - x[i]
        # bases = y[i] y y[i+1]
        area_trapecio = (y[i] + y[i+1]) * (x[i+1] - x[i]) / 2
        suma += area_trapecio
            
    return suma

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: Datos discretos
    x_datos = [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84]
    y_datos = [0.02, 0.077, 0.206, 0.431, 0.766, 1.163, 1.559, 1.907, 2.18, 2.377, 2.511, 2.604, 2.67] # y = x^2
    
    resultado = trapecio_datos(x_datos, y_datos)
    print(f"Datos x: {x_datos}")
    print(f"Datos y: {y_datos}")
    print(f"Resultado Trapecio (datos discretos): {resultado}")
