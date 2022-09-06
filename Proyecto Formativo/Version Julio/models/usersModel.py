
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
# ver usuarios ******************************************************************************
def verCarruselModel(id=""):
    sql = """
        SELECT
            id,
            img,
            decripcion,
            url,
            fecha_inicio,
            fecha_fin,
            estado
        FROM
            carrusel
    """

# en caso de seleccionar un usuario especifico **********************************************
    if len(id) != 0:
        sql += """
            WHERE decripcion like '%{0}%'
        """.format (id)
    return con.getData(sql)


# crear usuarios *************************************************************************
def crearUsuariosModel(datos):
    sql = """
        INSERT INTO usuarios
            (id,usuario, password)
        VALUES(NULL,'{0}','{1}')
    """.format(datos[0],datos[1])
    return con.query(sql)


# modificar usuario **********************************************************************
def modificarUsuarioModel(datos):
    sql = """
        UPDATE usuarios
        SET 
            usuario = '{1}',
            password = '{2}'
        WHERE 
            usuarios.id = {0}
    """.format(datos[0],datos[1],datos[2])
    return con.query(sql)

# borrar usuario ***************************************************************************
def borrarUsuarioModel(id):
    sql = """
        DELETE FROM tbl_usuarios
        WHERE
            usuarios.id = {0}
    """.format(id)
    return con.query(sql)