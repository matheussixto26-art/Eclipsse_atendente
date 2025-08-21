# meu_bot.py (versão para Discloud)
import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÕES ---
TOKEN = "MTQwNzA0NTcyNzU0ODM0NjU0MQ.GkZU1J.3zFisV2MYrDgvLxQ6BLVg01DUzbuDuj8D5weJU"

# --- CONFIGURAÇÃO DO BOT ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'Bot conectado como {self.user}')
        print(f'Carregado {len(self.cogs)} cogs.')
        print('------')

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
        
        synced = await self.tree.sync()
        print(f"Sincronizado {len(synced)} comandos.")

bot = MyBot()

# Roda o bot
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure:
    print("ERRO: O token do Discord fornecido é inválido.")
