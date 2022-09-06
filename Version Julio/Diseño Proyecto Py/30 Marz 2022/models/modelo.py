from database.dataSource import DataSource
from database.settings import conexion

#como una cadena de conexion
con = DataSource(conexion["host"],
                conexion["user"],
                conexion["passw"],
                conexion["database"],
                conexion["port"],
                conexion["tipo_bd"])

def verUsuarios(name):
    if len(name)==0:
        sql = """
            SELECT *
            FROM `usuario`"""
    else:
        sql = """
            SELECT *
            FROM `usuario`
            where id like '{}'
        """.format(name)

    return (con.getData(sql))