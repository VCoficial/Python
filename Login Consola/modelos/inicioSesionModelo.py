from database.dataSource import DataSource
from database.settings import conexion

con = DataSource (
    conexion["host"],
    conexion["user"],
    conexion["passw"],
    conexion["database"],
    conexion["port"],
    conexion["tipo_bd"]
)

def inicioSesionModelo(datos):
    sql = """
        SELECT *
        FROM `usuario`
        WHERE
            nombre like "{0}" and 
            contrasena like "{1}"
    """.format(datos[0],datos[1])
    

    return con.getData(sql)