#TODO Futur mirar de sincronitzar amb calendari Moodle

#TODO Per què quatre setmanes?
deures = {}
#TODO Més que deures és per apuntar dates de lliurament, no?       
#TODO Posar cada espai en funcions. Diferents.
def apuntarDeures():
  deures[input("Indica la matèria ")] = {input("Per a quin dia ") : input("Indica que s'ha d'apuntar ")}
apuntarDeures()
print(deures)
        
def ConsultarDeuresxMateria():
  print(deures[input("Digues la matèria de la que vols saber els deures ")])     
ConsultarDeuresxMateria()             

print(deures[input("Materia: ")][input("Dia: ")])
#TODO Consultar deures per setmana actual
#TODO Consultar deures per dia actual 