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

#Diccionari per guardar comanda i username
comandes = {}
#Comencen comandes
@bot.message_handler(commands=['agenda'])
def agenda_command(missatge):
  #missatge m'arriba tota la info del xat que estic fent servir
  missatge.from_user.username
  #identificador conversa missatge.chat.id
    
  #Fem botonera
  markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"),types.KeyboardButton("Agenda"),types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))
  #Creem la resposta
  #identificador conversa, missatge , la botonera 
  resposta = bot.send_message(missatge.chat.id,"Escull la matèria que vols apuntar",reply_markup=markup)
	
  #Li dic que quan toqui un botó que ha de fer
  #envies la resposta i quan toqui botó fan la funció jugar
  bot.register_next_step_handler(resposta, triarDia)

def triarDia(missatge):
  # hauràs d¡inserir usuari i resposta triada de matària
  #El botó (matèria) triat per l'usuari està a missatge.text
  alumne = missatge.from_user.username
  materia = missatge.text
  #Omplir diccionari
  #Demanar dia
  markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dilluns"),types.KeyboardButton("Dimarts"),types.KeyboardButton("Dimecres"),types.KeyboardButton("Dijous"),types.KeyboardButton("Divendres"))
  resposta1=bot.send_message(missatge.chat.id,"Escull el dia per al que apuntar",reply_markup=markup)
  #Escriure els deures
  bot.register_next_step_handler(resposta1, EscriureDeures)
  
def EscriureDeures(missatge):
  #llistat_alumnes = {alummne : {materia : [[dia,tasca][]]}}
  markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Seguir"))
  resposta1=bot.send_message(missatge.chat.id,"Fes clic al botó per seguir",reply_markup=markup)
  #Escriure els deures
  bot.register_next_step_handler(resposta1, Revisar)

def Revisar(missatge):
  materia = missatge.text
  alumne = missatge.from_user.username
  bot.send_message("Has apuntat ")
#Comencen comandes
@bot.message_handler(commands=['mostraDeures'])
def mostraDeures_command(missatge):  
  #Pintaràs els deures que tens guardats
  #Triant el diccionari que correspon a missatge.from_user.username
  return ""


@bot.message_handler(func=lambda message: True)
def echo_all(missatge):
	#Tractar només si t'interessa, ha fet camñí que tocar.
  #if comanda[missatge.missatge.from_user.username] == "apuntar deures":
      #Posar missatge.text al diccionari de deures
      bot.send_message(missatge.chat.id, "Deures apuntats")

bot.polling()
