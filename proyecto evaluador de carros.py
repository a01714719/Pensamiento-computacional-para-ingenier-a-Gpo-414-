MODELOS = ["toyota", "mazda", "chevrolet", "nissan", "ford"]
# Constante con los modelos válidos

carros_evaluados = []
# Lista anidada para almacenar la información de cada carro evaluado

def evaluar_kilometraje(kilometraje):
    """Evalúa el kilometraje del carro y devuelve su puntaje."""
    if kilometraje <= 50000:
        print("Kilometraje aceptable")
        return 1
    print("Kilometraje demasiado alto")
    return 0

def evaluar_choques(choques):
    """Evalúa los antecedentes de choques del carro y devuelve su puntaje."""
    if choques == 0:
        print("No ha tenido choques")
        return 1
    print("Ha tenido choques")
    return -2


while True:
# programa principal
    print("Vamos a evaluar el carro que vas a comprar.")

    modelo = input("Ingresa el modelo del carro que quieres comprar: ").lower()
    while modelo not in MODELOS:
        print("Modelo no válido. Modelos disponibles:", MODELOS)
        modelo = input("Ingresa nuevamente el modelo del carro: ").lower()

    kilometraje = int(input("Ingresa el kilometraje del carro: "))

    anio = int(input("Ingresa el año del carro que quieres comprar: "))
    while anio < 1926 or anio > 2026:
        print("Error: es imposible que el carro tenga esa edad.")
        anio = int(input("Ingresa nuevamente el año del carro: "))

    choques = int(input("¿Cuántos antecedentes de choques tiene?: "))

    puntaje = 0
    puntaje += evaluar_choques(choques)
    puntaje += evaluar_kilometraje(kilometraje)

    if anio >= 2018:
        print("Año del carro aceptable")
        puntaje += 1
    else:
        print("El carro es muy viejo")

    print("\nResultado de la evaluación:")
    if puntaje == 3:
        print("Este carro es recomendable.")
    elif puntaje == 2:
        print("Puede ser aceptable, revisa los detalles.")
    else:
        print("No recomendamos comprar este carro.")

    carros_evaluados.append([modelo, anio, kilometraje, choques, puntaje])
# Guardar la información en una lista anidada

    repetir = input("\n¿Quieres evaluar otro carro? (si/no): ").lower()
    if repetir == "no":
        print("\nGracias por usar el evaluador de carros.")
        print("\nResumen de carros evaluados:")
        print("Modelo\tAño\tKilometraje\tChoques\tPuntaje")

        for carro in carros_evaluados:
            print(f"{carro[0]}\t{carro[1]}\t{carro[2]}\t\t{carro[3]}\t{carro[4]}")

        break
