"""
yo quiero ahorrar dinero 
El programa me va a preguntar cuanto quiero ahorrar
y  luego me va a preguntar cuanto ahorro hasta que llegue al objetivo
"""
objetivo = float(input("¿Cuanto dinero queres ahorrar?: "))
ahorrando = 0
fin = False

while ahorrando < objetivo and fin != True:
    cantidad_a_agregar  = float(input("Indica cuanto euros queres guardar:"))
    ahorrando += cantidad_a_agregar
    if cantidad_a_agregar == 11:
        fin = True

print("Has llegado a tu objetivo! FELICITACIONES!!!")    
