import math

def trapecio(f, a, b, n):
    """
    Implementación del método del Trapecio.
    
    Parámetros:
    f : función a integrar
    a : límite inferior
    b : límite superior
    n : número de subintervalos
    """
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        suma += 2 * f(x)
            
    return (h / 2) * suma

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: integral de x^2 de 0 a 1
    f = lambda x: x**2
    resultado = trapecio(f, 0, 1, 6)
    print(f"Resultado Trapecio: {resultado}")
