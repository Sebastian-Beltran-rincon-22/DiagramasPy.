#Isla del tesoro
print("bienvenido a la isla, tu mision sera encontrar el tesoro")
def inicio():
    print("hora de emepezar la aventura")
    decision1 = input("hacia donde seas dirigirte, derecha, izquierda o centro:  ")
    if decision1 == "derecha":
        input("Caiste en un agujero Game over, vuelve a empezar ")
        inicio()
    elif decision1 == "izquierda":
        izquierda = input("que prefieres¿nadar o esperar:  ")
        if izquierda == "esperar":
            puertas = input("que puerta decides tomar escoge el color:  ")
            if puertas == "rojo" and "Rojo":
                print("Eres quemado Game Over, vuelve a empezar ")
                inicio()
            elif puertas == "azul" and "Azul":
                print("deborado por bestias Game Over,vuelve a intentar")
                inicio()
            elif puertas == "amarillo" and "Amarillo":
                print("Has Ganado :D, Felicidades")
            else:
                print("Game over, vuelve a intentar")
    else:
        decision1 == "centro"
        centro = input("que decides Escalar o pasar por arenas movedizas:  ")
        if centro =="arenas movedizas":
            print("entraste en las arenas movedizas")
            arenas = input("decision rapida ¿Dejarse hundir o tomar la soga?:  ")
            if arenas == "desarje hundir" and "Dejarse hundir":
                print("Has sido aplastado por las arenas Game Over, vuelve a intentarlo")
                inicio()
            else:
                print("lograste sostenerte de la soga")
                soga = input("Que prefieres recoger la joya preciosa o irte nadando:  ")
                if soga == "tomar joya" and "Tomar joya ":
                    print("Has caido en una trampa Game Over, vuelve a intentarlo")
                    inicio()
                else:
                    soga == "nadar" and "Nadar"
                    print("fuiste deborado por Cocodrilos Game over, vuelve a intentarlo")
                inicio()                
        else: 
            centro =="Escalar" and "escalar"
            print("Muerte por caida de gtan altura Game Over, vuelve a intentarlo")
        inicio()
inicio()
