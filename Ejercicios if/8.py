llantas = int(input("Ingrese el numero de llantas que  desea llevar "))

if llantas <= 5 :
    print(f"El precio unitario es de $240000, el precio total es: {240000 * llantas}")
elif llantas == 6 or llantas == 7:
    print(f"El precio unitario es de $221000, el precio total es: {221000 * llantas}")
else:
    print(f"El precio unitario es de $180000, el precio total es: {180000 * llantas}")