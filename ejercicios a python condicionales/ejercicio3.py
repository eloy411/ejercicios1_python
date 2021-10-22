
# 3. Un programa ha de llegir des de teclat un número de l’1 al 10.
# En primer lloc s’ha de garantir que l’entrada es trobi en aquest rang, i si no és així, 
# es mostra un missatge d’error i el programa finalitzarà. Si l’entrada numèrica és correcta, 
# voldrem que l’ordinador imprimeixi per pantalla si el nombre és PRIMER o no. 
# Recordeu que els nombres primers són aquells que només es poden dividir entre 1 i per si mateixos. 
# Del rang de  l’1 al 10 són primers l’1, 2, 3, 5, 7. 

 num = int(input("introduce un valor entre el 1 y 10"))

if num>=1 and num<=10:
     if num == 1 or num == 2 or num == 3 or num ==5 or num == 7:
         print("el numero es primo, primo ;)")
     else:
         print("el numero no es primo, primo :(")
else:
    print("el valor no es valido :O")