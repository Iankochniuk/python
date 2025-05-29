"""
Escribe un programa para calcular el mas grande de los numeros 
ingresados por el usuario
"""

numero_1 = int(input("ingresa un nuemro: "))
numero_2 = int(input("ingresa un segundo numero: "))

if numero_1 > numero_2:
    print(f"{numero_1} es mayor a {numero_2}.")
elif numero_1 == numero_2: 
    print("Los numeros son Iguales ")
else:
    print(f"{numero_2} es mayor a {numero_1}")    



