puntuacion = int(input("Ingrese una puntacion entre 0 y 10: "))
puntuacion_permitida = range(0,11)

if puntuacion in puntuacion_permitida:
    if puntuacion >=9:
        print("Su nota es A.")
    elif puntuacion >=8:
        print("Su nota es B.")
    elif puntuacion ==7:
        print("Su nota es C.")
    elif puntuacion ==6:
        print("Su nota es D:")   
else:
    print("Error! Puntuacion fuera de rango")            





