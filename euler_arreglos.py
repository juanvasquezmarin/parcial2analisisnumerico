def euler_arreglos(x, dy, y0):
    """
    Implementación del método de Euler para reconstruir y a partir de su derivada dy (datos).
    
    Parámetros:
    x  : arreglo de valores de x
    dy : arreglo de valores de la derivada dy/dx en los puntos x
    y0 : valor inicial de y en x[0]
    
    Retorna:
    y : arreglo de valores calculados de y
    """
    n = len(x)
    y = [0.0] * n
    y[0] = y0
    
    for i in range(n - 1):
        h = x[i+1] - x[i]
        # Euler: y_{i+1} = y_i + h * f(x_i, y_i)
        # Aquí f(x_i, y_i) es simplemente dy[i]
        y[i+1] = y[i] + h * dy[i]
        
    return y

# Ejemplo de uso
if __name__ == "__main__":
    # Derivada dy/dx = 2x, y(0) = 0 -> Solución exacta y = x^2
    x_datos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    dy_datos = [0, 0.4, 0.8, 1.2, 1.6, 2.0] # 2*x
    
    y_res = euler_arreglos(x_datos, dy_datos, 0)
    print("Euler Arreglos:")
    for xi, yi in zip(x_datos, y_res):
        print(f"x: {xi:.2f}, y: {yi:.4f}")
