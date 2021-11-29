#importo mis modulos para poder utlizar sus metodos

from crud import *
import sys,os,time,platform

#creo la opcion salir del programa
def salir():
    print("="*15,"GRACIAS POR USAR ESTE PROGRAMA","="*15)
    sys.exit()

#para limpiar la terminal ya sea en windows o linux 
def limpiar():
    time.sleep(1)

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#main es nuestra funcion principal
def main():

    #limpiamos la consola
    limpiar()
    
    #mostramos el enbacezado y esperamos un segundo
    print("="*15,"PROGRAMA UTILIZANDO CRUD","="*15,end="\n")

    time.sleep(1)

    # mostramos los datos y el menu principal
    mostra_datos()
    
    while True:
        
        #para que si ingresamos un valor desconocido while true permite mostrar otra vez el menu

        print("""
        1.- Mostrar datos de empleados
        2.- Añadir un empleados
        3.- Actualizar datos de empleado
        4.- Eliminar datos de empleado
        5.- Salir del programa
        """)

        time.sleep(1)

        #capturamos la opcion que se llevara a cabo luego limpiamos y mostramos la funcion
        accion = input("    ¿Que desea realizar?: ")

        limpiar()

        if accion == "1":
            mostra_datos()
            print("="*15,"PROGRAMA UTILIZANDO CRUD","="*15,end="\n")
        elif accion == "2":
            insertar_datos()
            limpiar()
            print("="*15,"PROGRAMA UTILIZANDO CRUD","="*15,end="\n")
        elif accion == "3":
            actualizar_datos()
            limpiar()
            print("="*15,"PROGRAMA UTILIZANDO CRUD","="*15,end="\n")
        elif accion == "4":
            eliminar_datos()
            time.sleep(1.5)
            limpiar()
            print("="*15,"PROGRAMA UTILIZANDO CRUD","="*15,end="\n")
        elif accion == "5":
            salir()
        else:
            print("    ingrese un numero correcto")
            time.sleep(1)
            limpiar()
            print("="*15,"PROGRAMA UTILIZANDO CRUD","="*15,end="\n")


#nuestro punto de acceso para ejecutar la funcion principal
if __name__ == '__main__':
    main()
