palabra = "paralelepípedo"
indice = 0

for var in palabra:
    indice +=1
    if var == "a" or var == "e" or var == "i" or var == "í" or var == "o" or var == "u":
        continue 
    else:
        print (f"Posición {indice}: {var}")


