import pandas as pd

# Leer el Excel
df = pd.read_excel("datos.xlsx")

# Convertir cada columna en un arreglo (lista)
x = df["x"].tolist()
y = df["y"].tolist()

print("Arreglo X:", x)
print("Arreglo Y:", y)

# Hay que asegurarse que las x esten separadas de forma uniforme
# y que ambos arreglos tengan el mismo tamaño

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

# Para el método del trapecio:

def calcularAreaTrapecio(b,a,fb,fa):
    return (((fb+fa)/2)*(b-a))

def verificarDivTrapecios(tam,n): # teniendo en cuenta el solapamiento
    r = ((tam-1)/n)+1
    if r % 1 == 0:
        return True
    else:
        return False

def hallarIntegralTrapecio(x,y,n):
    # n = cantidad de trapecios a dividir
    if verificarDivTrapecios(len(y),n):
        h = int(((len(y)-1)/n)+1)
        resultado = 0
        a = int(0)
        for i in range(0,n):
            resultado += calcularAreaTrapecio(x[(a+(h-1))],x[a],y[(a+(h-1))],y[a])
            #print(calcularAreaTrapecio(x[(a+(h-1))],x[a],y[(a+(h-1))],y[a]))
            a = (a+(h-1))
        return resultado
    else:
        print(f"No se puede dividir los datos en {n} trapecios")
        return None

# Para calcular el error se necesita la segunda derivada en un punto
# esta se calcula usando la formula (b-a)/d  donde d es la distancia 
# entre un punto y otro, todos los datos deben ser equidistantes para 
# aplicar esta formula

# Esta formula aplica hasta el antepenultimo dato, si se trata de aplicar
# en el penultimo o ultimo va a fallar por que no contamos con los datos 
# para hallar la segunda derivada de estos puntos

def calcularError(datos,pos,d):
    # primero hallamos la segunda derivada
    
    dx1 = (datos[pos+1] - datos[pos])/d
    dx2 = (datos[pos+2] - datos[pos+1])/d
    d2x = (dx2 - dx1)/d # esta es la segunda derivada del dato en la posicion ingresada
    
    # Ahora calculamos el error
    error = (-1/12)*d2x*((d)**3)

    return error

# Número de trapecios para la integral
n_trapecios = 12

area_trapecio = hallarIntegralTrapecio(x, y, n_trapecios)
print(area_trapecio)

# Ejemplo: calcular el error en la posición 1 y con paso d entre x
if len(x) > 2:
    d = x[1] - x[0]
    error_en_1 = calcularError(y, 1, d)
    print(error_en_1)
else:
    error_en_1 = None

# Guardar todo en un Excel
df_resultados = pd.DataFrame({
    'x': x,
    'y': y,
    'primerDerivada': primerDerivada,
    'segundaDerivada': segundaDerivada,
    'tercerDerivada': tercerDerivada,
    'cuartaDerivada': cuartaDerivada
})

# Fila resumen para el área y el error
extra_rows = []
extra_rows.append({'x':'IntegralTrapecio','y':area_trapecio,'primerDerivada':None,'segundaDerivada':None,'tercerDerivada':None,'cuartaDerivada':None})
if error_en_1 is not None:
    extra_rows.append({'x':'ErrorTrapecio_p1','y':error_en_1,'primerDerivada':None,'segundaDerivada':None,'tercerDerivada':None,'cuartaDerivada':None})

df_resultados = pd.concat([df_resultados, pd.DataFrame(extra_rows)], ignore_index=True)

df_resultados.to_excel('tabla_derivadas_y_trapecio.xlsx', index=False)

print("Archivo 'tabla_derivadas_y_trapecio.xlsx' generado correctamente.")