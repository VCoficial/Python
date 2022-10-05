import pandas as pd

""" 
lista=pd.DataFrame({'A': [1, 2, 3]})
print(lista)

lista.name = "Lista_numeros"
print(lista)

lista = pd.Series( [1, 2, 3] )
print ( lista )
lista.name = "Lista_numeros"
print ( lista ) """

# ************************************+

""" df = pd.DataFrame(
    {
        "columna1": [1, 2, 3], 
        "columna2": [1, 2, 3], 
    }
)

print (df) 
"""

# **************************************************

# https://archive.ics.uci.edu/ml/datasets/Iris

# lectura de datos
df = pd.read_csv("datos/iris.data")

print ( df )

# mostrar  5 primeros datos (xcantidad)
print ( df.head() )

# mostrar 5 ultimos datos (xcantidad)
print ( df.tail() )

# colocar cabeceras
cabecera = ["Lon_sepalo", "Anc_sepalo", "Lon_petalo", "anc_petalo", "clase"]
df.columns = cabecera

print ( df.head() )

# devolver el nombre de las columnas
print ( df.columns ) 

# mostrar cantidad filas y columnas
print ( df.shape )

# describe el dataframe
print ( df.describe() )

# contar datos de una columna
print (df['clase'].value_counts() )

# invertir de columnas a filas
#print (df.T)

# ordenar por columnas
print ( df.sort_values('Anc_sepalo') )

# mostrar columnas especificas
print ( df[["Lon_sepalo", "Anc_sepalo"]] )

# mostrar por filas y columnas
print ( df.iloc[[4, 5], [0, 1]] )

# mostrar datos condiciones
print ( df[ df["Lon_sepalo"] >5 ] )

# hallar promedio de columna
print ( df["Lon_sepalo"].mean())

# aplicar funciones matematicas
print ( df["Lon_sepalo"].apply(lambda x: -x))
print ( df["Lon_sepalo"].apply(lambda x: x**2))

