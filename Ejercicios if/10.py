cantidad = int(input("Ingrese la cantidad de los productos: "))
valor = int(input("Ingrese el precio unitario del producto: "))
total = valor * cantidad

if cantidad <= 5:
    print(f"el precio total de su compra es: {total}")
if cantidad > 5 and cantidad <= 10:
    descuento = 0.5
    descuento = int(total * descuento)

    print(f"el descuento es del 5%, el precio total de su compra es: {descuento}")

elif cantidad > 10:
    descuento = 0.8
    descuento = int(total * descuento)
    print(f"el descuento es del 8%, el precio total de su compra es: {descuento}")