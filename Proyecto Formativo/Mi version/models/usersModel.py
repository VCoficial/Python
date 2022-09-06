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
# ver Carrusel ******************************************************************************
def verCarruselmodel (id = ""):
    sql = """
        select
            id,
            img,
            descripcion,
            url,
            fecha_inicio,
            fecha_fin,
            estado
        from 
           carrusel
    """

    #en caso de seleccionar un usuario
    if len(id) != 0:
        sql += """
            WHERE usuario like '%{0}%'
        """.format (id)
    
    return con.getData(sql)

# Ver usuarios ***************************************************************************
def verusuario (usuario= "", password=""):
    sql="""
    select (usuario),(password) from usuario
    """
    if  len(usuario) != 0:
       sql += """
            where usuario='{0}' and password='{1}'
        """.format (usuario,password)
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