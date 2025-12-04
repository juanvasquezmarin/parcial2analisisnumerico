import pandas as pd

# === Lectura de datos ===
df = pd.read_excel("datos.xlsx")
x = df["x"].tolist()
y = df["y"].tolist()

print("Arreglo X:", x)
print("Arreglo Y:", y)

# === Algoritmos de derivadas ===
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

# === Simpson 1/3 para área bajo la curva ===
def calcularSimp13(fx0, fx1, fx2, a, b):
    return ((fx0 + 4*fx1 + fx2) / 6) * (b - a)

def verificarIntervalos(x, y, n):
    r = ((len(x) - 1) / n) + 1
    if r >= 3 and r % 2 != 0:
        return True
    else:
        return False

def hallarAreaSimp13(x, y, n):
    if verificarIntervalos(x, y, n):
        r = int(((len(x) - 1) / n))
        a = 0
        p = int(r // 2)
        resultado = 0
        for i in range(0, n):
            resultado += calcularSimp13(y[a], y[a+p], y[a+2*p], x[a], x[a+2*p])
            a += 2*p
        return resultado
    else:
        print(f"El conjunto de datos no se puede dividir en {n} intervalos")
        return None

# === Cálculo del área con Simpson 1/3 ===
n_intervalos = 2  # Cambia esto si necesitas más/menos intervalos
area = hallarAreaSimp13(x, y, n_intervalos)
print(f"Área aproximada bajo la curva (Simpson 1/3, n={n_intervalos}): {area}")

# === Guardar resultados en Excel incluyendo el valor del área ===
df_derivadas = pd.DataFrame({
    'x': x,
    'y': y,
    'primerDerivada': primerDerivada,
    'segundaDerivada': segundaDerivada,
    'tercerDerivada': tercerDerivada,
    'cuartaDerivada': cuartaDerivada
})

# Agrega una fila con el área en la columna y (las demás celdas vacías)
area_row = {
    'x': 'Área_Simpson13',
    'y': area,
    'primerDerivada': None,
    'segundaDerivada': None,
    'tercerDerivada': None,
    'cuartaDerivada': None
}
df_derivadas = pd.concat([df_derivadas, pd.DataFrame([area_row])], ignore_index=True)

df_derivadas.to_excel('tabla_derivadas_simpson13.xlsx', index=False)
print("Archivo 'tabla_derivadas_simpson13.xlsx' generado correctamente, con el área incluida al final.")