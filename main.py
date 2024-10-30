import discord
from discord.ext import commands
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Discord bot token ve Telegram bot token'ı buraya ekleyin
DISCORD_TOKEN = 'MTMwMDc2NjMxNTY2MDg0MTA2Mg.GrMOKw.rqY61OVO__17fU0VhP_niVs7cPE-y4RJg-Yhuo'
TELEGRAM_TOKEN = '7812449434:AAFaRMA47IHBF4JeEJghCSdveId5UWPia1A'
TELEGRAM_CHAT_ID = '-1002390461572'  # Telegram grubunun chat ID'si
DISCORD_CHANNEL_ID = 1300768478579658805  # Discord'daki news kanalının ID'si

# Discord botunu başlat
intents = discord.Intents.all()
intents.messages = True
discord_bot = commands.Bot(command_prefix='!', intents=intents)

# Telegram botunu başlat
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

@discord_bot.event
async def on_ready():
    print(f'Bot {discord_bot.user} olarak giriş yaptı.')

@discord_bot.event
async def on_message(message):
    if message.channel.id == DISCORD_CHANNEL_ID and not message.author.bot:
        # Discord'dan gelen mesajı Telegram grubuna gönder
        await app.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message.content)

# Uygulamayı çalıştırmak için gerekli olan bir asyncio döngüsü başlatma
async def main():
    await discord_bot.start(DISCORD_TOKEN)

discord_bot.run(DISCORD_TOKEN)
