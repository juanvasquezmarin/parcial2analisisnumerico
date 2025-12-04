import pandas as pd

# ==== Define aquí tu función de la EDO dy/dx = f(x, y) ====
def f(x, y):
    return x + y  # <-- Cambia esto por tu ecuación

# ==== Condiciones iniciales y parámetros ====
x0 = 0      # Valor inicial de x
y0 = 1      # Valor inicial de y
xf = 2      # Valor final de x
h  = 0.1    # Paso

# ==== Método de Runge-Kutta de 4to orden ====
def runge_kutta4(f, x0, y0, xf, h):
    xs = [x0]
    ys = [y0]
    n = int((xf - x0) / h)
    x = x0
    y = y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        y += (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys

# ==== Ejecuta RK4 ====
x_vals, y_vals = runge_kutta4(f, x0, y0, xf, h)

# ==== Guarda resultados en Excel ====
df = pd.DataFrame({'x': x_vals, 'y': y_vals})
df.to_excel('tabla_resultados_funcion_rk4.xlsx', index=False)
print("Archivo 'tabla_resultados_funcion_rk4.xlsx' generado correctamente.")

# Opcional: muestra los resultados en pantalla
for xi, yi in zip(x_vals, y_vals):
    print(f"x = {xi:.2f}, y = {yi:.6f}")