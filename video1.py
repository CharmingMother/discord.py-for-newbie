import discord
from discord.ext import commands


Ahri=commands.Bot(command_prefix='.')



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



Ahri.run('NTUwODcxODI3ODQxNDE3Mjc4.D1ou-g.rmUNUT1_XHWF--cBlOWjexlbl2Q')
