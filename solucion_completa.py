# funciones
def filtro_jugador(num):
    arch = open("juegos.csv")
    L = []
    for linea in arch:
        datos = linea.strip().split(",")
        nombre = datos[0]
        if num == "s":
            if datos[1] == "1":
                L.append(nombre)
        else:
            if int(datos[1]) >= 2:
                L.append(nombre)
    arch.close()
    return L

def filtro_consola_año(c, a):
    arch = open("juegos.csv")
    L = []
    for linea in arch:
        datos = linea.strip().split(",")
        if c == datos[-2] and a == datos[-1]:
            L.append(datos[0])
    L.sort()
    return L
        
def escribir_archivo(datos):
    arch = open("filtro_juegos.txt", "w")
    for juego in datos:
        arch.write(juego + "\n")
    arch.close()
    print("Archivo creado!!")
    
### MAIN
L_jugador = []
L_consola = []
while True:
    print("***MENU PRINCIPAL***")
    print("1) Filtro jugador.")
    print("2) Filtro consola y año")
    print("3) Escribir archivo.")
    print("4) Salir")
    op = input("Ingrese opcion: ")
    if op == "4":
        print("Saliendo del sistema...")
        break
    elif op == "1":
        players = input("Singleplayer o Multiplayer (s/m)?: ")
        L_jugador = filtro_jugador(players)
        print("EL resultado de la busqueda es (los 10 primeros):" )
        print(L_jugador[:10])
    elif op == "2":
        consola = input("Ingrese nombre de consola: ")
        anio = input("Ingrese año: ")
        L_consola = filtro_consola_año(consola, anio)
        if len(L_consola) == 0:
            print("No hay juegos con esos filtros.")
        else:
            print("EL resultado de la busqueda es (los 10 primeros):" )
            print(L_consola[:10])
    elif op == "3":
        print("*** Menu de escritura ***")
        print("1) Escribir filtro jugador.")
        print("2) Escribir filtro consola y año.")
        op2 = input("Ingrese opcion: ")
        if op2 == "1":
            if len(L_jugador) == 0:
                print("No hay informacion que escribir.")
            else:
                escribir_archivo(L_jugador)
        elif op2 == "2":
            if len(L_consola) == 0:
                print("No hay informacion que escribir.")
            else:
                escribir_archivo(L_consola)           