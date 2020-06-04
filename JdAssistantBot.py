#https://github.com/sergiperez/tallerTelegramBot
#Instal·lar API pip3 install pyTelegramBotApi
#https://python-telegram-bot.readthedocs.io/en/stable/
import telebot
from telebot import types

#TODO
#Token que lliga amb el bot de Telegram
TOKEN = '970292498:AAFB32dEsoBGBCnqJyIeXL7urpCHGjCQOZg' 
bot = telebot.TeleBot(TOKEN)

#Diccionari per guardar deures

#Comencen comandes
@bot.message_handler(commands=['agenda'])
def agenda_command(missatge):
 # markup = types.InlineKeyboardMarkup()
  #ui = types.InlineKeyboardButton('Private',url='https://telegram.me/mosydev')
  #op = types.InlineKeyboardButton('Bot',url='https://telegram.me/mosydevbot')
  #markup.add(ui)
  #markup.add(op)
  #bot.send_message(missatge.chat.id,'Our Bot And Owner Private',reply_markup=markup)
	#missatge m'arriba tota la info del xat que estic fent servir
  missatge.from_user.username
  #identificador conversa missatge.chat.id
  #TODO fer que apareixin les matèries amb una botonera
  
  #Fem botonera
  markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Mates"),types.KeyboardButton("Català"),types.KeyboardButton("Socials"),types.KeyboardButton("Castellà"),types.KeyboardButton("Naturals/Bio"),types.KeyboardButton("Fisica"),types.KeyboardButton("Filo/Etica"),types.KeyboardButton("Quimica"),types.KeyboardButton("Agenda"),types.KeyboardButton("EF"),types.KeyboardButton("CMC"),types.KeyboardButton("Eco"),types.KeyboardButton("Eco Empresa"),types.KeyboardButton("Tecno"),types.KeyboardButton("English"),types.KeyboardButton("Musica"),types.KeyboardButton("Plastica"),types.KeyboardButton("Optativa"))

	
  #Creem la resposta
  #identificador conversa, missatge , la botonera 
  resposta=bot.send_message(missatge.chat.id,"Escull la matèria que vols apuntar",reply_markup=markup)
	
  #Li dic que quan toqui un botó que ha de fer
  #envies la resposta i quan toqui botó fan la funció jugar
  bot.register_next_step_handler(resposta, triarDia)

def triarDia(missatge):
  # hauràs d¡inserir usuari i resposta triada de matària
  #El botó (matèria) triat per l'usuari està a missatge.text
  alumne = missatge.from_user.username
  #Omplir diccionari
  #{alumne:{missatge.text: [[dia,tasca],[]]}}
  #Demanar dia
  markup = types.ReplyKeyboardMarkup(row_width=5, one_time_keyboard=True)
  markup.add(types.KeyboardButton("Dll"),types.KeyboardButton("Dm"),types.KeyboardButton("Dc"),types.KeyboardButton("Dj"),types.KeyboardButton("Dv"))
  resposta1=bot.send_message(missatge.chat.id,"Escull el dia per al que apuntar",reply_markup=markup)
  #Escriure els deures
  bot.register_next_step_handler(resposta1, EscriureDeures)
  return ""

def EscriureDeures(missatge):

  return ""

#Comencen comandes
@bot.message_handler(commands=['mostraDeures'])
def mostraDeures_command(missatge):  
  #Pintaràs els deures que tens guardats
  #Triant el diccionari que correspon a missatge.from_user.username
  return ""

bot.polling()
