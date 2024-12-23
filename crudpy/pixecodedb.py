from conexion import *

class CClientes:
    
    def ingresa(nombres,apellidos,sexo):
        
        try:
         cone = CConexion.conexionbd()
         cursor = cone.cursor()
         sql ="insert into pixecodedb.clientes values(null,%s,%s,%s);"
         #la variable valores tiene que ser una tupla
         #como minimina expresión es: (valor,) la coma hace que sea una tupla
         #las tuplas son listas inmutables, eso quiere decir que no se puede modificar  
         valores = (nombres,apellidos,sexo)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"registro ingresado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))