
talla = float(input("Ingrese su talla: "))
peso = float(input("Ingrese su peso: "))

formula = peso / (talla**2)

if formula < 20:
    print("Usted esta desnutrido")
elif formula >= 20 and formula < 25:
    print("Usted tiene un peso normal")
elif formula >= 25 and formula < 30:
    print("Usted tiene sobrepeso")
elif formula >= 30 and formula < 35:
    print("Usted tiene obesidad grado 1")
elif formula >= 35 and formula < 40:
    print("Usted tiene obesidad grado 2")
else:
    print("Usted tiene obesidad grado 3")