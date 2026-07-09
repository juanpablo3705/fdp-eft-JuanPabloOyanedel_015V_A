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
        if plataforma == valores[1]:
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
                    busqueda_precio(p_min, p_max, inventario, juegos)
                    break
                else:
                    print("Error, el precio mínimo debe ser menor o igual al precio máximo y ambos deben ser mayor o igual a cero.")
        case 3:
            print("3")
        case 4:
            print("4")
        case 5:
            print("5")
        case 6:
            print("Programa finalizado.")
            break