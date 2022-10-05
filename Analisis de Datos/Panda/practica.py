import pandas as pd
df = pd.read_csv("Analisis de Datos\datos\equipos.data")

# 1.Organice la cabecera 
cabecera = ["victorias", "derrotas", "empates", "otros", "equipos"]
df.columns = cabecera
""" print ( df.head() ) """

# 2.muestre nombre de las columnas
""" print ( df.columns ) """

# 3.muestre los últimos 5 datos
""" print ( df.tail(5) ) """

# 4.hallar el promedio de victorias
""" print (df["victorias"].mean()) """

# 5.hallar el promedio de derrotas
""" print (df["derrotas"].mean()) """

# 6.hallar promedio de empates
""" print (df["empates"].mean()) """

# 7.hallar sumatoria de victorias
""" print (df["victorias"].sum()) """

# 8.ordenar columnas por equipos
""" print ( df.sort_values('equipos') )  """

# 9.mostrar cantidad de filas y columnas
""" print ( df.shape ) """

# 10.mostrar los 5 primeros datos
""" print ( df.head() )  """

# 11.mostrar victorias del america
""" print (df.loc[df["equipos"]=='America',['victorias','equipos']]) """

# 12.mostrar victorias del nacional
""" print (df.loc[df["equipos"]=='Nacional',['victorias','equipos']]) """

