
#     8. Com que mai recordem els rangs de les classes a les adreces 
# IP, decidim fer un programa que ens digui, donada una IP,
#  a quina classe pertany ( A, B, C, D, E ). 
# El programa acceptarà com a entrades 4 xifres, que correspondran a 
# cadascuna dels quatre valors numèrics de l’adreça IP en format decimal. 
# Per exemple, si l’adreça que ens ocupa és 123.1.10.4, 
# l’usuari introduirà les xifres 123, 1, 10 i 4 en aquest ordre ( per octets ).
# Com a millora del programa, 
# seria interessant que també ens digues si es tracta d’una adreça de 
# tipus públic o privat ( recordeu l’adreçament públic i privat )‏
# Finalment, el programa hauria d’imprimir a quina xarxa pertany la IP
# Donada l’entrada per teclat: 192<enter>168 <enter> 10 <enter> 3 <enter>
# La sortida per pantalla  seria:

oct1 = int(input("introduce primer octeto"))
oct2 = int(input("introduce segundo octeto"))
oct3 = int(input("introduce tercer octeto"))
oct4 = int(input("introduce cuarto octeto"))
tipo = "publica"

if oct1 >= 0 and oct1 <= 127:
    clase = 'a'
    if oct1 == 10:
        tipo = "privada"
else:
    if oct1 >= 128 and oct1 <= 191:
        clase = 'b'
        if oct1 == 172 and (oct2 >= 16 and oct2 <= 31):
            tipo = "privada"
    else:
        if oct1 >= 192 and oct1 <= 223:
            clase = 'c'
            if oct1 == 192 and oct2 == 168:
                tipo = "privada"
        else:
            if oct1 >= 224 and oct1 <= 239:
                clase = 'd'
            else:
                if oct1 >= 240 and oct1 <= 255 and (oct4>=0 and oct4<=254):
                    clase = 'e'

print(f"la IP es: {oct1}.{oct2}.{oct3}.{oct4}")
print(f"es de clase: {clase}")
print(f"es de tipo: {tipo}")