#! /usr/bin/python3

import discord
from discord.ext import commands
import datatime

# en command_prefix se establece el prefijo para el comando ejemplo: !play
bot = commands.Bot(command_prefix='!', description="Me presento, soy Jarvis")

# con @bot.command creamos los comandos nuevos para el bot
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# comando de información del servidor: !info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem impsum asdasd", timestamp=datetime.datatime.utcnow(), color=discord.color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"ctx.guil.owner")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.fuild.icon}")

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    # evento del bot
    await bot.change_presence(activity=discord.Streaming(name="Online", url="Aqui tu link de twitch"))
    # Output al ejecutarlo en consola
    print("Jarvis is online")

bot.run('aqui van tus licencias de bot')
