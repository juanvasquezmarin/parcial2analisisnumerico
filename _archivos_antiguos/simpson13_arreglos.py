def simpson13_arreglos(x, y):
    """
    Implementación del método de Simpson 1/3 para datos discretos.
    
    Parámetros:
    x : arreglo de valores de x (debe tener espaciamiento constante)
    y : arreglo de valores de y correspondientes a x
    """
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("El número de intervalos debe ser par (número de puntos impar) para Simpson 1/3")
    
    # Calculamos h asumiendo espaciamiento constante
    h = x[1] - x[0]
    
    suma = y[0] + y[-1]
    
    for i in range(1, n):
        if i % 2 == 0:
            suma += 2 * y[i]
        else:
            suma += 4 * y[i]
            
    return (h / 3) * suma

# Ejemplo de uso
if __name__ == "__main__":
    # Datos para y = x^2 en [0, 1] con n=4 (5 puntos)
    x_datos = [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84]
    y_datos = [0.02, 0.077, 0.206, 0.431, 0.766, 1.163, 1.559, 1.907, 2.18, 2.377, 2.511, 2.604, 2.67] # y = x^2
    
    
    resultado = simpson13_arreglos(x_datos, y_datos)
    print(f"Resultado Simpson 1/3 (arreglos): {resultado}")
