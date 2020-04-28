#TODO Futur mirar de sincronitzar amb GoogleCalendar
#TODO Millorar estil de programació: noms variables, format, mirar bones pràctiques. 
#https://docs.google.com/document/d/1PEkRTAWlR4NYJNKJvz9iw4R6m-wJpxDi7xv5tpLPP54/edit 

#TODO Només guarda horari d'un alumne, com ho faràs per guardar més d'un alumne?
#TODO Pista, diccionaris en Pyhton.
alumne1=[[],[],[],[],[]]
dies=["dilluns","dimarts","dimecres","dijous","divendres"]
hores=["8 a 9" , "9 a 10" , "10 a 11" , "11.30 a 12.30" , "12.30 a 13.30" , "13.30 a 14.30"]
for d in dies:
    for h in hores:
        print( "Quina materia tens " + d + " de " + h + "?")
        f=dies.index(d)# Excel·lent
        alumne1[f].append(input().upper())
    print("Els "+d+" l'alumne te "+ str(alumne1[f]) +"; es correcte?")
    resposta=input()
    resultat=resposta.upper()#Cal dues variables?
    if resultat == "NO":
        print("Quin ha sigut l'error?")
        #TODO Escriure en format més de menú. Posant línia a línia opció.
        #TODO NO veig utilitat a tantes opcions. I si es mostra bucle de ves 
        # dient si està bé o no, i cada iteració es canvia una matèria o canviar-lo tot.
        print("Marca la lletra 'a' si l'error és d'una sola matèria; marca la lletra 'b'si l'error és de dues matèries, marca la lletra 'c' si vols tornar a escriure l'horari sencer, marca el numero 1 si vols deixar-ho com esta")
        resposta=input()
        resposta= resposta.upper()
    if resposta == "A":
        print("Indica la matèria incorrecta")
        #TODO Com vigiles que entri bé el nom de la matèria, un cop posi MATES i altre posi Matemàtiques. 
        canvi=(alumne1[f].index(input().upper()))
        print("Digues la materia que correspon")
        alumne1[f][canvi]=input().upper()
    if resposta == "B":
        print("Indica les matèries incorrectes")
        canvi=(alumne1[f].index(input().upper()))
        canvi2=(alumne1[f].index(input().upper()))
        print("Digues les matèries que corresponen")
        alumne1[f][canvi]=input().upper()
        alumne1[f][canvi2]=input().upper()
    if resposta == "C":
        print("Molt bé, ara torna a començar")
        alumne1.clear()
        for h in hores:
            print("Quina materia tens "+d+" de "+h+"?")
            alumne1.append(input().upper())
        print("Els "+d+" l'alumne te: "+ str(alumne1))
    if resposta == "1":
        print()


#TODO Fer dues funcions diferents, anterior és crear horari
#TODO QUe ve ara és cercar quan toca una matèria
#pregunta els dies de cada materia
num=[0,1,2,3,4]
pregunta=input("Quins dies tens...").upper()
for n in num:
    if pregunta in alumne1[n]:
        dato= alumne1[n].index(pregunta)
        print ("Els "+dies[n]+" tens "+ pregunta.lower()+" de "+ hores[dato])
    else:
        print("Els "+dies[n]+" no hi ha "+pregunta.lower())

#TODO Falta fer funció que digui que toca un dia concret