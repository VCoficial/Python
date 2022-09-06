from database.dataSource import DataSource
from database.settings import conexion

con = DataSource(conexion["host"],
                conexion["user"],
                conexion["passw"],
                conexion["database"],
                conexion["port"],
                conexion["tipo_db"])
def guardarDatos(lista):
    sql = """
    INSERT INTO usuario
        (usuario,password)
    VALUES
        ({0}, {1})
    """.format(lista[0], lista[1])
    return con.query(sql)