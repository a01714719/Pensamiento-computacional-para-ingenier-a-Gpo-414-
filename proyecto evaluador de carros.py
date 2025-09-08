print("Vamos a evaluar el carro que vas a comprar carro")
#aca defino las variables que vamos a utilizar para evaluar el carro
kilometraje = int(input("Ingresa el kilometraje del carro que quieres comprar: "))
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