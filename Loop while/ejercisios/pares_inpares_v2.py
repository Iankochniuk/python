"""
Escriba un  programa que pregunte cuantos numeros se va a
introducir. pida esos nuemros y diga al fianal cuantos han sido pares y
cuantos inpares
"""
numeros_a_chequear = int(input("¿Cuantos numeros vas a ingresar?:"))

contador_numero = 0
contador_impar = 0
contador_par = 0

while contador_numero < numeros_a_chequear:
    numero = int(input("Ingresa un numero: "))
    #chequeo si es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un nuemero par")
        contador_par += 1
    else:
        print(f"{numero} es un numero impar ")
        contador_impar +=1    

    contador_numero += 1

print(f"El total de numeros pares ha sido: {contador_par}")
print(f"El total de numero impares ha sido: {contador_impar}")    