       #calculadora del 1 al 10
"""
rango =  range (1,11)

numero =int(input("¿Que numero queres multiplicar?: "))

for num in rango:
    print(f"{numero}*{num} ---> {numero+num}")
"""
          #caulculadora V 2.0    
print("------CAULCULADORA V 2.0------")
nuemro_a_multiplicar = range (1,11)
multiplicadores = range (1,11)

for numero in nuemro_a_multiplicar:
    #tabla
    print(f"--------TABLA DEL {numero}:")
    for mult in multiplicadores:
        print(f"{numero}*{mult} ---> {numero*mult}")