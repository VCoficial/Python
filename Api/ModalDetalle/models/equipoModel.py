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


""" copiar consulta update para equipo """

def editarequipoModel(datos):
    sql = """
        UPDATE `equipos` 
            SET serie='{1}', id_Marca='{2}', detalle='{3}', id_Usuario='{4}', estado='{5}', img='{6}', Qr='{7}
        WHERE id='{0}'
    """.format (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7] )
    
    return con.query(sql)

def verpcModel(id = ""):
    sql = """
    SELECT 
    serie,
    id_Marca,
    detalle,
    id_Usuario,
    estado,
    img
    FROM
    equipos"""
    if len(id) !=0:
        sql += """
            WHERE id = '{0}'
        """.format (id)
    return con.getData(sql)




    