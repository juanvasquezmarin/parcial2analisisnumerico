def euler(f, x0, y0, h, n):
    """
    Implementación del método de Euler.
    
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
        y = y + h * f(x, y)
        x = x + h
        print(f"x{i+1} = {x:.4f}, y{i+1} = {y:.4f}")
        
    return y

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: dy/dx = x + y, y(0) = 1
    f = lambda x, y: x + y
    euler(f, 0, 1, 0.1, 5)
