def rk2(f, x0, y0, h, n):
    """
    Implementación del método de Runge-Kutta de 2do Orden (RK2).
    Este es equivalente al método de Heun, pero estructurado como RK.
    
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
        k2 = f(x + h, y + h * k1)
        
        y = y + (h / 2) * (k1 + k2)
        x = x + h
        print(f"x{i+1} = {x:.4f}, y{i+1} = {y:.4f}")
        
    return y

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: dy/dx = x + y, y(0) = 1
    f = lambda x, y: x + y
    rk2(f, 0, 1, 0.1, 5)
