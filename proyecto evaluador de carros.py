print("Vamos a evaluar el carro que vas a comprar carro")
#aca defino las variables que vamos a utilizar para evaluar el carro
kilometraje = int(input("Ingresa el kilometraje del carro que quieres comprar: "))
año = int(input("Ingresa el año del carro que quieres comprar: "))
choques = int(input("cuantos antecedentes de choques?: "))
puntaje=0
#aca evaluamos el kilometraje
if kilometraje <= 50000:
    print("Kilometraje aceptable")
    puntaje += 1
else:
    print("Kilometraje demasiado alto")
# aca evaluamos el año
if año >= 2018:
    print("Año del carro aceptable")
    puntaje += 1
else:
    print("El carro es muy viejo")
#aca evaluamos choques
if choques == 0:
    print("No ha tenido choques")
    puntaje += 1
else:
    print("Ha tenido choques ")
    puntaje-=2
# Resultado final
if puntaje == 3:
    print("Este carro es recomendable")
if puntaje == 2:
    print("Puede ser aceptable, revisa los detalles")
else:
    print("No recomendamos comprar este carro ")