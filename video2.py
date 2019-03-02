import asyncio
import discord
from discord.ext import commands


Ahri=commands.Bot(command_prefix='.')
Ahri.remove_command('help')


@Ahri.event
async def on_ready():
    print(Ahri.user.name)



@Ahri.event
async def on_message(msg):
    if 'ahri' in msg.content.lower():
        await Ahri.send_message(msg.channel,"Hello there summoner **{}**".format(msg.author.display_name))

    await Ahri.process_commands(msg)


@Ahri.command(pass_context=True)
async def hi(con):
    await Ahri.say("Hello summoner **{}**".format(con.message.author.display_name))



def condition(msg):
    """[The first and only parameter of the check function must be present and can have any name as long as it still follows python's rules
    The chek function allows you to set conditions for your commands to run before excuting a command
    
    The below example checks to see if the person using the command has the ID equal th the set value
    If the condition is true the command will run and if not it won't
    ]
    
    Arguments:
        msg {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """



    return msg.message.author.id == '185181025104560128' #it can only have a return type and must have a True or False value in that return 



@commands.check(condition)
@Ahri.command(pass_context=True, name='def', aliases=['define','meaning','definition'],no_pm=True)
async def define(con):
    await Ahri.say("Hi")


@Ahri.command(pass_context=True)
async def status(con,user:discord.Member):
    await Ahri.say(user.status)
    await Ahri.say("{} is currently playing {}".format(user.display_name,user.game))



@Ahri.command(pass_context=True)
async def chan(con,channel:discord.Channel):
    await Ahri.say(channel.name)
    await Ahri.say(channel.created_at)


@Ahri.command(pass_context=True)
async def user(con, us: discord.User):
    await Ahri.say(us.avatar_url)



Ahri.run('NTUwODcxODI3ODQxNDE3Mjc4.D1uD_g.PCsq7OWPKYv15AQZ070fhG7ERhQ') #Place your bot token here and please make sure taht  you don't get it leaked and if it's leaked, reset it!
