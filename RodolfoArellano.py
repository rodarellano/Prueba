def registrarlibro(): 
    titulo = input("Ingrese título del LIBRO: ")
    autor = input("Ingrese autor del LIBRO: ")
    genero = input("Ingrese el género del LIBRO: ")
    precio = input("Ingrese un precio para el LIBRO: ")

def lista_libros():
    print(f"""
    Título:\t{titulo}
    Autor:\t{autor}
    Género:\t{genero}
    Precio:\t{precio}
    """)
    
def reg_venta(): 
     titLibro = input("Ingrese el título del LIBRO: ")
     cantLibro = int(input("Ingrese la cantidad de LIBROS vendidos: "))
     precioLibro = int(input("Ingrese precio del LIBRO: "))
     precioFinal = int(input("Ingrese el precio final del LIBRO: "))
     
def impr_ventas():
    print("""
          <<INVENTARIO>>
          1.- Imprimir todos los reportes
          2.- Imprimir por género
          3.- Salir
          """)
    
while True:
            print("""
            --------------
            <<INVENTARIO>>
            --------------
            1.- Registrar libro
            2.- Listar todos los libros
            3.- Registrar venta
            4.- Imprimir reporte de ventas
            5.- Generar TXT
            6.- Salir      
                """)
            try:    
                opcion = int(input("SELECCIONE UNA OPCIÓN: "))
                if opcion >= 1 and opcion <= 6:
                    if opcion == 1:
                        print(registrarlibro)
                    elif opcion == 2:
                        print(lista_libros)
                    elif opcion == 3:
                        print(reg_venta)
                    elif opcion == 4:
                        print(impr_ventas)
                    elif opcion ==5:
                        print()
                    elif opcion ==6:
                        print("Muchas gracias!!")
                        break
            except ValueError:
                print("INGRESE VALORES VALIDOS!!!")
