print("Bienvenido al Himalaya")

edad = int(input("Ingresa tu edad: "))

if 18 <= edad < 80:
    estudios_secundarios = input("¿Terminaste tus estudios secundarios? (si/no): ").strip().lower()

    if estudios_secundarios == "si":
        print("Puede registrarse.")
    elif estudios_secundarios == "no":
        print("Lo sentimos, debe completar los estudios secundarios para registrarse.")
    else:
        print("Respuesta no válida. Por favor, escriba 'si' o 'no'.")
else:
    print("No puedes inscribirte a la universidad.")
