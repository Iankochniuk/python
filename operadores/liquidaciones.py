print("Bienvenido Usuario")


salario = int(input("Ingresa tu salario:"))
años = int(input("¿Cuantos años trabajaste:  "))
dias = int(input("¿Cuantos dias trabajo?: "))
meses = int(input("¿Cuantos meses trabajo?: "))
total_antiguedad = años
 
indemnisacion = salario*años
liquidacion =  salario/dias
liquidacion_2 = liquidacion*dias




if años > 1 and meses > 3:
    indemnisacion = salario*(años+1)
elif años >= 1 and meses<3:
    indemnisacion = salario*años

else:
    indemnisacion = 0
    print("No hay indemnizacion")    
    

print("Su Liquidacion seria: $" +str(liquidacion_2))
print(f"La indemnizacion es de: ${indemnisacion}")
print(f"El total a percibir es de $ {liquidacion+indemnisacion}")