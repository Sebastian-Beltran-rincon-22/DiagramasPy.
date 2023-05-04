#actividad
frutas = ["manzana","pera","kiwi","piña","mandarina"]
for i in frutas:
    print(i)
for fruta in frutas:
    print("las letras de la "+fruta+":"  )
    for i in fruta:
        print(i)
#actividad
numeros =[10,20,30,40,50,60,70,80,90]
suma = 0
for i in numeros:
    suma += i
    print("la suma de los numeros es:", suma)
#actividad
caracteres = input("escribe lo que gustes y lo veras en cadena:  ")
for i in caracteres:
    print(i)
#actividad
palabras = ["leon", "perro", "leopardo", "gato", "elefante"]
letra = input("Ingrese la letra inicial: ")
for i in palabras:
    if i.startswith(letra):
        print(i)
#actividad
lista1 = [2, 4, 6, 8, 10]
lista2 = [4, 8, 12, 16, 20]
lista3suma = []
for i in range(len(lista1)):
    lista3suma.append(lista1[i] + lista2[i])
print("La lista 3 es :", lista3suma)
#actividad
numero = int(input("ingresar el numero que desee saber la tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

