import csv

file = open ('datos/COVCOL.csv' )
lectura = csv.reader(file)

datos = ""

for fila in lectura:
    try:
        print(fila[5])
        if int(fila[5]) >= 18 and int(fila[5])<62:
            total = "adulto"
        elif int(fila[5]) >= 62:
            total = "viejo"
        else:
            total = "nino"
        
        filas = (fila[7]+";"+fila[5]+";"+total) 
        datos += filas+"\n"
    except:
        pass
print (datos)

archivo = open("dato.csv", "w")
archivo.write(datos)
archivo.close