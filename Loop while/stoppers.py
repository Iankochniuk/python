# break -> interrumpe TOTALMENTE las interaciones del loop, osea finaliza el top
# continue -> salta a la siguiente interacion sin ejecutar nada mas en esa

nombre = "PENSAR"
for letra in nombre:
    if letra == "N":
        continue
    print(letra)
