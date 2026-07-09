# funcion mostrar menu:
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

# funcion leer opcion:
def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción del menú: "))
            if (opcion >= 1) and (opcion <= 6):
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

# funcion opcion 1 - stock por plataforma:
def stock_plataforma(plataforma, juegos, inventario):
    contador_stock = 0
    for clave, valores in juegos.items():
        if plataforma.lower() == valores[1].lower():
            contador_stock = contador_stock + inventario[clave][1]
    print(f"El stock para la plataforma seleccionada es de: {contador_stock}.")

# funcion opcion 2 - busqueda de juegos por rango de precios:
def busqueda_precio(p_min, p_max, inventario, juegos):
    lista_juegos = []
    for clave, valores in inventario.items():
        if (valores[0] >= p_min) and (valores[0] <= p_max) and (valores[1] != 0):
            titulo = juegos[clave][0]
            codigo = clave
            lista_juegos.append(f"{titulo}--{codigo}")
    if len(lista_juegos) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        lista_juegos.sort()
        print(lista_juegos)

# funcion buscar codigo:
def buscar_codigo(codigo, inventario):
    return codigo in inventario

# funcion opcion 3 - actualizar precio de juego:
def actualizar_precio(codigo, nuevo_precio, inventario):
    if buscar_codigo(codigo, inventario):
        inventario[codigo][0] = nuevo_precio
        return True
    else:
        return False
    
# funcion opcion 4 - validar codigo:
def validar_codigo(codigo, inventario):
    if (codigo.strip() == "") or (buscar_codigo(codigo, inventario) == True):
        return False
    else:
        return True
    
# funcion opcion 4 - validar titulo:
def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar plataforma:
def validar_plataforma(plataforma):
    if plataforma.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar genero:
def validar_genero(genero):
    if genero.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar clasificacion:
def validar_clasificacion(clasificacion):
    if (clasificacion == "E") or (clasificacion == "T") or (clasificacion == "M"):
        return True
    else:
        return False
    
# funcion opcion 4 - validar multiplayer:
def validar_multiplayer(multiplayer):
    if (multiplayer == "s") or (multiplayer == "n"):
        return True
    else:
        return False

# funcion opcion 4 - validar editor:
def validar_editor(editor):
    if editor.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar precio:
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False
    
# funcion opcion 4 - validar stock:
def validar_stock(stock):
    if stock >= 0:
        return True
    else:
        return False
    
# funcion opcion 4 - agregar juego:
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    if buscar_codigo(codigo, inventario):
        return False
    else:
        juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
        inventario[codigo] = [precio, stock]
        return True

# funcion opcion 5 - eliminar juego:
def eliminar_juego(codigo, juegos, inventario):
    if buscar_codigo(codigo, inventario):
        del juegos[codigo]
        del inventario[codigo]
        return True
    else:
        return False

# programa principal:
juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
}
inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2]
}
while True:
    mostrar_menu()
    opcion_elegida = leer_opcion()
    match opcion_elegida:
        case 1:
            plataforma = input("Ingrese el nombre de la plataforma a revisar su stock de juegos: ").strip()
            if len(juegos) == 0:
                print("Error, no hay juegos registrados.")
            else:
                stock_plataforma(plataforma, juegos, inventario)         
        case 2:
            while True:
                try:
                    p_min = int(input("Ingrese un precio mínimo para buscar por rango: "))
                    p_max = int(input("Ingrese un precio máximo para buscar por rango:  "))
                except ValueError:
                    print("Debe ingresar valores enteros")
                    continue
                if (p_min >= 0) and (p_max >= 0) and (p_min <= p_max):
                    break
                else:
                    print("Error, el precio mínimo debe ser menor o igual al precio máximo y ambos deben ser mayor o igual a cero.")
            busqueda_precio(p_min, p_max, inventario, juegos)
        case 3:
            while True:
                codigo = input("Ingrese el código del juego al que desea modificar su precio: ").strip().upper()
                while True:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if nuevo_precio > 0:
                            break
                        else:
                            print("Debe ingresar valores enteros positivos.")
                    except ValueError:
                        print("Debe ingresar valores enteros.")
                if actualizar_precio(codigo, nuevo_precio, inventario):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                otro_intento = input("¿Desea actualizar otro precio (s/n)?").strip().lower()
                if otro_intento == "s":
                    print("Actualizando otro precio...")
                elif otro_intento == "n":
                    break
                else:
                    print("Debe seleccionar s o n. Inténtelo otra vez.")
                    break
        case 4:
            while True:
                codigo = input("Ingrese el código del juego a agregar: ").strip().upper()
                if validar_codigo(codigo, inventario):
                    break
                else:
                    print("Error, el código no debe estar vacío ni ser sólo espacios en blanco y no debe existir previamente.")
            while True:
                titulo = input("Ingrese el título del juego a agregar: ").title()
                if validar_titulo(titulo):
                    break
                else:
                    print("Error, el título no debe estar vacío ni ser sólo espacios en blanco.")
            while True:
                plataforma = input("Ingrese la plataforma del juego a agregar: ").strip()
                if validar_plataforma(plataforma):
                    break
                else:
                    print("Error, la plataforma no debe estar vacía ni ser sólo espacios en blanco.")
            while True:
                genero = input("Ingrese el género del juego a agregar: ").strip().lower()
                if validar_genero(genero):
                    break
                else:
                    print("Error, el género no debe estar vacío no ser sólo espacios en blanco.")
            while True:
                clasificacion = input("Ingrese la clasificación del juego a agregar (E/T/M): ").strip().upper()
                if validar_clasificacion(clasificacion):
                    break
                else:
                    print("Error, la clasificación debe ser exactamente E, T ó M.")
            while True:
                multiplayer = input("Ingrese si el juego es multiplayer (s = sí, n = no): ").strip().lower()
                if validar_multiplayer(multiplayer):
                    if multiplayer == "s":
                        multiplayer = True
                    else:
                        multiplayer = False
                    break
                else:
                    print("Error, debe ingresar sólo s ó n.")
            while True:
                editor = input("Ingrese el editor del juego a agregar: ")
                if validar_editor(editor):
                    break
                else:
                    print("Error, el editor no debe estar vacío o ser sólo espacios en blanco.")
            while True:
                try:
                    precio = int(input("Ingrese el precio del juego a agregar: "))
                    if validar_precio(precio):
                        break
                    else:
                        print("Error, el precio debe ser un número entero mayor que cero.")
                except ValueError:
                    print("Error, el precio debe ser números enteros.")
            while True:
                try:
                    stock = int(input("Ingrese el stock del juego a agregar: "))
                    if validar_stock(stock):
                        break
                    else:
                        print("Error, el stock debe ser un número entero mayor o igual a cero.")
                except ValueError:
                    print("Error, el stock deben ser números enteros.")
            if agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
                print("Juego agregado")
            else:
                print("El código ya existe")
        case 5:
            codigo = input("Ingrese el código del juego que se desea eliminar: ").strip().upper()
            if eliminar_juego(codigo, juegos, inventario):
                print("Juego eliminado")
            else:
                print("El código no existe")
        case 6:
            print("Programa finalizado.")
            break