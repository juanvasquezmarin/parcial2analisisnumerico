import math

def simpson38(f, a, b, n):
    """
    Implementación del método de Simpson 3/8.
    
    Parámetros:
    f : función a integrar
    a : límite inferior
    b : límite superior
    n : número de subintervalos (debe ser múltiplo de 3)
    """
    if n % 3 != 0:
        raise ValueError("n debe ser múltiplo de 3 para Simpson 3/8")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            suma += 2 * f(x)
        else:
            suma += 3 * f(x)
            
    return (3 * h / 8) * suma

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: integral de x^2 de 0 a 1
    f = lambda x: x**2
    resultado = simpson38(f, 0, 1, 6)
    print(f"Resultado Simpson 3/8: {resultado}")
