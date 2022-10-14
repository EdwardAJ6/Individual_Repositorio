
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print(f"El numero mayor es: {numero1}, el segundo es: {numero2} y el menor es: {numero3}")

elif numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
    print(f"El numero mayor es: {numero2}, el segundo es: {numero1} y el menor es: {numero3}")

elif numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
    print(f"El numero mayor es: {numero3}, el segundo es: {numero1} y el menor es: {numero2}")

elif numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
    print(f"El numero mayor es: {numero3}, el segundo es: {numero2} y el menor es: {numero1}")