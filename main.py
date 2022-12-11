import os

import telebot
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("CHAVE_API"))

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
  bot.send_message(mensagem.chat.id, "Saindo a pizza pra sua casa: Tempo de espera em 20min.")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
  bot.send_message(mensagem.chat.id, "Saindo o brabo, em 10 min chega ai.")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
     bot.send_message(mensagem.chat.id, "Tem salada aqui não. clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):

  texto = """
    O que você vai querer? (Clique em uma opção)
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada
    """
  bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
  bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um email para teste@gmail.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
  bot.send_message(mensagem.chat.id,  "Valeu! Biasi mandou um abraço de volta")

def verificar(mensagem):
    return True
 

@bot.message_handler(func=verificar)
# @bot.message_handler(commands=["ola"])
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço pro Biasi
    Responder qualquer outra coisa não vai funcionar, clique
    em uma das opções 
    """
    bot.reply_to(mensagem, texto)

bot.polling()

#  para manter ele ligado precisa de algum servidor rodando
#  um exemplo de um é o replit.com, voce pode rodar/criar
#  codigos la, baixar blibliotecas e deixar rodando, mas é 
#  pago