def rk2_arreglos(x, dy, y0):
    """
    Implementación del método RK2 para datos discretos.
    Para datos donde la derivada solo depende de x, RK2 es equivalente a Heun/Trapecio.
    
    Parámetros:
    x  : arreglo de valores de x
    dy : arreglo de valores de la derivada dy/dx en los puntos x
    y0 : valor inicial de y en x[0]
    
    Retorna:
    y : arreglo de valores calculados de y
    """
    # Reutilizamos la lógica de Heun ya que matemáticamente son equivalentes para y' = f(x)
    n = len(x)
    y = [0.0] * n
    y[0] = y0
    
    for i in range(n - 1):
        h = x[i+1] - x[i]
        # RK2 (Heun): y_{i+1} = y_i + (h/2) * (k1 + k2)
        # k1 = f(x_i) = dy[i]
        # k2 = f(x_{i+1}) = dy[i+1]
        y[i+1] = y[i] + (h / 2) * (dy[i] + dy[i+1])
        
    return y

# Ejemplo de uso
if __name__ == "__main__":
    x_datos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    dy_datos = [0, 0.4, 0.8, 1.2, 1.6, 2.0]
    
    y_res = rk2_arreglos(x_datos, dy_datos, 0)
    print("RK2 Arreglos:")
    for xi, yi in zip(x_datos, y_res):
        print(f"x: {xi:.2f}, y: {yi:.4f}")
