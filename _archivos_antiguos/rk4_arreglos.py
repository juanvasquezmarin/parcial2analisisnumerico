def rk4_arreglos(x, dy, y0):
    """
    Implementación del método RK4 para datos discretos.
    Para aplicar RK4 a datos discretos (y' = f(x)), necesitamos el valor de la derivada
    en el punto medio del intervalo. Por lo tanto, este método avanza saltando un índice
    (toma pasos de 2*h usando x[i], x[i+1] como medio, x[i+2]).
    
    Parámetros:
    x  : arreglo de valores de x (debe tener espaciamiento constante)
    dy : arreglo de valores de la derivada dy/dx en los puntos x
    y0 : valor inicial de y en x[0]
    
    Retorna:
    x_res : arreglo de x donde se calculó y (subconjunto del original)
    y_res : arreglo de valores calculados de y
    """
    n = len(x)
    if n < 3 or n % 2 == 0:
        # Necesitamos al menos 3 puntos y un número impar de puntos para tener intervalos pares
        # Si no es así, se podría ajustar, pero para este ejemplo estricto:
        print("Advertencia: RK4 con arreglos requiere número impar de puntos para usar pasos completos.")
    
    y_res = [y0]
    x_res = [x[0]]
    
    y_actual = y0
    
    # Avanzamos de 2 en 2
    for i in range(0, n - 2, 2):
        h_step = x[i+1] - x[i] # Paso simple
        h_total = x[i+2] - x[i] # Paso completo del RK4 (2*h)
        
        # RK4 para y' = f(x):
        # k1 = f(x_i)          = dy[i]
        # k2 = f(x_i + H/2)    = dy[i+1]
        # k3 = f(x_i + H/2)    = dy[i+1]
        # k4 = f(x_i + H)      = dy[i+2]
        
        k1 = dy[i]
        k2 = dy[i+1]
        k3 = dy[i+1]
        k4 = dy[i+2]
        
        # y_{n+1} = y_n + (H/6) * (k1 + 2k2 + 2k3 + k4)
        # H = 2 * h_step
        
        y_next = y_actual + (h_total / 6) * (k1 + 2*k2 + 2*k3 + k4)
        
        y_res.append(y_next)
        x_res.append(x[i+2])
        y_actual = y_next
        
    return x_res, y_res

# Ejemplo de uso
if __name__ == "__main__":
    # Derivada dy/dx = 2x, y(0) = 0 -> Solución exacta y = x^2
    # Usamos puntos suficientes
    x_datos = [0, 0.1, 0.2, 0.3, 0.4] # Paso 0.1, RK4 avanzará 0.2
    dy_datos = [0, 0.2, 0.4, 0.6, 0.8]
    
    x_out, y_out = rk4_arreglos(x_datos, dy_datos, 0)
    print("RK4 Arreglos (saltando de a 2 puntos):")
    for xi, yi in zip(x_out, y_out):
        print(f"x: {xi:.2f}, y: {yi:.4f}")
