
print("Ingresee el numero de la figura geometrica que deseé calcular el area \n 1 para cuadrado \n 2 para rectángulo \n 3 para triángulo \n 4 para círculo \n 5 para rombo \n 6 para trapecio")

opcion = int(input("Ingrese el numero de la figura geométrica: "))

if opcion == 1:
    print(" Area del Cuadrado ")
    numero1 = float(input("Ingrese el lado del cuadrado: "))
    area = numero1 * numero1
    print(f"El area del cuadrado es: {area}")

elif opcion == 2: 
    print(" Area del Rectángulo ")
    numero1 = float(input("Ingrese la base: "))
    numero2 = float(input("Ingrese la altura: "))

    area = numero1 * numero2
    print(f"El area del rectángulo es: {area}")

elif opcion == 3:
    print(" Area del Triángulo ")
    numero1 = float(input("Ingrese la base: "))
    numero2 = float(input("Ingrese la altura: "))

    area = (numero1 * numero2) / 2
    print(f"El area del triángulo es: {area}")

elif opcion == 4:
    print(" Area del Círculo ")
    numero1 = float(input("Ingrese el radio del circulo: "))
    area = (numero1**2) * 3.14
    print(f"El area del círculo es: {area}")

elif opcion == 5:
    print(" Area del Rombo ")
    numero1 = float(input("Ingrese la diagonal Mayor: "))
    numero2 = float(input("Ingrese la diagonal Menor: "))

    area = (numero1* numero2) / 2
    print(f"El area del Rombo es: {area}")

elif opcion == 6:
    print(" Area del Trapecio ")
    numero1 = float(input("Ingrese la base Mayor: "))
    numero2 = float(input("Ingrese la base Menor: "))
    numero3 = float(input("Ingrese la altura: "))

    area = ((numero1 + numero2) * numero3) / 2
    print(f"El area del trapecio es: {area}")