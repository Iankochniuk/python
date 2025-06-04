print("Bienvenido usuario")
 
edad = int(input("Ingrese su edad: "))
pais = input("¿Es usted Argentino o tiene ciudadania Argentina?")
#nacionalidad = int(input("Ingrese su nacionalidad: "))

if edad >= 18 and pais == "si":
    print("Te es obligatorio Votar")    
elif edad >= 16 and edad < 18 and pais == "si":
    print("Puede votar pero no es obligatorio ")
elif edad < 16 and pais == "si" :
    print("No puede votar por minoria de edad") 
else:  
    print("No puedes votar porque no eres argentino")  


    
    