#TODO Futur mirar de sincronitzar amb calendari Moodle
deures = {}

#TODO Més que deures és per apuntar dates de lliurament, no?       
#TODO Posar cada espai en funcions. Diferents.
def apuntarDeures():
  materia = input("Digues la matèria que s'ha d'apuntar ")
  dia = input("Indica per a quin dia ")
  quins_deures = input("Esciru que vols apuntar ")
  if materia in deures:
    deures[materia] = deures[materia] , {dia : quins_deures}
  else:
    deures[materia] = {dia : quins_deures}
  return deures
        
def ConsultarDeuresxMateria():
  #TODO Vigilar errors. Que passa si poso matèria que no hi ha deures.
  materia = input("Digues la matèria de la que vols saber els deures ")
  if materia in deures.keys():
    print(deures[materia])
  else:
    print ("Alguna cosa no ha anat bé   = (")
  return deures

def ConsultarDeuresxDia():
  quin_dia = input("Digues de quin dia vols saber el deures ")
  for materia in deures.keys():
    print(materia + " : " + deures[materia][quin_dia])
  return deures


def ConsultarDeuresxDia2():
  prova = deures.values()
  quin_dia = input("Digues de quin dia vols saber el deures ")
  if quin_dia in prova:
    for materia in deures.keys():
      seleccio_dia = deures[materia]
      print(materia + " : " + deures[materia][quin_dia])
  else:
    print ("Alguna cosa no ha anat bé   = (")
  return deures
  
apuntarDeures()
apuntarDeures()
apuntarDeures()
ConsultarDeuresxMateria()
ConsultarDeuresxDia()
ConsultarDeuresxDia2()