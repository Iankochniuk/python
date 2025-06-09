"""
Seguir la receta para hacer galletas de chocolate. Hay que poner
100ml de leche, 30g de harina y 10g de chocolate.Ayudarse
del while para hacer esto. En caso de que el usuario se pase con los 
ingredientes. tiralos y volver a cero
"""
harina = 0
leche = 0
chocolate = 0

while leche < 100 or harina < 30 or chocolate < 10:
    leche += int(input("ML de leche a agregar:"))
    harina += int(input("Gr de harina a agregar:"))
    chocolate += int(input("Gr de chocolate a agregar:"))

    if leche > 100 or harina > 30 or  chocolate > 10:
        #RESETEAR TODAS LAS VARIABLE
        print("Te exediste con los ingrediente enpieza de nuevo.")
        leche = 0
        harina = 0
        chocolate = 0 

print("Felicidades puedes comer tus galleta en 30 minutos!")        

