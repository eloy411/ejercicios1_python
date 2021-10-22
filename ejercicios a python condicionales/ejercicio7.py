#  7. Volem fer un programa que donades dues entrades numèriques per teclat:
# any  ( ex. 1998)‏
# mes (1-gener, 2 febrer, 3-març....) 
# ens indiqui per pantalla quants dies té aquest mes en concret.
# Nota: Tingueu en compte que pels anys de traspàs febrer té 29 dies.
# Com a recordatori:
# la tabla esta en el moodle.

age = int(input("introduce un año"))
month = int(input("1.Enero, 2.Febrero, 3.Marzo, 4.Abril, 5.Mayo, 6.Junio, 7.Julio, 8.Agosto, 9.Septiembre, 10.Octubre, 11.Noviembre, 12.Diciembre"))

calculo = age%4 == 0 and age%100 != 0 or (age%400 == 0)

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("el mes tiene 31 dias")
else:
    if month == 2 and calculo:
        print("febrero tiene 29 dias por que el año es bisiesto")
    elif month == 2 and calculo == False:
        print("febrero tiene 28 dias porque el año no es bisiesto")
    else:
        print("el mes tiene 30 dias")