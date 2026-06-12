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


# Se define la funcion valdar_inventario_vacio que valida que el inventario se encuentre vacio para permitir el acceso a las distintas funcionalidades del menú principal.

def validar_inventario_vacio(inventario_viv):
    """
    Comprueba si el listado inventario se contiene o no elementos (una lista vacia corresponde a False). 
    Si no contiene elementos devuelve True, si contiene, devuelve False.
    
    Parámetro:
        inventario_viv (lista): listado de diccionarios con el formato herramienta:cantidad

    Retorna:
        True: si el inventario está vacío.
        False: si el inventario contiene elementos.
    """
    if not inventario_viv:
        return True
    else:
        return False

# Se define una funcion que valide que una herramienta esta presente en el listado.

def validar_herramienta_unica(herramienta_vhu,inventario_vhu):
    """
    Comprueba si la herramienta ingresada en la variable herramienta se encuentra en el listado inventario.
    
    Parámetros:
        herramienta_vhu (str): herramienta a ingresar al listado inventario por primera vez.
        inventario_vhu (lista): listado de herramientas previamente registradas por el usuario.
    
    Retorna:
        Booleano True: si la herramienta no se encuentra en la lista.
        Booleano False: si la herramienta se encuentra en la lista.
    """
    # Creo un listado de las claves de los diccionarios dentro de la lista inventario.
    herramientas_registradas = [list(item.keys())[0] for item in inventario_vhu]
    # Compruebo la presencia de la herramienta a ingresar en el listado previo.
    if herramienta_vhu in herramientas_registradas:
        print(f"\nLa herramienta {herramienta_vhu} ya fue registrada en el inventario. Proceda con el ingreso de una nueva herramienta.")
        return False
    else:
        return True


# ============================================================= #
# FUNCIONES OPERATIVAS
# ============================================================= #

# Se define la función cantidad_tipos_herramientas para que el usuario ingrese el número de tipos de herramientas que quiere ingresar en el stock inicial.
# Se limita a 500, para evitar que el usuario ingrese por error numeros muy altos que bloqueen el programa.

def cantidad_tipos_herramientas(inventario_cth):
    """
    Permite al usuario ingresar la cantidad de tipos de herramientas que compondrán el stock inicial de la ferretería, siempre que sea un número ente 1 y 1000.
    Valida que el listado inventario se encuentre vacio con la funcion validar_inventario_vacio.

    Retorna:
        int: Número entero de tipos de herramientas a incorporar al stock.
    """
    if not validar_inventario_vacio(inventario_cth):
        print("\nSe han registrado herramientas en el inventario previamente.")
        print("Para agregar nuevas herramientas ingrese en la opción 5.")

    while validar_inventario_vacio(inventario_cth):
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

        print("\nSe han registrado herramientas en el inventario previamente")
        print("Para agregar nuevas herramientas ingrese en la opción 5. ALTA DE NUEVO PRODUCTO del menú")

# Se define la funcion registrar_tipos_herramientas(inventario_rth)

def registrar_tipos_herramientas(inventario_rth,tipos_herramientas_rth):
    """
    Permite al usuario cargar el nombre de la herramienta y la cantidad que compone el stock inicial de dicha herramienta.
    Valida que la herramienta no se encuentre ya registrada con la funcion validar_herramienta_unica.
    
    Parametro:
        inventario_rth: listado de diccionarios con el formato herramienta:cantidad
    
    Retorna:
        lista: inventario_rth
    """
    # Solicitar nombre y cantidad de herramientas en un ciclo for que itera la cantidad de veces establecida en la variable tipos_herramientas.
    for i in range(tipos_herramientas_rth):
        while True:
            try:
                herramienta = input(f"\nIngrese el nombre de la herramienta Nro. {i+1}: ").upper()
                if not validar_herramienta_unica(herramienta, inventario_rth):
                    continue
                cantidad = int(input(f"Ingrese la cantidad de la herramienta {herramienta}: "))
                if cantidad <= 0:
                    print("\nIngreso inválido. La cantidad debe ser un número entero positivo.")
                else:
                    inventario_rth.append({herramienta: cantidad})
                    break
            except ValueError:
                    print("\nIngreso inválido. La cantidad debe ser un número entero positivo.")
            except Exception as e:
                    print(f"""Ocurrió el siguiente error: {type(e).__name__}. 
                    Por favor, tome nota del error y comuniquese con el servicio de soporte de la aplicación.
                    Lamentamos las molestias ocasionadas.""")
    return inventario_rth

# Se define una funcion que muestra el inventario actual de la ferretería.

def mostrar_inventario(inventario_mi):
    """
    Muestra por pantalla el inventario de herramientas y sus cantidades, siempre que se haya validado la presencia de elementos en el inventario.
    
    Parámetro:
        inventario_mi (lista): listado de diccionarios con el formato herramienta:cantidad.
    """
    if validar_inventario_vacio(inventario_mi):
        print("\nEl inventario está vacío.")
    else:
        for item in inventario_mi:
            for herramienta, cantidad in item.items():
                print(f" {herramienta:<20} {cantidad:>5} unidad/es")

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
            print("\nOpción 1: CARGA DE HERRAMIENTAS CON EXISTENCIAS INICIALES")

            # Solicito la cantidad de tipos de herramientas a ingresar en las existencias iniciales con la función cantidad_tipos_herramientas().
            # Almaceno el valor en la variable tipos_herramientas que será empleada en funciones posteriores.
            tipos_herramientas = cantidad_tipos_herramientas(inventario)

            # Muestro un mensaje de confirmación para el usuario. 
            if tipos_herramientas:
                print(f"\nSe registrarán {tipos_herramientas} tipos de herramientas en las existencias iniciales.")

                # Permito al usuario cargar la cantidad tipos_herramientas con la funcion registrar_tipos_herramientas.
                inventario = registrar_tipos_herramientas(inventario, tipos_herramientas)
                print(f"\nSe registraron {tipos_herramientas} herramientas en las existencias iniciales.")

        case 2: 
            print("\nOpción 2: VISUALIZACION DE INVENTARIO")

            # Imprimo un listado del inventario.
            mostrar_inventario(inventario)
        case 3:
            print("\nOpción 3: CONSULTA DE STOCK")
        case 4:
            print("\nOpción 4: REPORTE DE AGOTADOS")
        case 5:
            print("\nOpción 5: ALTA DE NUEVO PRODUCTO")
        case 6:
            print("\nOpción 6: ACTUALIZACION DE STOCK (VENTA / INGRESO)")
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
            print("\nOpción 7: SALIR")
            run_menu = False


