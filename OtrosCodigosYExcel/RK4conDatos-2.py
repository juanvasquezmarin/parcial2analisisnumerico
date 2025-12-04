import pandas as pd

# === Leer los datos desde Excel ===
df = pd.read_excel("datos.xlsx")
x = df["x"].tolist()
y = df["y"].tolist()

print("Arreglo X:", x)
print("Arreglo Y:", y)

# === Métodos de derivación ===
def derivarFD(y2, y3, y4, h):
    return (-y4 + 4*y3 - 3*y2)/(2*h)

def derivarCD(y1, y3, h):
    return (y3 - y1)/(2*h)

def derivarBD(y2, y1, y0, h):
    return (3*y2 - 4*y1 + y0)/(2*h)

def hallarDerivadas(x, y):
    h = x[1] - x[0]
    n = len(y)
    arrDerivada = []
    for i in range(n):
        if i == 0:  
            arrDerivada.append(derivarFD(y[i], y[i+1], y[i+2], h))
        elif i == n-1:
            arrDerivada.append(derivarBD(y[i], y[i-1], y[i-2], h))
        else:
            arrDerivada.append(derivarCD(y[i-1], y[i+1], h))
    return arrDerivada

primerDerivada = hallarDerivadas(x, y)
segundaDerivada = hallarDerivadas(x, primerDerivada)
tercerDerivada = hallarDerivadas(x, segundaDerivada)
cuartaDerivada = hallarDerivadas(x, tercerDerivada)

# === Método de Runge-Kutta 4 adaptado a datos tabulados ===
def runge_kutta4_datos(x, y):
    n = len(x)
    y_rk4 = [y[0]]
    for i in range(n-1):
        h = x[i+1] - x[i]
        
        # Estimación de la derivada (f(x, y)) en puntos necesarios por RK4:
        # Se hace con forward/central/backward dependiendo de la posición
        
        # k1 = f(x_i, y_i)
        if i == 0:
            k1 = derivarFD(y[i], y[i+1], y[i+2], h)
        elif i == n-2:
            k1 = derivarBD(y[i], y[i-1], y[i-2], h)
        else:
            k1 = derivarCD(y[i-1], y[i+1], h)
        
        # Para k2 y k3, usamos valores intermedios: x_i + h/2
        # Usamos aproximaciones de y:
        y_half1 = y[i] + 0.5*h*k1
        
        # k2 = f(x_i + h/2, y_half1)
        # Buscamos el índice cercano al punto medio o usamos la pendiente local
        if i < n-2:
            k2 = (y[i+1] - y[i]) / h  # forward diff como aproximación
        else:
            k2 = (y[i] - y[i-1]) / h  # backward diff al final
        
        y_half2 = y[i] + 0.5*h*k2
        
        # k3 = f(x_i + h/2, y_half2)
        if i < n-2:
            k3 = (y[i+1] - y[i]) / h
        else:
            k3 = (y[i] - y[i-1]) / h
        
        y_end = y[i] + h*k3
        
        # k4 = f(x_i + h, y_end)
        if i < n-2:
            k4 = (y[i+2] - y[i+1]) / h
        else:
            k4 = (y[i+1] - y[i]) / h
        
        # Cálculo final
        y_next = y_rk4[-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        y_rk4.append(y_next)
    
    return y_rk4

y_rk4 = runge_kutta4_datos(x, y)

# === Guardar todos los resultados juntos en un nuevo Excel ===
df_resultados = pd.DataFrame({
    'x': x,
    'y': y,
    'primerDerivada': primerDerivada,
    'segundaDerivada': segundaDerivada,
    'tercerDerivada': tercerDerivada,
    'cuartaDerivada': cuartaDerivada,
    'y_rk4': y_rk4
})

df_resultados.to_excel('tabla_resultados_rk4.xlsx', index=False)
print("Archivo 'tabla_resultados_rk4.xlsx' generado correctamente.")