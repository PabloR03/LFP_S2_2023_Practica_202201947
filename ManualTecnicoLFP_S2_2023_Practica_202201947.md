# LENGUAJES FORMALES DE PROGRAMACION B-
## Practica 1
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Pablo Andres Rodriguez Lima
Carne: 202201947
Correo: pabloa10rodriguez@gmail.com
```
---
## Descripción del Proyecto
Presentacion de programa para el manejo de archivos aplicado para un sistema de inventario de una tienda, con posibilidad de ejecutar acciones tales como agregar y disminuir stock, atraves de una interfaz, uso de archivos .inv y .mov
Requerimientos mínimos para el uso del programa
Python en su versión 2.8 o posteriores (se creó bajo la versión 3.11.4), Se recomienda un ide como Pycharm o bien un editor de texto con su extensión como Visual Studio Code.


## Objetivos
* Objetivo General
    * Desarrollar y presentar un programa de software integral que permita el manejo eficiente del inventario de una tienda a través de la implementación de archivos .inv y .mov
* Objetivos Específicos
    * Crear una interfaz de usuario intuitiva y de fácil uso que posibilite a los empleados de la tienda interactuar con el sistema de inventario de manera eficiente y sin complicaciones.
    * Implementar un sistema de gestión de archivos que utilice los formatos .inv y .mov para almacenar y registrar los cambios en el inventario, garantizando la integridad y trazabilidad de los datos.

---
## Ejemplo de Texto
**Clases y métodos utilizados**
“datos_producto”para adjuntar y guardar como objetos los datos propuestos en el inventario a cargar
![INVCLASS](https://i.ibb.co/y0pBm8q/202201947-inventario-Class.png)

Clase “inventario_DAO” se importa de la clase anterior para realizar la logística y el funcionamiento del programa
![INVCLASSDAO](https://i.ibb.co/Nmy8QCQ/202201947-inventario-DAO.png)

**Método “__init__(self)”**
	Es un método en el cual se crea una lista en la cual se almacenan todos los artículos para la venta va a ser bajo la cual puede trabajar el programa.
**Método “Agregar al Programa”**
	Es un método el cual recibe como objeto las variables separadas de cada articulo de la lista y ordena para cargarlo y adjuntarlo en el array antes creado.
**Método “encontrar_producto”**
	Es un método el cual recorre la lista y verifica que Producto y Ubicación estén en el mismo lado, ya que es una restricción, deben existir los dos para que se pueda llevar acabo un movimiento.
**Método “agregar_stock”**
	Es un método que verifica que si el articulo y la ubicación coinciden pueda agregar más del mismo artículo a la lista aumentando su cantidad en el stock.
**Método “vender_producto”**
	Es un método el cual verifica que un articulo exista y permite que se disminuyan sus existencias, solo funciona si no se exceden en la venta es decir siempre tiene que haber por lo menos un producto en stock.
**Método “Imprimir”**
	Es un método que lo que permite es imprimir en consola los movimientos que hace para llevar un mejor control de lo que se va haciendo.

## Aplicación principal
Se importa las clases antes mencionadas y se declara una variable para entrar al menú principal.
Este imprime una serie de opciones las cuales están: Cargar Inventario, Instrucciones de Movimiento, Crear Informe.
Se despliega un while para que ingrese una de las opciones antes mencionadas.
![MENU](https://i.ibb.co/z4cBzn3/202201947-app-Menu.png)

CASO 1: “Cargar Inventario Inicial”
Aquí bajo la variable “ruta_del_archivo” se busca el archivo correspondiente a la carga del inventario, se llama a la lista para que guarde los objetos y ya los pueda manipular el programa.
Se llama al método imprimir para que muestre el estado en consola, si todo fue cargado bien no muestra error de lo contrario solicitara que lo vuelva a cargar.
![APPINV](https://i.ibb.co/wMwSpKx/202201947-app-Inventario.png)

CASO 2: “Instrucciones de movimiento” 
Se solicita al usuario que ingrese una ruta de acceso, luego se abre el archivo la cual recibe una instrucción y dependiendo de la condición hace la venta disminuyendo el stock o agrega el stock siempre y cuando se cumplan las validaciones.
![APPMOV](https://i.ibb.co/qYmSj73/202201947-app-Movimiento.png)

CASO3: “Creación del reporte”
Crea un archivo .txt al cual se le ingresa un encabezado y se tabulan los resultados de los movimientos demostrando que fue lo que quedo al final.
![REPORTE](https://i.ibb.co/9pNd3Mx/202201947-app-Reporte.png)

CASO 4: “Salida”
Se da un nuevo valor a la variable de condición de salida y rompe para salir del while. 
![SALIDA](https://i.ibb.co/ySVbLBV/202201947-app-Salida.png)