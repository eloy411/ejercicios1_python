
# 2. Hem de fer un programa que ens digui si un any que li indiquem és any de traspàs (bisiesto ). 
# Sabem que els anys de traspàs són tots aquells múltiples de quatre, però que no són múltiples de 100. 
# Com a excepció, si que ho són els múltiples de 400.
#     • ex. L’any 200 NO és de traspàs 
#     • ex. L’any 204 SI és de traspàs
#     • ex. L’any 800 SI és de traspàs
# El programa llegirà un any i mostrarà un missatge “any de traspàs” o “any normal” segons el cas.
#  Es demana escriure el pseudocodi.

age = int(input("introduce un año"))

if age%4==0 and age%100 != 0 or (age%400==0):
    print("este año es bisiesto")
else:
    print("este año no es bisiesto, loki")
