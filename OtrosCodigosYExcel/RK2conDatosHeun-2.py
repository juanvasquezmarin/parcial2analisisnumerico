import pandas as pd

# === Leer los datos desde Excel ===
df = pd.read_excel("datos.xlsx")
x = df["x"].tolist()
y = df["y"].tolist()

print("Arreglo X:", x)
print("Arreglo Y:", y)

# === Método de Runge-Kutta 2 para datos tabulados ===
def runge_kutta2_datos(x, y):
    n = len(x)
    y_rk2 = [y[0]]
    for i in range(n - 1):
        h = x[i+1] - x[i]

        # Estimación de la pendiente en los nodos con diferencias finitas
        k1 = (y[i+1] - y[i]) / h
        # k2 usa el siguiente nodo, si está disponible:
        if i < n - 2:
            k2 = (y[i+2] - y[i+1]) / h
        else:
            k2 = k1  # al final, reutiliza k1
        
        y_next = y_rk2[-1] + (h/2) * (k1 + k2)
        y_rk2.append(y_next)

    return y_rk2

y_rk2 = runge_kutta2_datos(x, y)

# === Guardar los resultados en un Excel ===
df_resultados = pd.DataFrame({
    'x': x,
    'y': y,
    'y_rk2': y_rk2
})
df_resultados.to_excel('tabla_resultados_rk2_datos.xlsx', index=False)
print("Archivo 'tabla_resultados_rk2_datos.xlsx' generado correctamente.")