from Inventario_DAO import inventario_DAO
from inventarioClass import datos_producto
manejador_lista = inventario_DAO()



a=0
while a!=-1:
    print("")
    print("===============================================================")
    print("  PRACTICA 1 - LENGUAJES FORMALES DE PROGRAMACION - 202201947")
    print("===============================================================")
    print("")
    print("1. Cargar inventario inicial")
    print("2. Cargar instrucciones de movimientos")
    print("3. Crear informe de inventario")
    print("4. Salir")
    
    while True:
        try:
            a = int(input("Seleccione una opcion: "))
            if a >= 1 and a <= 4:
                print("Seleccionaste Opcion:", a)
                break
            else:
                print("Opcion incorrecta, ingrese una opcion válida mayor que 0")
        except ValueError:
            print("Opcion incorrecta, ingrese una opción válida (asegúrese que sea un número)")


    print("")
    print("")
    if a==1:
        print("")
        print("Cargara el inventario inicial")
        
        #ruta_del_archivo = input("Ingrese la ruta completa del archivo: ")
        try:
            with open("Inventario.inv", "r+") as archivo:
                for linea in archivo:
                    objeto = linea.strip().replace("crear_producto ", "").split(';')
                    manejador_lista.agregar_producto(objeto[0], objeto[1], objeto[2], objeto[3])
            print("--------------------------------------")         
            manejador_lista.imprimir_productos()
            print("--------------------------------------")
        except FileNotFoundError:
            print("El archivo no existe ")
        print("--------------------------------------")         
        print("Continuara al menu con inventario cargado")
        print("--------------------------------------")
        print("")
        print("")
    elif a==2:
        print("")
        print("Cargara las instrucciones de movimientos")
        print("")

        print("")
        print("")
    elif a==3:
        print("")
        print("Se creara el informe/reporte de inventario")
        print("")

        print("")
        print("")
    elif a==4:
        print("")
        print("ESTA SALIENDO")
        a=-1
        break

