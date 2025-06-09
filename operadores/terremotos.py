magnitud = float(input("Ingrese la magnitud del terremoto: "))

if 1 <= magnitud >2:
    print("Not felt or rarely felt")    
elif 2 <= magnitud < 4:
    print("Very rarely causes danger")     
elif 4 <= magnitud < 5:
    print("Damage to weak buildings")
elif 5 <= magnitud < 6:
    print("Damage only poor constructed buildings")
elif 6 <= magnitud < 7:
    print("Damage good constructed")
elif 7 <= magnitud < 8:
    print("Causes damage to almost all buildings")   
elif 8 <= magnitud < 9:
    print("Causes major destrucion")        
elif  magnitud > 9:
    print("Causes unbelievable dange")   
else:
    print("Magnitude not found.")    