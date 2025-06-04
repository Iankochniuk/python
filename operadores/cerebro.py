potencial_reposo = -60 
umbral_exitacion = range(-55,-49)
mv = int(input("ingrese los mV a ejecutar en la neurona:"))

resultado = potencial_reposo+mv
print(f"la neurona tiene un potencial de {resultado}mv")

if resultado in umbral_exitacion:
    print("Neurona exitada")
else:
    print("NO paso nada")