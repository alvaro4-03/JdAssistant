alumne1=[[],[],[],[],[]]
dies=["dilluns","dimarts","dimecres","dijous","divendres"]
hores=["8 a 9" , "9 a 10" , "10 a 11" , "11.30 a 12.30" , "12.30 a 13.30" , "13.30 a 14.30"]
for d in dies:
    for h in hores:
        print( "Quina materia tens " + d + " de " + h + "?")
        f=dies.index(d)
        alumne1[f].append(input().upper())
    print("Els "+d+" l'alumne te "+ str(alumne1[f]) +"; es correcte?")
    resposta=input()
    resultat=resposta.upper()
    if resultat == "NO":
        print("Quin ha sigut l'error?")
        print("Marca la lletra 'a' si l'error és d'una sola matèria; marca la lletra 'b'si l'error és de dues matèries, marca la lletra 'c' si vols tornar a escriure l'horari sencer, marca el numero 1 si vols deixar-ho com esta")
        resposta=input()
        resposta= resposta.upper()
    if resposta == "A":
        print("Indica la matèria incorrecta")
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


#pregunta els dies de cada materia
num=[0,1,2,3,4]
pregunta=input("Quins dies tens...").upper()
for n in num:
    if pregunta in alumne1[n]:
        dato= alumne1[n].index(pregunta)
        print ("Els "+dies[n]+" tens "+ pregunta.lower()+" de "+ hores[dato])
    else:
        print("Els "+dies[n]+" no hi ha "+pregunta.lower())