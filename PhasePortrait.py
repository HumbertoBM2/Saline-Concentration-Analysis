# Humberto Barrera Martínez
# Fecha 06/09/2023
# Descripción: Programa en python que grafica el plano fase de un sistema de EDOs
import numpy as np
import matplotlib.pyplot as plt

# Se define la función que calcula las derivadas del sistema de EDOs
def sistema(x, y, vs, vd, f0):
    dxdt = -x / vs * f0
    dydt = (x / vs - y / vd) * f0
    return dxdt, dydt

# Se define el rango de valores para x y y
x = np.linspace(0, 500, 500)  # Rango para x
y = np.linspace(0, 500, 500)  # Rango para y

# Se crea una malla con los valores de x y y
X, Y = np.meshgrid(x, y)

# Se definen los valores de las constantes
vs = 920000000  # Volumen del lago salado
vd = 8100000000  # Volumen del lago dulce
f0 = 1820  # Tasa de flujo

# Se calculan las derivadas del sistema de EDOs
DX, DY = sistema(X, Y, vs, vd, f0)

# Se grafica el plano fase del sistema de EDOs
plt.figure(figsize=(8, 8))
plt.streamplot(X, Y, DX, DY, color='blue', density=1.5, linewidth=1, arrowsize=1)
plt.xlabel('Concentracion Salada (c_s)')
plt.ylabel('Concentracion Dulce (c_d)')
plt.title('Plano Fase del Sistema de Ecuaciones (streamplot)')
plt.grid()
plt.show()
