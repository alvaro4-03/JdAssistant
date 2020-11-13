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
deures = []
dia = ("Dilluns","Dimarts","Dimecres","Dijous","Divendres")
materia = ("Mates","Català","Castellano","Anglès","Física")

#Diccionari per guardar comanda i username
def diccionari(missatge):
  alumne = missatge.from_user.username
  diccionari_dia_deures = {dia:deures}
  diccionari_materia_deures = {materia:deures}
  diccionari_alumne = {alumne:[dia,materia]}
#Comencen comandes

@bot.message_handler(commands=['agenda'])
def agenda_command(missatge):

  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  resposta=bot.send_message(missatge.chat.id,"Escull la matèria que vols apuntar",reply_markup=markup)
  bot.register_next_step_handler(resposta, triarDia)
def triarDia(missatge):
  # hauràs d¡inserir usuari i resposta triada de matària
  #El botó (matèria) triat per l'usuari està a missatge.text
  alumne = missatge.from_user.username
  #Omplir diccionari
  #Demanar dia
  markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
  resposta1=bot.send_message( missatge.chat.id , "Escull el dia per al que apuntar els deures de " + missatge.text,  reply_markup=markup )

  #Escriure els deures
  bot.register_next_step_handler(resposta1, EscriureDeures)

def EscriureDeures (missatge):
  resposta1 = missatge.text
  resposta2 = bot.send_message(missatge.chat.id, "Escriu els  deures que vols que s'apuntin per " + resposta1)
  @bot.message_handler(func=lambda message: True)
  def echo_all(missatge):
    resposta3 = missatge.text
    deure = bot.send_message(missatge.chat.id, "Has apuntat " + resposta3 + " per al " + resposta1)
  return deures

#Tractar només si t'interessa, ha fet camñí que tocar.
  #if comanda[missatge.missatge.from_user.username] == "apuntar deures":
   #Posar missatge.text al diccionari de deures
  #Escriure els deures
  #bot.register_next_step_handler(resposta1)


@bot.message_handler(commands=['consultaragenda'])
def consultaragenda(missatge):
 # markup2 = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
 # markup2.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
 # dia = reply_markup=markup2
  markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dia"), types.KeyboardButton("Materia"))
  resposta_triar_manera = bot.send_message(missatge.chat.id, "Escull com vols consultar els deures apuntats; a travès del dia o de la matèria?", reply_markup=markup)
  if resposta_triar_manera == "Materia":
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"), types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
    resposta_materia = bot.send_message(missatge.chat.id, "Escull la matèria de la que vols consultar els deures", reply_markup=markup)
  elif resposta_triar_manera == "Dia":
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
    resposta_dia = bot.send_message(missatge.chat.id, "Escull el dia que vols consultar els deures", reply_markup=markup)
  #resposta_dia = bot.send_message(missatge.chat.id, "Escll el dia del que vols consultar els deures", dia)
#  bot.load_next_step_handlers()
 # consulta = bot.send_message(missatge.chat.id, missatge.from_user.username, resposta3)
  #Pintaràs els deures que tens guardats
  #Triant el diccionari que correspon a missatge.from_user.username
#  return ""


#Tractar només si t'interessa, ha fet camñí que tocar.
#if comanda[missatge.missatge.from_user.username] == "apuntar deures":
      #Posar missatge.text al diccionari de deures

bot.polling()
