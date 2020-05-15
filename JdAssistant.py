#TODO Futur mirar de sincronitzar amb GoogleCalendar
#TODO Millorar estil de programació: noms variables, format, mirar bones pràctiques. 
#https://docs.google.com/document/d/1PEkRTAWlR4NYJNKJvz9iw4R6m-wJpxDi7xv5tpLPP54/edit 

alumnes = {}
alumne1 = [ [] , [] , [] , [] , [] ]
dies = [ "dilluns" , " dimarts" , "dimecres" , "dijous" , "divendres" ]
hores = [ "8 a 9" , "9 a 10" , "10 a 11" , "11.30 a 12.30" , "12.30 a 13.30" , "13.30 a 14.30" ]
numeromateria = [ 0 , 1 , 2 , 3 , 4, 5 ]
numdia = [ 0 , 1 , 2 , 3 , 4 ]

def crearHorari():
  for d in dies:
    for h in hores:
        print( "Quina materia tens " + d + " de " + h + "?")
        f = dies.index(d)
        alumne1[f].append(input().upper())
    print( "Els "+d+" l'alumne te "+ str(alumne1[f]) +"; es correcte?" )
    resposta = input( "Escriu si o no " ).upper()
    if resposta == "NO":
        # Pintar codi input en lñínies per ocpió i recollir només input()
        print( "Quin ha sigut l'error?" )
        resposta = input("Marca la lletra 'a' si l'error és d'una sola matèria; marca la lletra 'b'si l'error és de dues matèries, marca la lletra 'c' si vols tornar a escriure l'horari sencer, marca el numero 1 si vols deixar-ho com esta  " )
        resposta = resposta.upper()
    #TODO Canviar usant elif
    if resposta == "A":
        canvi = (alumne1[f].index(input("Indica la matèria incorrecta ").upper()))
        alumne1[f][canvi] = input("Digues la materia que correspon ").upper()
    if resposta == "B":
        canvi = (alumne1[f].index(input("Indica la primera matèria incorrecta ").upper()))
        canvi2 = (alumne1[f].index(input("Indica la segona matèria incorrecta ").upper()))
        alumne1[f][canvi] = input("Digues la primera matèria que correspon ").upper()
        alumne1[f][canvi2] = input("Digues la segona matèria que correspon ").upper()
    if resposta == "C":
        print("Molt bé, ara torna a començar")
        alumne1.clear()
        for h in hores:
            print("Quina materia tens "+d+" de "+h+"?")
            alumne1.append(input().upper())
        print("Els "+d+" l'alumne te: "+ str(alumne1))
    if resposta == "1":
        print()
  return alumne1
print(alumnes)

def materiaHorari():
  preguntamateria = input("Quins dies tens...").upper()
  for n in numdia:
    if pregunta in alumne1[n]:
        dato = alumne1[n].index(preguntamateria)
        print ("Els "+dies[n]+" tens "+ pregunta.lower()+" de "+ hores[dato])
    else:
        print("Els "+dies[n]+" no hi ha "+pregunta.lower())

def diaHorari():
  #TODO Mostrar els dies perquè triï
  preguntadia = input("Quin dia vols saber? ").lower()
  for n in numeromateria:
    if preguntadia in dies:
      dia = dies.index(preguntadia)
      print("Els " + preguntadia + " tens " + alumne1[dia][n])

print("Les funcions disponibles són: /crearhorari o /consultarmateria i /consultardia si ja has creat l'horari")
print("Escriu la funció que vulguis utilitzar")
funcio = input().upper()
if funcio == "/CREARHORARI":
  alumnes[input("Posa el teu nom ")] = str(crearHorari())
elif funcio == "/CONSULTARMATERIA":
  materiaHorari()
elif funcio == "/CONSULTARDIA":
  diaHorari()
else:
  print("Alguna cosa no ha anat bé :(")
