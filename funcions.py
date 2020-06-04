import telebot
import random
from telebot import types

def sumar(numero1, numero2):
  resultat = numero1 + numero2
  return resultat

def aixecar():
  print("Àlvaro s'aixeca")


#num1 = int(input("A"))
#num2 = int(input("B"))
#print(str(sumar(num1,num2))+str(sumar(78,89)))
#aixecar()

#porra = {clau:valor}

cognoms = {"Harun":"meraga"}
edat = {"Harun":17}
porra = {"Harun":{"Edat":13,"Cognom":"Meraga","Porra":[0,0]}}

print(porra["Harun"]["Edat"])
print(porra)
