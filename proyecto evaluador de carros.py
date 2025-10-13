modelos = ["toyota", "mazda", "chevrolet", "nissan", "ford"]
carros_evaluados = []
while True:
    print("Vamos a evaluar el carro que vas a comprar carro")
    modelo=input("Ingresa el modelo del carro que quieres comprar: ")
    while modelo not in modelos:
        print("Modelo no válido. Modelos disponibles:", modelos)
        modelo = input("Ingresa nuevamente el modelo del carro: ")
    #aca defino las variables que vamos a utilizar para evaluar el carro
    kilometraje = int(input("Ingresa el kilometraje del carro que quieres comprar: "))
    año = int(input("Ingresa el año del carro que quieres comprar: "))
    while año < 1926 or año >2026:
        print("Error, es imposible que el carro tenga esa edad")
        año = int(input("Ingresa el año del carro que quieres comprar: "))

    choques = int(input("cuantos antecedentes de choques?: "))
    puntaje=0
    #aca evaluamos el kilometraje
    def evaluar_kilometraje(kilometraje):
        if kilometraje <= 50000:
            print("Kilometraje aceptable")
            return 1
        else:
            print("Kilometraje demasiado alto")
            return 0
    #aca evaluamos choques
    def evaluar_choques(choques):
        if choques == 0:
            print("No ha tenido choques")
            return 1
        else:
            print("Ha tenido choques")
            return -2
    puntaje += evaluar_choques(choques)
    puntaje += evaluar_kilometraje(kilometraje)
    #aca evaluamos año 
    if año >= 2018:
        print("Año del carro aceptable")
        puntaje += 1
    else:
        print("El carro es muy viejo")

    # Resultado final
    if puntaje == 3:
        print("Este carro es recomendable")
    if puntaje == 2:
        print("Puede ser aceptable, revisa los detalles")
    else:
        print("No recomendamos comprar este carro ")
    
    carros_evaluados.append([modelo, año, kilometraje, choques, puntaje])
    repetir = input("¿Quieres evaluar otro carro? (si/no): ")
    if repetir == "no":
        print("Gracias por usar el evaluador de carros ")
        print("\nResumen de carros evaluados:")
        print("Modelo  Año  Kilometraje  Choques  Puntaje")
        for carro in carros_evaluados:
            print(carro)
        break