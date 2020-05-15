#TODO Futur mirar de sincronitzar amb calendari Moodle
deures = {}
     
def apuntarDeures():
  materia = input("Digues la matèria que s'ha d'apuntar ")
  dia = input("Indica per a quin dia ")
  quins_deures = input("Esciru que vols apuntar ")
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

apuntarDeures()
apuntarDeures()
apuntarDeures()
print(deures)
ConsultarDeuresxMateria()
ConsultarDeuresxDia()
