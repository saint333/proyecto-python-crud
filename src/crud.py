# importo mi archivo conexion y dos modulos mas
import conexion, os, time

#creo una funcion para traer todos los datos de mi base de datos
def leer_datos():

    #verficamos con try si todo esta bien
    try:

        #con el cursor creado lo utilizaremos como medio que nos conecte a la base de datos y tambien para ejecutar algunos query
        cursor = conexion.conexion_server().cursor()
        cursor.execute("select * from empleado;")

        #creamos una variable que contega los datos de los empleados
        empleados = cursor.fetchall()

        #con datos mostraremos uno por uno los empleados
        datos=[empleado for empleado in empleados]

        #retornamos la lista de datos
        return datos

    except Exception as e:

        return e

#para dar mas orden a los datos creamos otra funcion
def mostra_datos():
    
    #encabezado 
    print("="*15,"MOSTRANDO DATOS DE LOS EMPLEADOS","="*15,end="\n")

    #la lista que nos retorna leer_datos() lo almacenamos en la variable datos
    datos= leer_datos()

    #encabezado de la informacion
    print("ID ","NOMBRE\t\t","CARGO \t","SALARIO",sep="\t")

    #recoremos datos y damos formato para vizualizar los datos mas ordenados
    for dato in datos:
        print(dato[0],dato[1],"\t",dato[2],dato[3],sep="\t",end="\n")
    print()

    time.sleep(1)

#funcion para agregar a un empleado
def insertar_datos():
    try:

        #creamos nuestra conexion y el query para insertar datos en la base de datos
        cursor = conexion.conexion_server().cursor()
        empleado = "insert into empleado values(?,?, ?, ?)"

        #mostramos el encabezado y pedimos los datos del empleado
        print("="*15,"INGRESE DATOS DEL EMPLEADO","="*15)
        id=int(input("Ingrese su ID: "))
        nombre= input("Ingrese su nombre: ")
        cargo = input("Cargo que va a desenpeñar: ")
        salario = float(input("Pago mensual: "))

        #limpiamos consola y damos visualizacion de lo ocurrido
        os.system("clear")

        print("AGREGANDO DATOS ......")
        time.sleep(1.5)
        print("EMPLEADO AGREGADO SATISFACTORIAMENTE....")
        time.sleep(1.5)

        #ejecutamos el query con los datos obtenidos y actualizamos la base de datos
        cursor.execute(empleado,id,nombre,cargo,salario)
        cursor.commit()

    except Exception as e:

        return e

#funcion para actualizar los datos de los empleados
def actualizar_datos():

    try:

        #creamos nuestra conexion  y los query donde el primero para mostrar los datos del empleado que queremos actualizar y el ultimo para efectuar los cambios
        cursor = conexion.conexion_server().cursor()
        mostrar_emp= "select nombre,cargo,salario from empleado where id=?"
        empleado = "update empleado set nombre=?,cargo=?,salario=? where id = ?"

        #mostramos la cabezera y obtenemos el ID
        print("INGRESE SU ID PARA MOSTRAR DATOS A ACTUALIZAR")
        id=int(input("Ingrese su ID: "))

        #visualizamos lo acurrido
        time.sleep(1.5)
        print("BUSCANDO DATOS DEL EMPLEADO...")
        time.sleep(1.5)
        print("DATOS OBTENIDOS.....")
        time.sleep(1.5)
        os.system("clear")

        #ejecutamos el consulta pasando como parametro mostrar_emp y id y lo que retorna lo almacenamos en mostrar_empleado luego sobreescribimos la variable para finalmente encerrar en una lista en la variable datos
        mostrar_empleado=cursor.execute(mostrar_emp,id)
        mostrar_empleado = mostrar_empleado.fetchone()
        datos = list(mostrar_empleado)
        
        #mostramos los datos del empleado
        print("="*15,"DATOS DEL EMPLEADO","="*15)
        print("NOMBRE\t\t","CARGO \t","SALARIO",sep="\t")
        print(datos[0],"\t",datos[1],datos[2],sep="\t")

        time.sleep(2)

        #obtenemos los datos para actualizar
        print("="*15,"ACTUALIZAR DATOS DEL EMPLEADO","="*15)
        nombre= input("Ingrese su nombre: ")
        cargo = input("Cargo que va a desenpeñar: ")
        salario = float(input("Pago mensual: "))

        #visualizamos lo acurrido
        time.sleep(2)
        print("ACTUALIZANDO DATOS ......")
        time.sleep(2)
        print("DATOS DEL EMPLEADO ACTUALIZADOS......")
        time.sleep(2.5)
        os.system("clear")
        
        #ejecutamos el query con los datos obtenidos y actualizamos la base de datos
        cursor.execute(empleado,nombre,cargo,salario,id)
        cursor.commit()

    except Exception as e:

        return e

#funcion para eliminar datos de los empleados
def eliminar_datos():
    try:

        #medio de conexion y el query para eliminar los datos en sql server
        cursor = conexion.conexion_server().cursor()
        eliminar = "delete from empleado where id = ?"

        #emcabezado y obtenemos el ID para ubicar el empleado a eliminar
        print("====INGRESE SU ID PARA BORRAR/ELIMINAR DATOS DEL EMPLEADO====")
        id=int(input("Ingrese su ID: "))

        #pasamos como parametro el query y el ID y lo ejecutamos
        cursor.execute(eliminar,id)

        #limpiamos la consola 
        os.system("clear")

        #damos una mejor visualizacion de lo que sucede
        print("ELIMANDO DATOS......")
        time.sleep(2.5)
        print("DATOS ELIMINADOS..........")
        time.sleep(1.5)

        #guardamos los cambios
        cursor.commit()

    except Exception as e:

        return e


