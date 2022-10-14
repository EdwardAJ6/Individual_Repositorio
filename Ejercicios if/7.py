cuenta = int(input("Ingrese el valor de El numero cuenta: "))

if cuenta < 150000:
    print(f"El numero cuenta es de: {cuenta}, usted puede  pagar en efectivo")
elif cuenta >= 150000 and cuenta < 300000:
    print(f"El numero cuenta es de: {cuenta}, usted puede  pagar en efectivo o pago por celular")
elif cuenta >= 300000 and cuenta <= 600000:
    print(f"El numero cuenta es de: {cuenta}, usted puede  pagar en efectivo, pago por celular o tarjeta débito")
else:
    print(f"El numero cuenta es de: {cuenta}, usted puede  pagar en efectivo, pago por celular, tarjeta débito o crédito")