import mysql.connector
class CConexion:
 def conexionbd():
    try:
            
        conexion = mysql.connector.connect(user='root',password='root',
                                                host='127.0.0.1 ',
                                                database='pixecodedb',
                                                port='3306')
        print("conexion correcta")
             
        return conexion
            
    except mysql.connector.Error as error:
        print("error al conectar con la base de datos {}".format(error))
            
        return conexion
    
    
 conexionbd()
         