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

def valLoginModel(datos):
    
    sql = """ 
        SELECT 
            id,
            nombre,
            apellido, 
            id_tipo,
            numeroDocumento,
            id_rol,
            correo,
            telefono,
            ficha,
            id_centro
        FROM 
            usuario
        WHERE
            numeroDocumento like '{0}' AND
            contrasena like '{1}'
    """.format (datos[0], datos[1])
    
    return con.getData(sql)