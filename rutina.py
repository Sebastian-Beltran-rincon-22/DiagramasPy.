# mi rutina diaria
print("inicio de mi rutina diaria")
levantar = input("levantarme o posponer alarma:  ")
while True:
    if levantar == "levantarse" and "Levantarse":
        print("me levanto a revisar mis pendientes") 
        break
    else:
        levantar == "posponer" and "Posponer"
        print("posponer")
        posponer = int(input("Cuanto se va a posponer:  "))
        while True:
            if posponer >0 and posponer <21:
                print("dormir otro poco")
            break
        else:
            print("levantarse por obligacion")
        break
desayuno = input("que voy a desayunar:  ")
while True:
    if desayuno == "sandwich" and "huevos":
        print("comer y empezar el dia")
    break
else:
    ("corregir escritura")
actividadDia =input("Que actividad realizar en el dia: ")
while True:
    if actividadDia == "pendientes" and "Pendientes":
        revisarC = input("revisar campus de la universidad:  ")
        while True:
            if revisarC =="Si" and "si":
                print("Ingresar al campus")
            trabasOlec = input("Realizar trabajos o lecturas:  ")
            if trabasOlec == "trabajos" and "Trabajos":
                print("empezar adelantar trabajos")
            else:
                trabasOlec == "lecturas" and "Lecturas"
                print("Realizar lecturas pertinentes")
            break
        else:
            print("revisar otros pendientes")
        break
    else:
        actividadDia == "dia de descanso" and "Dia de descanso"
        diaDesca = input("ver algo, salir o jugar:  ")
        while True:
            if diaDesca =="salir" and "Salir":
                print("Salir con familia o amigos")
                break
            elif diaDesca =="jugar" and "jugar":
                print("jugar en el pc ")
                break
            else:
                diaDesca =="ver algo" and "Ver algo"
            print("revisar series pendientes y ver alguna")
            break
    break
