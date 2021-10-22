
# 4. Donats dos números per teclat, un programa ha de dir qui és múltiple de qui. En aquest cas,
# es mostrarà un missatge per pantalla “el número X és múltiple de Y”,
# altrament dirà “No ho és”.
# Atenció: l’usuari pot introduir els dos nombres en qualsevol ordre, 
# no els escriurà necessàriament en ordre numèric
#  ( primer el menor, segon el major ).

numX = int(input("introduce un numero"))
numY = int(input("introduce otro numero"))

if numX < numY:
    operacion = numY%numX
    if operacion == 0:
        print(f"{numX} es multiple de {numY}")
    else:
        print("los numeros introducidos no son multiples")
else:
    operacion = numX%numY
    if operacion == 0:
        print(f"{numY} es multiple de {numX}")
    else:
        print("los numeros introducidos no son multiples")