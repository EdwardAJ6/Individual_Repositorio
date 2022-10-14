rango = int(input(" Ingrese el tamaño de la pizza, recuerde que el rango es de 1 a 3: "))
ingredientes = int(input(" Ingrese  el numero de ingredientes adicionales: "))

valmultiplicacion =  4000 * ingredientes
# print(valmultiplicacion)

if rango == 1:
    precio = 15000
    print(f" el precio a pagar es de: {precio + valmultiplicacion}")

elif rango == 2:
    precio = 24000
    print(f" el precio a pagar es de: {precio + valmultiplicacion}")

elif rango == 3:
    precio = 36000
    print(f" el precio a pagar es de: {precio + valmultiplicacion}")

else:
    print("Error")
