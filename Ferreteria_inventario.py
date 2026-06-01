# ============================================================= #
# FUNCIONES DE MENU
# ============================================================= #

# Se define una funcion que presenta el menu principal.
def menu_principal():
    print("""\n MENU PRINCIPAL
    1. Carga inicial de herramientas.
    2. Visualización del inventario.
    3. Consulta de stock.
    4. Reporte de agotados.
    5. Alta de nuevo producto.
    6. Actualización de stock.
    7. Salir.""")

# Se define una funcion que muestra el menu secundario de la opcion 6. Actualizacion de stock.
def menu_secundario():
    print("""\n MENU ACTUALIZACION DE STOCK.
    1. Venta.
    2. Ingreso.
    3. Volver al menu principal.""")


# ============================================================= #
# FUNCIONES DE VALIDACION DE INGRESO DE DATOS
# ============================================================= #
# Se define la funcion validar_opcion que valida que el usuario ingrese un numero correspondiente al menu principal y secundario.
def validar_opcion(minimo_vo,maximo_vo):
    while True:
        try:
            opcion_vo = int(input("Ingrese una opción: "))
            if minimo_vo <= opcion_vo <= maximo_vo:
                return opcion_vo
            else:
                print(f"Solo se permite el ingreso de los números {minimo_vo} a {maximo_vo}")
        except ValueError:
            print("Ingrese el valor númerico correspondiente a la acción detallada en el menú.")
        except Exception as e:
            print(f"""Ocurrió el siguiente error: {type(e).__name__}. 
            Por favor, tome nota del error y comuniquese con el servicio de soporte de la aplicación.
            Lamentamos las molestias ocasionadas.""")


# ============================================================= #
# PROGRAMA PRINCIPAL
# ============================================================= #

menu_principal()
opcion = validar_opcion(1,7)

