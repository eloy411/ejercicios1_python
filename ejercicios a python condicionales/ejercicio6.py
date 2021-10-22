# 6. En una empresa necessiten un petit programa que permeti calcular
# l’import que han de pagar als treballadors. Els pagaments es fan de forma setmanal.
# • Per a cada assalariat es recullen via teclat les següents dades:
# • Número d’hores setmanals treballades a la setmana
# • Preu per hora ( és diferent per a cada treballador )‏
# Es considera que un treballador comença a fer hores extres a 
# partir de la hora 36 (la 35 és part de l’horari setmanal). 
# Les hores extres es paguen un 50% més que les hores normals.
# El programa ha d’imprimir per pantalla l’import final, 
# tenint en compte el preu hora indicat i si hi ha hores extres o no.

numH = float(input("introduce numero de horas"))
precioH = float(input("introduce precio de hora"))

if numH > 35:
    total = (numH - 35) * (precioH * 1.5) + (35 * precioH)
else:
    total = numH * precioH
print(f"el numero de horas son {numH} por la cual cobrara un total de {total}€")