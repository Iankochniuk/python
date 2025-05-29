"""
IF condicion:
    intrucciones
ELIF condicion2:
    otras instrucciones
ELSE:
    otras instruciones        
"""
#solo una condicion puede ser verdadera y va ser ejecutado 
#En caso de ninguno ser verdadero, se ejecuta el else 

edad =  int(input("¿Cual es su edad?"))

#chequear si es menor a 16 años
if edad < 16:
    print("No es mayo de edad  y no puede votar")
elif edad >=16 and edad < 18:
    print("No eres mayor de edad pero puedes votar, es opcional")    
else:
    print("Eres mayor de edad y tienes obligacion de votar")    