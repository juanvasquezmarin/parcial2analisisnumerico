import math

def simpson13(f, a, b, n):
    """
    Implementación del método de Simpson 1/3.
    
    Parámetros:
    f : función a integrar
    a : límite inferior
    b : límite superior
    n : número de subintervalos (debe ser par)
    """
    if n % 2 != 0:
        raise ValueError("n debe ser par para Simpson 1/3")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)
            
    return (h / 3) * suma

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: integral de x^2 de 0 a 1
    f = lambda x: x**2
    resultado = simpson13(f, 0, 1, 6)
    print(f"Resultado Simpson 1/3: {resultado}")
