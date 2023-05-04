#fritando un huevo
print("Vamos a preparar un huevo")
huevo = input("Desea ir a la cocina:  ")
if huevo =="si" and "Si":
    ()
else:
    print("Vuelva mas tarde")
estufa = input("Desea prender la estufa:  ")
if estufa == "si" and "Si":
    print("estufa encendida")
else:
    print("Estufa apagada")
while True:
    numHuevos = int(input("Cuantos huevos desea hacer:  "))
    if numHuevos > 0:
        break
    else:
        print("deben ser 1 o mas huevos")
while True:
    comoHuevos = input("como desea preparar los huevos elija una sola opcion:  ")
    if comoHuevos == "fritos" and "revueltos" and "pericos":
        print("Se encuentran preparando espere por favor...")
        break
    else: 
        print("error revidar como desea los huevos valido, fritos, revueltos y pericos ")
comerYa = input("desea comer los huevos ya:  ")
if comerYa == "si" and "Si":
    print("buen provecho")
else:
    print("vuelva en otro momento por ellos")
