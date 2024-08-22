palabra = "CalcetÍN SUcio"
indice = 0

for letra in palabra.lower():
    indice +=1
    if letra == "a" or letra == "á" or letra == "e" or letra == "é" or  letra == "i" or letra == "í" or letra == "o" or letra == "ó" or letra == "u" or letra == "ú":
        continue 
    else:
        print (f"Posición {indice}: {letra}")


