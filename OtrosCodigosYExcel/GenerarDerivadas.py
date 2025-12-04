import pandas as pd

# Hay que asegurarse que las x esten separadas de forma uniforme
# y que ambos arreglos tengan el mismo tamaño

# Leer el Excel
df = pd.read_excel("datos.xlsx")

# Convertir cada columna en un arreglo (lista)
x = df["x"].tolist()
y = df["y"].tolist()

print("Arreglo X:", x)
print("Arreglo Y:", y)


# Algoritmo para generar la tabla de derivadas de los datos ingresados

# deriva usando la formula de forward difference f'(x) = (y(i+1) - y(i))/h
# donde h es la distancia en x entre y(i) e y(i+1)
def derivarFD(y2, y3, y4, h):
    return (-y4 + 4*y3 - 3*y2)/(2*h)

# derivar con central difference para mayor precision en los datos intermedios
def derivarCD(y1, y3, h):
    return (y3 - y1)/(2*h)

# derivar backward difference de segundo orden para los ultimos datos
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


df = pd.DataFrame({
    'x': x,
    'y': y,
    'primerDerivada': primerDerivada,
    'segundaDerivada': segundaDerivada,
    'tercerDerivada': tercerDerivada,
    'cuartaDerivada': cuartaDerivada
})

# Guardar a Excel
df.to_excel('tabla_derivadas.xlsx', index=False)

print("Archivo 'tabla_derivadas.xlsx' generado correctamente.")
