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
diccionari_alumne = {}
variable = {}
var_materia = {}
estat_anim = {}
diccionari_deures = {}
temps = {}
variable_horari = {}
dia_alumne = [[] , [] , [] , [] , []]
dies = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres"]
hora = ["8 a 9", "9 a 10", "10 a 11", "11:30 a 12:30", "12:30 a 13:30", "13:30 a 14:30"]
hora_variable = {}
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
    diccionari_alumne[alumne] = {dia:[]}
    print(diccionari_alumne)
  elif diccionari_alumne  != {} and dia not in  diccionari_alumne[alumne].keys():
    diccionari_alumne[alumne] = diccionari_alumne[alumne],{dia:[]}
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
    if diccionari_alumne[alumne][variable[alumne]] == []:
      diccionari_alumne[alumne][variable[alumne]]=[var_materia[alumne] + ": " + resposta3]
      print(diccionari_alumne)
    else:
      diccionari_alumne[alumne][variable[alumne]]=[diccionari_alumne[alumne][variable[alumne]], [var_materia[alumne] + ": " + resposta3]]
      print(diccionari_alumne)
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
  print(diccionari_alumne[missatge.from_user.username][variable[missatge.from_user.username]])

  if variable[missatge.from_user.username] in diccionari_alumne[missatge.from_user.username].keys():
    for u in diccionari_alumne[missatge.from_user.username][variable[missatge.from_user.username]]:
      bot.send_message(missatge.chat.id, u)
    print(u)
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

  if missatge.text == ":- (":
    temps[missatge.from_user.username] = missatge.date

  estat = [missatge.text + datetime.datetime.fromtimestamp(missatge.date).strftime('%c')]
  if estat_anim == {}:
    estat_anim[missatge.from_user.username] = [estat]
  else:
    estat_anim[missatge.from_user.username]= [estat_anim[missatge.from_user.username] + estat]
  print(estat_anim)
  print(estat_anim[missatge.from_user.username])

#datetime.datetime.fromtimestamp(missatge.date).strftime('%c')



@bot.message_handler(commands=['horari'])

#def horari(missatge):
 # dia_alumne = [[] , [] , [] , [] , []]
 # hora = ["8 a 9", "9 a 10", "10 a 11", "11:30 a 12:30", "12:30 a 13:30", "13:30 a 14:30"]
 # dies = ["dilluns", "dimarts", "dimecres", "dijous", "divendres"]
 # for d in dies:
  #  for h in hora:
   #   markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    #  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
     # resposta=bot.send_message(missatge.chat.id, "Digues la matèria que et toca els  " + d + " de " + h, reply_markup=markup)
     # f = dies.index(d)
     # dia_alumne[f].append(resposta)

#for d in dies:
 # for h in hores
def horari2(missatge):
  markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
  resposta = bot.send_message(missatge.chat.id, "Digues de quin dia vols saber o apuntar el teu calendari", reply_markup=markup)
  bot.register_next_step_handler(resposta, horari3)

def horari3(missatge):
  variable_horari[missatge.from_user.username] = missatge.text
  if dia_alumne[dies.index(missatge.text)] == []:
    print("hola")
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    markup.add(types.KeyboardButton("8 a 9"),types.KeyboardButton("9 a 10"),types.KeyboardButton("10 a 11"),types.KeyboardButton("11:30 a 12:30"),types.KeyboardButton("12:30 a 13:30"),types.KeyboardButton("13:30 a 14:30"))
    resposta = bot.send_message(missatge.chat.id, "L'horari està buit, selecciona les hores per omplir-lo", reply_markup=markup)
    def horari(missatge):
      hora_varaible[missatge.from_user.username] = missatge.text
      markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
      markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
      resposta=bot.send_message(missatge.chat.id, "Escull la matèria que et toca els " + variable_horari[missatge.from_user.username] + " de " + hora_variable[missatge.from_user.username], reply_markup=markup)
      def horari2(missatge):
        dia_alumne[dies.index(variable_horari[missatge.from_user.username])].append([hora_varaible[missatge.from_user.username] + ": " + missatge.text])
        print(dia_alumne)
        bot.send_message(missatge.chat.id, "S'ha apuntat que de " + hora_variable[missatge.from_user.username] + " els " + variable_horari[missatge.from_user.username] + " et toca " + missatge.text)

  elif dia_alumne[dies.index(missatge.text)]  != [] and len(dia_alumne[dies.index(missatge.text)]) != 6:
    print("adeu")
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    markup.add(types.KeyboardButton("8 a 9"),types.KeyboardButton("9 a 10"),types.KeyboardButton("10 a 11"),types.KeyboardButton("11:30 a 12:30"),types.KeyboardButton("12:30 a 13:30"),types.KeyboardButton("13:30 a 14:30"))
    resposta = bot.send_message(missatge.chat.id, "L'horari no està complert, selecciona les hores buides per omplir-lo", reply_markup=markup)
  else:
    bot.send_message(missatge.chat.id, dia_alumne[dies.index(missatge.text)])
#  bot.register_next_step_handler(resposta,horari4)

#def horari4(missatge):
 # hora_variable[missatge.from_user.username] = missatge.text
 # markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
#  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
#  resposta=bot.send_message(missatge.chat.id, "Escull la matèria que et toca els " + variable_horari[missatge.from_user.username] + " de " + hora_variable[missatge.from_user.username], reply_markup=markup)

  #bot.register_next_step_handler(resposta, horari5)

#def horari5(missatge):
 # dia_alumne[dies.index(variable_horari[missatge.from_user.username])].append([hora_variable[missatge.from_user.username] + ": " + missatge.text])
  #print(dia_alumne)
  #resposta = bot.send_message(missatge.chat.id, "S'ha apuntat que de " + hora_variable[missatge.from_user.username] + " els " + variable_horari[missatge.from_user.username] + " et toca " + missatge.text)
  #bot.register_next_step_handler(resposta, horari3)



bot.polling()

