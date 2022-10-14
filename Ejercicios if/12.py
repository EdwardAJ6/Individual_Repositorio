
print("Digite 1 si es mujer, digite 2 si es hombre")

edad = int(input("Digite su edad: "))
genero = int(input("Digite su genero: "))

if genero == 1:
    pulsaciones =(220 - edad) / 10
    print(f"sus pulsaciones cada 10 segundos con respecto a su edad {pulsaciones}")
elif genero == 2:
    pulsaciones = (210 - edad) / 10 
    print(f"sus pulsaciones cada 10 segundos con respecto a su edad {pulsaciones}")