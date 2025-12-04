import pandas as pd

# ==== Define aquí tu función de la EDO dy/dx = f(x, y) ====
def f(x, y):
    return x + y  # <-- Cambia esto por tu EDO

# ==== Condiciones iniciales y parámetros ====
x0 = 0     # Valor inicial de x
y0 = 1     # Valor inicial de y
xf = 1     # Valor final de x
h  = 0.1   # Tamaño del paso

# ==== Método de Runge-Kutta de 2º orden (Heun/Improved Euler) ====
def runge_kutta2(f, x0, y0, xf, h):
    xs = [x0]
    ys = [y0]
    n = int((xf - x0)/h)
    x = x0
    y = y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h*k1)
        y += (h/2) * (k1 + k2)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys

# ==== Ejecuta RK2 ====
x_vals, y_vals = runge_kutta2(f, x0, y0, xf, h)

# ==== Guarda resultados en Excel ====
df = pd.DataFrame({'x': x_vals, 'y': y_vals})
df.to_excel('tabla_resultados_funcion_rk2.xlsx', index=False)
print("Archivo 'tabla_resultados_funcion_rk2.xlsx' generado correctamente.")

# Opcional: imprimir en pantalla
for xi, yi in zip(x_vals, y_vals):
    print(f"x = {xi:.2f}, y = {yi:.6f}")