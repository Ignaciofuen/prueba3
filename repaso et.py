l=[]
l2=[]
l3=[]
def filtro_jugador():
    
    arch=open("juegos.csv","r")
    for linea in arch:
        datos=linea.strip().split(",")
        nombre=datos[0]
        n=int(datos[1])
        if player =="s" and n ==1:
            l.append(nombre)
        
        if player =="m" and n>1:
            l2.append(nombre)
    arch.close()
    if len (l)==0:
        print("No hay juegos para un jugador")
    else:
        print("juegos singleplayer: ",l[:10])
    if len (l2)==0:
        print("no hay juegos para mas de un jugador")
    else:
        print("juegos multijugador: ",l2[:10])
def filtro_consola(a,b):
    arch =open("juegos.csv","r")
    for linea in arch:
        datos=linea.strip().split(",")
        if a==datos[-2] and b==datos[-1]:
            l3.append(datos[0])
    arch.close()
    return l3




while True:
    print("\nMenú:")
    print("1. filtro jugador")
    print("2. filtro consola")  
    print("3. Guardar archivos")
    print("4. Salir")
    opcion=input("Ingrese una opción: ")

    if opcion=="1":
        player = input("ingrese opcion de juego :(m) para multiplayer o (s)para single player :")
        filtro_jugador()
    elif opcion=="2":
        consola=input("ingrese nombre consola")
        ano=input("ingrese ano")
        l_consola=filtro_consola(consola,ano)
        print(l_consola)

    
