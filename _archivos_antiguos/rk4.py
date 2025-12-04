def rk4(f, x0, y0, h, n):
    """
    Implementación del método de Runge-Kutta de 4to Orden (RK4).
    
    Parámetros:
    f  : función derivada dy/dx = f(x, y)
    x0 : valor inicial de x
    y0 : valor inicial de y
    h  : tamaño del paso
    n  : número de pasos
    """
    x = x0
    y = y0
    
    print(f"x0 = {x}, y0 = {y}")
    
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + 0.5 * h, y + 0.5 * h * k1)
        k3 = f(x + 0.5 * h, y + 0.5 * h * k2)
        k4 = f(x + h, y + h * k3)
        
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h
        print(f"x{i+1} = {x:.4f}, y{i+1} = {y:.4f}")
        
    return y

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: dy/dx = x + y, y(0) = 1
    f = lambda x, y: x + y
    rk4(f, 0, 1, 0.1, 5)
