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

# registrar usuario
def registrarUsuarioModel(datos):
    sql = """
        INSERT INTO `usuario` 
            (`nombre`, `apellido`, `id_tipo`, `numeroDocumento`, `id_Rol`, 
            `contrasena`, `estado`, `correo`, `telefono`, `ficha`, `id_centro`, `fechaNacimiento`) 
        VALUES 
            ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '', '{10}');
    """.format (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10] )
    
    return con.query(sql)