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

# ver carrusel ****************************************************
def verCarruselModel(id = ""):
    sql = """ 
        SELECT 
            id, 
            img, 
            descripcion, 
            url, 
            fecha_inicio, 
            fecha_fin, 
            estado 
        FROM
            carrusel
    """
    
    # en caso de seleccionar n usuario expcifico
    if len(id) != 0:
        sql += """
            WHERE id like '{0}'
        """.format (id)
    
    return con.getData(sql)   




    
    
    
    
    
    
    
    
           