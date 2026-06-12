# ============================================================= #
# FUNCIONES DE MENU
# ============================================================= #

# Se define una funcion que presenta el menu principal.

def menu_principal():
    """
    Muestra por pantalla el menú principal y solicita al usuario la entrada de menú a la que desea acceder.
    Valida la entrada del usuario con la función validar_opcion(minimo_vo,maximo_vo)

    Retorna:
        int: La entrada de menú seleccionada por el usuario.
    """

    print("""\n MENU PRINCIPAL
    1. Carga de Herramientas con Existencias Iniciales.
    2. Visualización del inventario.
    3. Consulta de stock.
    4. Reporte de agotados.
    5. Alta de nuevo producto.
    6. Actualización de stock.
    7. Salir.""")
    print()
    opcion_mp = validar_opcion(1,7)

    return opcion_mp


# Se define una funcion que muestra el menu secundario de la opcion 6. Actualizacion de stock, y solicita al usuario la opcion de menú seleccionada.

def menu_secundario():

    """
    Muestra por pantalla el menú secundario correspondiente a la opción 6 del menú principal y solicita al usuario la entrada de menú a la que desea acceder.
    Valida la entrada del usuario con la función validar_opcion(minimo_vo,maximo_vo)

    Retorna:
        int: La entrada de menú seleccionada por el usuario.
    """

    print("""\n MENU ACTUALIZACION DE STOCK.
    1. Venta.
    2. Ingreso.
    3. Volver al menú principal.""")
    print()

    opcion_ms = validar_opcion(1,3)

    return opcion_ms


# ============================================================= #
# FUNCIONES DE VALIDACION DE INGRESO DE DATOS
# ============================================================= #

# Se define la funcion validar_opcion que valida que el usuario ingrese un numero correspondiente al menu principal o al menu secundario.

def validar_opcion(minimo_vo,maximo_vo):
    """
    Valida que el usuario ingrese un número entero entre los números minimo_vo y maximo_vo, correspondientes al listado de un menú de opciones.
    
    Parámetros:
        minimo_vo (int): Número entero de la opción inicial del menú.
        maximo_vo (int): Número entero de la opción final del menú.
    
    Retorna:
        int: La opción elegida por el usuario, cuando ésta cumple los requisitos establecidos.
    """

    while True:
        try:
            opcion_vo = int(input("\nIngrese una opción: "))
            if minimo_vo <= opcion_vo <= maximo_vo:
                return opcion_vo
            else:
                print(f"\nIngreso inválido. Solo se permite el ingreso de los números {minimo_vo} a {maximo_vo}.")
        except ValueError:
            print("\nIngreso inválido. Ingrese el valor númerico correspondiente a la opción del menú a la que desea acceder.")
        except Exception as e:
            print(f"""Ocurrió el siguiente error: {type(e).__name__}. 
            Por favor, tome nota del error y comuniquese con el servicio de soporte de la aplicación.
            Lamentamos las molestias ocasionadas.""")

# ============================================================= #
# FUNCIONES OPERATIVAS
# ============================================================= #

# Se define la función cantidad_tipos_herramientas para que el usuario ingrese el número de tipos de herramientas que quiere ingresar en el stock inicial.
# Se limita a 500, para evitar que el usuario ingrese por error numeros muy altos que bloqueen el programa.

def cantidad_tipos_herramientas():
    """
    Permite al usuario ingresar la cantidad de tipos de herramientas que compondrán el stock inicial de la ferretería, siempre que sea un número ente 1 y 1000.

    Retorna:
        int: Número entero de tipos de herramientas a incorporar al stock.
    """
    while True:
        try:
            tipos_cth = int(input("\nIngrese el número de herramientas que quiere registrar en el inventario: "))
            if tipos_cth <= 0:
                print("\nIngreso inválido. Debe ingresar al menos un tipo de herramienta.")
            elif tipos_cth > 500:
                print("\nIngreso inválido. Solo se permite el ingreso incial de hasta 500 tipos de herramientas en el stock. \nPara ingresar un número mayor de herramientas una vez completado el total permitido, deberá ingresar en la opción 5 del menú principal.")
            else:
                return tipos_cth
        except ValueError:
            print("\nIngreso inválido. Ingrese un número entero.")
        except Exception as e:
            print(f"""Ocurrió el siguiente error: {type(e).__name__}. 
            Por favor, tome nota del error y comuniquese con el servicio de soporte de la aplicación.
            Lamentamos las molestias ocasionadas.""")

# ============================================================= #
# PROGRAMA PRINCIPAL
# ============================================================= #

# Se establece la variable run_menu para evitar el uso de break en la opción 7 de salida del programa.
run_menu = True

# Se define una lista llamada inventario, que contendra diccionarios con la estructura herramientas:cantidad.
inventario = []


while run_menu:
    opcion_menu_principal = menu_principal()
    match opcion_menu_principal:
        case 1:
            print("\nCARGA DE HERRAMIENTAS CON EXISTENCIAS INICIALES")
            tipos_herramientas = cantidad_tipos_herramientas()
        case 2: 
            print("\nVISUALIZACION DE INVENTARIO")
        case 3:
            print("\nCONSULTA DE STOCK")
        case 4:
            print("\nREPORTE DE AGOTADOS")
        case 5:
            print("\nALTA DE NUEVO PRODUCTO")
        case 6:
            print("\nACTUALIZACION DE STOCK (VENTA / INGRESO)")
            # Se establece la variable run_menu_secundario para evitar el uso de break en la opción 3 de retorno al menú principal.
            run_menu_secundario = True
            while run_menu_secundario:
                opcion_menu_secundario = menu_secundario()
                match opcion_menu_secundario:
                    case 1:
                        print("\nVENTA")
                    case 2: 
                        print("\nINGRESO")
                    case 3:
                        print("\nVOLVER AL MENU PRINCIPAL")
                        run_menu_secundario = False
        case 7:
            print("\nSALIR")
            run_menu = False


