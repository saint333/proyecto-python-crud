#importar el modulo para conectarme a sql server
import pyodbc

#creo una funcion de conexion a sql server
def conexion_server():
    try:
        connection= pyodbc.connect("DRIVER={ODBC Driver 17 for SQL server};SERVER=localhost;DATABASE=bdpractica;UID=SA;PWD=Joseph23@")

    #captura cualquier error que produzca y lo muestra
    except Exception as ex:
        print(ex)

    return connection

#punto de acceso para ejecutar la funcion que nos conecte a la base de dato
if __name__ == '__main__':
    conexion_server()