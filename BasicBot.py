# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import requests,bs4

import math ##for funsies


"""
TO DO ###
1) Make it a music bot
2) Fix the dab issue cause your a horrible person
3) Write stuff for people LEL
4)Make Motd daily and wierd.
5) Introduce new users
6) Figure out the help command
7) Make it moonlight as Ryuk PLZ!
8) Change it to yuno at day
9) an offerring function????
10) Coffee to be served, i mean ya need to work ya bish!
"""


# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Alright a little something i did for both expertimentaion and Hapiness. This is coffee", command_prefix="?", pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by Kaminolucky')
	return await client.change_presence(game=discord.Game(name='Bringing coffee to dumb people')) #This is buggy, let us know if it doesn't work.


##@client.event
##async def on_error(event, args, kwargs):
##        await client.send_message(kwargs.channel,"Alright smart stuff! Either that command doesn't exsist, or Kami has not made it a thing yet, So i suggest Spell it right or STAB KAMI TILL HE DOES ")
##        print(sys.exc_info())

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def hi(*args):

	await client.say("HEllo I am your friendly ~~Cancer~~ bot Coffee. Yoroshikune")
# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.

@client.command()
async def pick(*, args):
        y=str(args)
        x=random.choice(y.split(','))
        await client.say("The Hax Picked: "+x)

@client.command()
async def roll(*args):
        y=args
        x=y[0]
        z=x.split('d')
        no=int(z[0])
        limit=int(z[1])
        rolls=list()
        for i in range(no):
                rolls.append(random.randint(1,limit))
        res="Roll(s):"
        for i in rolls:
                res+=" "+str(i)
        await client.say(res)

@client.command()
async def dab(*,args="1"):
        try:
                y= int(args)
                if(y>10):
                        y=10
        except discord.ext.commands.errors.MissingRequiredArgument:
                print("hey there")
                y= 1
        for i in range(y):
                await client.say("*dabs*")
                await asyncio.sleep(0.5)


@client.command()
async def motd():
        w=open("motd.txt","r")
        x=w.read()
        await client.say(x)
        w.close()

@client.command()
async def motd_set(*,args):
        w=open("motd.txt","w")
        w.write(str(args))
        await client.say("motd has been set as "+ args)
        w.close()

@client.command()
async def calc(*,args):
        try:
                x= eval(args)
        except ZeroDivisionError:
                x="Bish , you just divided by zero"
        await client.say("Result: " + str(x))

@client.command()
async def userinfo(*,args):
        args=args.replace(" ","")
        args=args.lower()
        s="Users\\"
        s+=args+".txt"
        w=open(s,"r")
        y=w.read()
        await client.say(y)
        w.close()
##
##@client.command()
##async def help():
##        s="""
##                ````Alright this is the help module. I hope this works and i have NO idea
##                on what to say here so......``
##                """
##        await client.say(s)

client.run('NDA3MDY0OTIyMTU4MjY4NDE2.DU8Rfw.XOtOBsS0NjnR0d53v23lTxn5Md8')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
