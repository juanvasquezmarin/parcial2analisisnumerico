import pandas as pd

# === Lectura del archivo Excel ===
df = pd.read_excel("datos.xlsx")
x = df["x"].tolist()
y = df["y"].tolist()

print("Arreglo X:", x)
print("Arreglo Y:", y)

# === Algoritmo de derivadas ===
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
        if i == 0:  # primer punto -> forward
            arrDerivada.append(derivarFD(y[i], y[i+1], y[i+2], h))
        elif i == n-1:  # último punto -> backward
            arrDerivada.append(derivarBD(y[i], y[i-1], y[i-2], h))
        else:  # puntos internos -> central
            arrDerivada.append(derivarCD(y[i-1], y[i+1], h))
    return arrDerivada

primerDerivada = hallarDerivadas(x, y)
segundaDerivada = hallarDerivadas(x, primerDerivada)
tercerDerivada = hallarDerivadas(x, segundaDerivada)
cuartaDerivada = hallarDerivadas(x, tercerDerivada)

# === Algoritmo del método de Euler ===
def metodo_euler_datos(x, y):
    y_euler = [y[0]]
    for i in range(len(x) - 1):
        h = x[i+1] - x[i]
        pendiente = (y[i+1] - y[i]) / h
        y_euler_siguiente = y_euler[-1] + h * pendiente
        y_euler.append(y_euler_siguiente)
    return y_euler

y_euler = metodo_euler_datos(x, y)

# === Guardar TODOS los resultados juntos en un nuevo Excel ===
df_resultados = pd.DataFrame({
    'x': x,
    'y': y,
    'primerDerivada': primerDerivada,
    'segundaDerivada': segundaDerivada,
    'tercerDerivada': tercerDerivada,
    'cuartaDerivada': cuartaDerivada,
    'y_euler': y_euler
})
df_resultados.to_excel('tabla_euler.xlsx', index=False)

print("Archivo 'tabla_euler.xlsx' generado correctamente.")