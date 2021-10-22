
    # 5. Donada una entrada per teclat corresponent a la nota numèrica d’un examen, 
    # el programa ens imprimirà per pantalla la qualificació textual corresponent:
    # • Menor de 5 : 			Insuficient
    # • De 5 a 6(no inclòs):		Suficient
    # • De 6 a 7(no inclòs) 		Bé
    # • De 7 a 8’5(no inclòs)		Notable
    # • De 8’5 a 10(no inclòs)	Excel·lent
    # • 10				Matricula d’honor

    nota = float(input("introduce la nota de Anthony :O OMG!"))

    if nota >= 0 and nota < 5:
        print("SUSPENDIDISIMO")
    elif nota >= 5 and nota < 6:
        print("justito justito... pero apruebas")
    elif nota >= 6 and nota < 7:
        print("Bien pero puedes mejorar")
    elif nota >= 7 and nota < 9:
        print("Notable ;)")
    elif nota >= 9 and nota < 10:
        print("Excelente maquinola")
    elif nota == 10:
        print("ERES DIOS")
    else:
        print("Aureliano haga el favor de introducir bien la nota")
