import mysql.connector
class CConexion:
    def conexionbd():
        try:
            
             conexion = mysql.connector.connect(user='root',password='root',
                                                host='localhost',
                                                database='pixecode',
                                                port='3306')
            
        except mysql.connector.Error as error:
            print("error al conectar con la base de datos {}".format(error))