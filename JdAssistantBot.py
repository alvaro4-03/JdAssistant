#https://github.com/sergiperez/tallerTelegramBot
#Instal·lar API pip3 install pyTelegramBotApi
#https://python-telegram-bot.readthedocs.io/en/stable/
import telebot
from telebot import types
import datetime


#Token que lliga amb el bot de Telegram
TOKEN = '1376336790:AAFcTgWbf-4pJNejrAGknJSxZzuaCI6wXj0'
bot = telebot.TeleBot(TOKEN)

#Diccionari per guardar deures
prova = []
diccionari_alumne = {}
variable = {}
var_materia = {}
estat_anim = {}
estat_anim_neg = {}
diccionari_deures = {}
temps = {}
variable_horari = {}
dia_alumne = [[] , [] , [] , [] , []]
dies = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres"]
hora = ["8 a 9", "9 a 10", "10 a 11", "11:30 a 12:30", "12:30 a 13:30", "13:30 a 14:30"]
hora_variable = {}
diccionari_horari = {}
#Diccionari per guardar comanda i username Comencen comandes

@bot.message_handler(commands=['agenda'])
def triarDia(missatge):
  markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
  resposta1=bot.send_message( missatge.chat.id , "Escull el dia per al que apuntar els deures",  reply_markup=markup )

  bot.register_next_step_handler(resposta1, agenda_command)

def agenda_command(missatge):
  dia = missatge.text
  variable[missatge.from_user.username] = dia
  alumne = missatge.from_user.username

  if diccionari_alumne == {}:
    diccionari_alumne[alumne] = [{"Dilluns":[]} , {"Dimarts":[]} , {"Dimecres":[]} , {"Dijous":[]} , {"Divendres":[]}]
#    diccionari_alumne[alumne] = {dia:[]}

  elif diccionari_alumne != {} and missatge.from_user.username not in diccionari_alumne.keys():
    diccionari_alumne[missatge.from_user.username] = [{"Dilluns":[]} , {"Dimarts":[]} , {"Dimecres":[]} , {"Dijous":[]} , {"Divendres":[]}]
#    diccionari_alumne[missatge.from_user.username] = {dia:[]}

#  elif diccionari_alumne  != {} and dia not in  diccionari_alumne[alumne].keys():
 #   diccionari_alumne[alumne] = [diccionari_alumne[alumne],{dia:[]}]

  else:
    diccionari_alumne[alumne]= diccionari_alumne[alumne]

  print(diccionari_alumne)


  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Escull la matèria que vols apuntar per al " + dia, reply_markup=markup)


  bot.register_next_step_handler(resposta, EscriureDeures)



def EscriureDeures (missatge):
  materia = missatge.text
  var_materia[missatge.from_user.username] = materia
  print(materia)
  resposta2 = bot.send_message(missatge.chat.id, "Escriu els  deures que vols que s'apuntin de " + materia)
  @bot.message_handler(func=lambda m: True)
  def Deures(missatge):

    alumne = missatge.from_user.username
    print(materia)

    resposta3 = missatge.text
    deure = bot.send_message(missatge.chat.id, "Has apuntat " + resposta3)
    print(diccionari_alumne)
    p = dies.index(variable[alumne])
#    p = len(diccionari_alumne[alumne])
#    if p-1 != 0 and diccionari_alumne[alumne][p-1][variable[alumne]] == []:
    x = diccionari_alumne[alumne][p][variable[alumne]].append([var_materia[alumne] + ": " + resposta3])
#      x = diccionari_alumne[alumne][p][variable[alumne]].append([var_materia[alumne] + ": " + resposta3])
#      diccionari_alumne[alumne][p-1][variable[alumne]]=[var_materia[alumne] + ": " + resposta3]
    bot.send_animation(missatge.chat.id, "https://im3.ezgif.com/tmp/ezgif-3-fbe94dd84420.gif")
    print(diccionari_alumne)
#    elif diccionari_alumne[alumne][variable[alumne]] == []:
 #     n = diccionari_alumne[alumne][variable[alumne]].append([var_materia[alumne] + ": " + resposta3])
#      diccionari_alumne[alumne][variable[alumne]]=[var_materia[alumne] + ": " + resposta3]
     # bot.send_animation(missatge.chat.id, "https://im3.ezgif.com/tmp/ezgif-3-fbe94dd84420.gif")
#      print(diccionari_alumne)
  #  else:
   #   z = diccionari_alumne[alumne][variable[alumne]].append([var_materia[alumne] + ": " + resposta3])
#      diccionari_alumne[alumne][variable[alumne]]=[diccionari_alumne[alumne][variable[alumne]], [var_materia[alumne] + ": " + resposta3]]
    #  bot.send_animation(missatge.chat.id, "https://im3.ezgif.com/tmp/ezgif-3-fbe94dd84420.gif")
 #     print(diccionari_alumne)
  return ""


@bot.message_handler(commands=['consultaragenda'])
def consultaragenda(missatge):
  markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
  resposta1 = bot.send_message(missatge.chat.id, "Escull el dia del que vols consultar els deures", reply_markup=markup)
  bot.register_next_step_handler(resposta1, consulta)

def consulta(missatge):
  variable[missatge.from_user.username] = missatge.text
  print(variable)
  print(diccionari_alumne[missatge.from_user.username])
  f = dies.index(variable[missatge.from_user.username])
  if diccionari_alumne[missatge.from_user.username][f][variable[missatge.from_user.username]] != []:
    for u in diccionari_alumne[missatge.from_user.username][f][variable[missatge.from_user.username]]:
      bot.send_message(missatge.chat.id, u)
      print(u)
#  elif varaible[missatge.from_user.username] in diccionari_alumne[missatge.from_user.username].keys():
 #   for u in diccionari_alumne[missatge.from_user.username][varaible[missatge.from_user.username]]:
  #    bot.send_message(missatge.chat.id, u)
  else:
    bot.send_message(missatge.chat.id, "El dia que demamnes no te deures asignats")
  return ""


@bot.message_handler(commands=['estatdanim'])
def estatDanim (missatge):
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton(":- )"),types.KeyboardButton(":- |"),types.KeyboardButton(":- ("))
  resposta1 = bot.send_message(missatge.chat.id, "Com et trobes?", reply_markup=markup)
  bot.register_next_step_handler(resposta1, estat)

def estat(missatge):
  if missatge.text == ":- )":
    bot.send_animation(missatge.chat.id, "https://media1.tenor.com/images/8d920cdbab5c75e43e35dcdc8aac84a3/tenor.gif?itemid=7953774")
  elif missatge.text == ":- |":
    bot.send_animation(missatge.chat.id, "https://media.tenor.com/images/aa7138dd3b6b0b3e9c9caaf82aba73bc/tenor.gif")
  else:
    bot.send_animation(missatge.chat.id, "https://media.tenor.com/images/a1804436e7606fc88ff8a69c9b0bf65c/tenor.gif")

  if missatge.text == ":- (" and estat_anim_neg == {}:
    temps[missatge.from_user.username] = [str(missatge.date)]
    global prova
    prova = temps[missatge.from_user.username]
    print(prova)
    print(temps)
    estat_anim_neg[missatge.from_user.username] = [missatge.text + " : " + datetime.datetime.fromtimestamp(missatge.date).strftime('%c')]
  elif missatge.text == ":- (" and estat_anim_neg != {}:
    n  = prova.append(str(missatge.date))
    print(prova)
    estat_anim_neg[missatge.from_user.username] = estat_anim_neg[missatge.from_user.username],[missatge.text + datetime.datetime.fromtimestamp(missatge.date).strftime('%c')]
  else:
    estat_anim[missatge.from_user.username]= missatge.text
  print(estat_anim)
  print(estat_anim_neg)
  temps[missatge.from_user.username] = prova
  print(temps)
  if len(temps[missatge.from_user.username])  >= 3:
    bot.send_message(missatge.chat.id, "Et trobes bé?")
    bot.send_message(missatge.chat.id, "https://www.youtube.com/watch?v=nJ5F3ieB6nE")
    bot.send_message(missatge.chat.id, "https://www.youtube.com/watch?v=e7fGQqpORfA")
    bot.send_message(missatge.chat.id, "https://infolibros.org/libros-de-desarrollo-personal-gratis-pdf/")
    bot.send_message(missatge.chat.id, "https://open.spotify.com/show/0sGGLIDnnijRPLef7InllD")
    bot.send_message(missatge.chat.id, "Aqui et deixo dos enllaços a Youtube per a que et sentis millor, un enllaç a una pàgina web amb llibres d'autoajuda que potser et serveixen i també un enllaç al podcast d''Entiende tu mente' per si et cal; si no et serveix se't recomana posar-te en contacte amb professionals i sobretot explicar-s'ho a un adult")
    temps[missatge.from_user.username].clear()
#datetime.datetime.fromtimestamp(missatge.date).strftime('%c')
@bot.message_handler(commands=['horari'])
def horari(missatge):
#  for d in dies:
  #  for h in hora:
   #   markup = types.ReplyKeyboardMarkup(row_width=3)
    #  markup.add(types.KeyboardButton("Prova"),types.KeyboardButton("prova2"),types.KeyboardButton("prova3"))
#      resposta = bot.send_message(missatge.chat.id, "Digues la matèria que et toca de " + h + " els ", reply_markup=markup)
     # x = diccionari_horari[missatge.from_user.username][dies.index(d)][dies[dies.index(d)]].append(missatge.text)
     # print(diccionari_horari)
  if diccionari_horari == {}:
    diccionari_horari[missatge.from_user.username] = [{"Dilluns":[]} , {"Dimarts":[]} , {"Dimecres":[]} , {"Dijous":[]} , {"Divendres":[]}]
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Endevant!"))
    resposta = bot.send_message(missatge.chat.id, "L'horari està buit, a continuació el podràs omplir", reply_markup=markup)
    bot.register_next_step_handler(resposta, horari_dll1)
  else:
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"),types.KeyboardButton("Veure sencer"))
    resposta1=bot.send_message( missatge.chat.id , "Escull el dia que vols saber l'horari o si vols veure tot l'horari",  reply_markup=markup )
    bot.register_next_step_handler(resposta1, consulta_horari)

def consulta_horari(missatge):
 hora = ["8 a 9", "9 a 10", "10 a 11", "11:30 a 12:30", "12:30 a 13:30", "13:30 a 14:30"]
 if missatge.text == "Veure sencer":
#    for d in diccionari_horari[missatge.from_user.username]:
 #     for h in diccionari_horari[missatge.from_user.username][dies]:
   bot.send_message(missatge.chat.id, diccionari_horari[missatge.from_user.username])

def horari_dll1(missatge):
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dilluns de 8 a 9", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dll2)
def horari_dll2(missatge):
  x = diccionari_horari[missatge.from_user.username][0]["Dilluns"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dilluns de 9 a 10", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dll3)

def horari_dll3(missatge):
  y = diccionari_horari[missatge.from_user.username][0]["Dilluns"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dilluns de 10 a 11", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dll4)

def horari_dll4(missatge):
  z = diccionari_horari[missatge.from_user.username][0]["Dilluns"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dilluns de 11:30 a 12:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dll5)

def horari_dll5(missatge):
  c = diccionari_horari[missatge.from_user.username][0]["Dilluns"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dilluns de 12:30 a 13:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dll6)

def horari_dll6(missatge):
  f = diccionari_horari[missatge.from_user.username][0]["Dilluns"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dilluns de 13:30 a 14:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dm1)

def horari_dm1(missatge):
  d = diccionari_horari[missatge.from_user.username][0]["Dilluns"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimarts de 8 a 9", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dm2)
 # dia_alumne[f].append(resposta)

def horari_dm2(missatge):
  d = diccionari_horari[missatge.from_user.username][1]["Dimarts"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimarts de 9 a 10", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dm3)

def horari_dm3(missatge):
  d = diccionari_horari[missatge.from_user.username][1]["Dimarts"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimarts de 10 a 11", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dm4)

def horari_dm4(missatge):
  d = diccionari_horari[missatge.from_user.username][1]["Dimarts"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimarts de 11:30 a 12:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dm5)

def horari_dm5(missatge):
  d = diccionari_horari[missatge.from_user.username][1]["Dimarts"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimarts de 12:30 a 13:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dm6)

def horari_dm6(missatge):
  d = diccionari_horari[missatge.from_user.username][1]["Dimarts"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimarts de 13:30 a 14:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dc1)

def horari_dc1(missatge):
  d = diccionari_horari[missatge.from_user.username][1]["Dimarts"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimecres de 8 a  9", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dc2)
 # dia_alumne[f].append(resposta)

def horari_dc2(missatge):
  d = diccionari_horari[missatge.from_user.username][2]["Dimecres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimecres de 9 a 10", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dc3)

def horari_dc3(missatge):
  d = diccionari_horari[missatge.from_user.username][2]["Dimecres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimecres de 10 a 11", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dc4)

def horari_dc4(missatge):
  d = diccionari_horari[missatge.from_user.username][2]["Dimecres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimecres de 11:30 a 12:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dc5)

def horari_dc5(missatge):
  d = diccionari_horari[missatge.from_user.username][2]["Dimecres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimecres de 12:30 a 13:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dc6)

def horari_dc6(missatge):
  d = diccionari_horari[missatge.from_user.username][2]["Dimecres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dimecres de 13:30 a 14:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dj1)

def horari_dj1(missatge):
  d = diccionari_horari[missatge.from_user.username][2]["Dimecres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dijous de 8 a 9", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dj2)
 # dia_alumne[f].append(resposta)

def horari_dj2(missatge):
  d = diccionari_horari[missatge.from_user.username][3]["Dijous"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dijous de 9 a 10", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dj3)

def horari_dj3(missatge):
  d = diccionari_horari[missatge.from_user.username][3]["Dijous"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dijous de 10 a 11", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dj4)

def horari_dj4(missatge):
  d = diccionari_horari[missatge.from_user.username][3]["Dijous"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dijous de 11:30 a 12:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dj5)

def horari_dj5(missatge):
  d = diccionari_horari[missatge.from_user.username][3]["Dijous"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dijous de 12:30 a 13:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dj6)

def horari_dj6(missatge):
  d = diccionari_horari[missatge.from_user.username][3]["Dijous"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Dijouss de 13:30 a 14:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dv1)

def horari_dv1(missatge):
  d = diccionari_horari[missatge.from_user.username][3]["Dijous"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Divendres de 8 a 9", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dv2)
 # dia_alumne[f].append(resposta)

def horari_dv2(missatge):
  d = diccionari_horari[missatge.from_user.username][4]["Divendres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Divendres de 9 a 10", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dv3)

def horari_dv3(missatge):
  d = diccionari_horari[missatge.from_user.username][4]["Divendres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Divendres de 10 a 11", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dv4)

def horari_dv4(missatge):
  d = diccionari_horari[missatge.from_user.username][4]["Divendres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Divendres de 11:30 a 12:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dv5)

def horari_dv5(missatge):
  d = diccionari_horari[missatge.from_user.username][4]["Divendres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Divendres de 12:30 a 13:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_dv6)

def horari_dv6(missatge):
  d = diccionari_horari[missatge.from_user.username][4]["Divendres"].append(missatge.text)
  print(diccionari_horari)
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els Divendres de 13:30 a 14:30", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari_f)

def horari_f(missatge):
  d = diccionari_horari[missatge.from_user.username][4]["Divendres"].append(missatge.text)
  bot.send_message(missatge.chat.id, "El calenddari s'ha apuntat correctament")

bot.polling()

