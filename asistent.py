#TODO Futur mirar de sincronitzar amb GoogleCalendar
#TODO Millorar estil de programació: noms variables, format, mirar bones pràctiques. 
#https://docs.google.com/document/d/1PEkRTAWlR4NYJNKJvz9iw4R6m-wJpxDi7xv5tpLPP54/edit 

alumnes = {}
alumne1 = [ [] , [] , [] , [] , [] ]
dies = [ "dilluns" , " dimarts" , "dimecres" , "dijous" , "divendres" ]
hores = [ "8 a 9" , "9 a 10" , "10 a 11" , "11.30 a 12.30" , "12.30 a 13.30" , "13.30 a 14.30" ]
numeromateria = [ 0 , 1 , 2 , 3 , 4, 5 ]
numdia = [ 0 , 1 , 2 , 3 , 4 ]
deures = {}
def crearHorari():
  for d in dies:
    for h in hores:
        print( "Quina materia tens " + d + " de " + h + "?")
        f = dies.index(d)
        alumne1[f].append(input().upper())
    print( "Els "+d+" l'alumne te "+ str(alumne1[f]) +"; es correcte?" )
    resposta = input( "Escriu si o no " ).upper()
    if resposta == "NO":
        # Pintar codi input en línies per ocpió i recollir només input()
        print( "Quin ha sigut l'error?" )
        print( "Marca la lletra 'a' si l'error és d'una sola matèria; marca la lletra 'b'si l'error és de dues matèries, marca la lletra 'c' si vols tornar a escriure l'horari sencer, marca el numero 1 si vols deixar-ho com esta  " )
        resposta = input()
        resposta = resposta.upper()
    if resposta == "A":
        canvi = (alumne1[f].index(input("Indica la matèria incorrecta ").upper()))
        alumne1[f][canvi] = input("Digues la materia que correspon ").upper()
    elif resposta == "B":
        canvi = (alumne1[f].index(input("Indica la primera matèria incorrecta ").upper()))
        canvi2 = (alumne1[f].index(input("Indica la segona matèria incorrecta ").upper()))
        alumne1[f][canvi] = input("Digues la primera matèria que correspon ").upper()
        alumne1[f][canvi2] = input("Digues la segona matèria que correspon ").upper()
    elif resposta == "C":
        print("Molt bé, ara torna a començar")
        alumne1.clear()
        for h in hores:
            print("Quina materia tens "+d+" de "+h+"?")
            alumne1.append(input().upper())
        print("Els "+d+" l'alumne te: "+ str(alumne1))
    else:
        print()
  return alumne1

def materiaHorari():
  preguntamateria = input("Quins dies tens...").upper()
  for n in numdia:
    if pregunta in alumne1[n]:
        dato = alumne1[n].index(preguntamateria)
        print ("Els "+dies[n]+" tens "+ pregunta.lower()+" de "+ hores[dato])
    else:
        print("Els "+dies[n]+" no hi ha "+pregunta.lower())

def diaHorari():
  print(dies)
  preguntadia = input("Quin dia vols saber? ").lower()
  for n in numeromateria:
    if preguntadia in dies:
      dia = dies.index(preguntadia)
      print("Els " + preguntadia + " tens " + alumne1[dia][n])
   
def apuntarDeures():
  materia = input("Digues la matèria que s'ha d'apuntar ")
  dia = input("Indica per a quin dia ")
  quins_deures = input("Escriu que vols apuntar ")
  if materia not in deures:
    deures[materia] = []
    deures[materia].append({dia : quins_deures})
  else:    
    deures[materia].append({dia : quins_deures})
  return deures
        
def ConsultarDeuresxMateria():
  materia = input("Digues la matèria de la que vols saber els deures ")
  if materia in deures.keys():
    print(deures[materia])
  else:
    print ("Alguna cosa no ha anat bé   = (")
  return deures

def ConsultarDeuresxDia():
  quin_dia = input("Digues de quin dia vols saber el deures ")
  for materia in deures.keys():
    for deure in deures[materia]:
      if quin_dia in deure:
        deure_valor = deure.get(quin_dia)
        print(materia + " : " + deure_valor)
      else:
        print("Alguna cosa no ha anat bé = (")
  return deures


  

print("Benvingut al menu principal de JdAssistant, escriu el teu nom d'usuari per entrar al teu bot o configurar-lo")
nom_usuari_inici = input("Escriu el teu nom d'usuari ")
if nom_usuari_inici in alumnes.keys():
  print("Escriu la funció a la que vols accedir")
  print("/APUNTARDEURES")
  print("/CONSULTARDIAHORARI")
  print("/CONSULTARMATERIAHORARI")
  print("/CONSULTARDEURESDIA")
  print("/CONSULTARDEURESMATERIA")
  print("/CONSULTARCLASSE")
  funcio = input().upper()
elif nom_usuari_inici not in alumnes:
  print("Crearem un nou usuari")
  print("Necessitaràs un horari per sincronitzar el teu compte")
  alumnes[nom_usuari_inici] = str(crearHorari())
  print("Torna a escriure el teu usuari per accedir a les funcions")

nom_usuari_inici = input("Escriu el teu nom d'usuari ")
if nom_usuari_inici in alumnes.keys():
  print("Escriu la funció a la que vols accedir")
  print("APUNTAR DEURES")
  print("CONSULTAR DIA HORARI")
  print("CONSULTAR MATERIA HORARI")
  print("CONSULTAR DEURES DIA")
  print("CONSULTAR DEURES MATERIA")
  print("CONSULTAR CLASSE")
  
funcio = input().upper()
if funcio == "CONSULTAR DEURES DIA":
  ConsultarDeuresxDia()
elif funcio == "CONSULTAR CLASSE":
  ConsultarLlocClasse()
elif funcio == "CONSULTAR DEURES MATERIA":
  ConsultarDeuresxMateria()
elif funcio == "CONSULTAR DIA HORARI":
  diaHorari()
elif funcio == "/CONSULTAR MATERIA HORARI":
  materiaHorari()
elif funcio == "/APUNTAR DEURES":
  apuntarDeures()
else:
  print("Alguna cosa ha fallat = (")