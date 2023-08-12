from Inventario_DAO import inventario_DAO
from inventarioClass import datos_producto
listacontodo = inventario_DAO()



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
                print("")
                print("")
                print("***************************")
                print("  Seleccionaste Opcion:", a)
                print("***************************")
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
            with open("Practica_202201947/inventario.inv", "r+") as archivo:
                for linea in archivo:
                    producto = linea.strip().replace("crear_producto ", "").split(';')
                    listacontodo.agregar_al_programa(producto[0], producto[1], producto[2], producto[3])
            print("--------------------------------------")         
            listacontodo.imprimir()
            print("---------------------------------------------")         
            print("  Continuara al menu con inventario cargado")
            print("---------------------------------------------")
        except FileNotFoundError:
            print("El archivo no existe ")
            print("No se cargara el inventario inicial, ingrese de nuevo al menu y seleccione la opcion 1")
        
        print("")
        print("")
    elif a==2:
        print("")
        print("Cargara las instrucciones de movimientos")
        #ruta_del_archivo_mov = input("Ingrese la ruta completa del archivo con el inventario: ")
        try:
            with open("Practica_202201947/movimientos.mov", "r+") as archivo:
                for linea in archivo:
                    producto = linea.strip().split(' ')
                    instruccion = producto[0]
                    accion_producto = producto[1].split(';')
                    if instruccion == "agregar_stock":
                        listacontodo.agregar_stock(accion_producto[0], accion_producto[2], int(accion_producto[1]))
                    elif instruccion == "vender_producto":
                        listacontodo.vender_producto(accion_producto[0], accion_producto[2], int(accion_producto[1]))
        except FileNotFoundError:
            print("El archivo no existe.")
        print("------------------------------------------")         
        listacontodo.imprimir()
        print("------------------------------------------") 
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

