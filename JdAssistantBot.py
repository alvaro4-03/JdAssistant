#https://github.com/sergiperez/tallerTelegramBot
#Instal·lar API pip3 install pyTelegramBotApi
#https://python-telegram-bot.readthedocs.io/en/stable/
import telebot
from telebot import types

#TODO
#Token que lliga amb el bot de Telegram
TOKEN = '1376336790:AAFcTgWbf-4pJNejrAGknJSxZzuaCI6wXj0'
bot = telebot.TeleBot(TOKEN)

#Diccionari per guardar deures
diccionari_alumne = {}
variable = {}
#Diccionari per guardar comanda i username
#Comencen comandes

@bot.message_handler(commands=['agenda'])
def triarDia(missatge):
  # hauràs d¡inserir usuari i resposta triada de matària
  #El botó (matèria) triat per l'usuari està a missatge.text
  #Omplir diccionari
  #Demanar dia
  markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
  resposta1=bot.send_message( missatge.chat.id , "Escull el dia per al que apuntar els deures",  reply_markup=markup )

  #Escriure els deures
  bot.register_next_step_handler(resposta1, agenda_command)

def agenda_command(missatge):
  dia = missatge.text
  variable[missatge.from_user.username] = dia
  alumne = missatge.from_user.username
  diccionari_alumne[alumne] = {dia:[]}

  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id, "Escull la matèria que vols apuntar per al " + dia, reply_markup=markup)


  bot.register_next_step_handler(resposta, EscriureDeures)



def EscriureDeures (missatge):
  materia = missatge.text
  resposta2 = bot.send_message(missatge.chat.id, "Escriu els  deures que vols que s'apuntin de " + materia)
  @bot.message_handler(func=lambda message: True)
  def echo_all(missatge):
    resposta3 = missatge.text
    deure = bot.send_message(missatge.chat.id, "Has apuntat " + resposta3 + " de " + materia)

    diccionari_alumne[missatge.from_user.username][variable[missatge.from_user.username]]=[materia + ": " + resposta3]
 # return deures

#Tractar només si t'interessa, ha fet camñí que tocar.
  #if comanda[missatge.missatge.from_user.username] == "apuntar deures":
   #Posar missatge.text al diccionari de deures
  #Escriure els deures
  #bot.register_next_step_handler(resposta1)


@bot.message_handler(commands=['consultaragenda'])
def consultaragenda(missatge):
#  bot.send_message(missatge.chat.id, diccionari_alumne[missatge.from_user.username][variable[missatge.from_user.username]])
 # markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
#  markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
  bot.send_message(missatge.chat.id, "Escriu els dia que vols consultar els deures"

#  resposta_materia = bot.send_message(missatge.chat.id, "Escull el dia del que vols consultar els deures", reply_markup=markup)
  if resposta_materia in diccionari_alumne[missatge.from_user.username].keys():
    bot.send_message(missatge.chat.id, "Ben fet")
  #Pintaràs els deures que tens guardats
  #Triant el diccionari que correspon a missatge.from_user.username
#  return ""


#Tractar només si t'interessa, ha fet camñí que tocar.
#if comanda[missatge.missatge.from_user.username] == "apuntar deures":
      #Posar missatge.text al diccionari de deures

bot.polling()
