import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd

num_lineas = 95

f=open("CALICATAS_2.gpx","r")
lineas = f.readlines()
latitudes = np.zeros(num_lineas)
longitudes = np.zeros(num_lineas)
cod = {}
x = 0
for linea in lineas:

    latitudes[x] = linea[5:15]
    longitudes[x] = linea[22:32]
    cod[x] = str(linea[95:98])
    x=x+1

f.close()

x = 0
for linea in lineas:
    print(latitudes[x])
    x=x+1

x = 0
for linea in lineas:
    print(longitudes[x])
    x=x+1

x = 0
for linea in lineas:
    print(cod[x])
    x=x+1

print(latitudes.size)
print(longitudes.size)
