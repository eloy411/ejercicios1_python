


# 1. Volem construir una calculadora molt simple. 
# L’usuari entrarà per teclat dues xifres. A continuació entrarà un 1 si vol fer el producte de les dues xifres anteriors,
# o bé un 2 si vol sumar les dues xifres. 
# El programa finalment donarà el resultat d’aplicar l’operació escollida sobre els números introduïts.
# Feu servir la sortida en pantalla per a indicar a l’usuari que ha d’introduir en cada moment. Es demana escriure el pseudocodi del programa.


num1 = int(input("introduce el primer valor"))
num2 = int(input("introduce el segundo valor"))
operacion = int(input("introduce 1 si quieres sumar/introduce 2 si quieres multiplicar"))
resultado = 0
if operacion == 1:
    resultado = num1 + num2
    print(resultado)
elif operacion == 2:
    resultado = num1 * num2
    print(resultado)
else:
    print("la operación seleccionada no es correcta")
