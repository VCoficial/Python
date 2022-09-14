from colorama import Cursor
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



def registrarUsuarioModel(datos):
    sql = """
        INSERT INTO `persona` 
            ( `nombre`, `Telefono`) 
        VALUES 
            ('{0}', '{1}');
    """.format (datos[0], datos[1])
    print(sql)
    return con.query(sql)


def verUsuarios(id = ""):
    
    sql = """ 
        SELECT 
           *
        FROM 
            persona           
    """
    if len(id) !=0:
        sql += """
            WHERE ID = '{0}'
        """.format (id)
    
    return con.getData(sql)    



def modificarUsuariosModel (datos):
    sql = """
        UPDATE persona 
        SET
            nombre = '{1}',
            Telefono = '{2}'
        WHERE
            ID  = {0}
    """.format(datos[0],datos[1],datos[2])
    return con.query(sql)

#-------------------------------------------------------------------------------

def borrarUsuariosModel (id):
    sql = """
        DELETE FROM persona 
        WHERE
            ID = {0}
    """.format(id)
    print(sql)
    return con.query(sql)    








