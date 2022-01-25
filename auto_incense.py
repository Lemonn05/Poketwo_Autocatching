ID = ########### #Your channel ID

import discord
import time
import random 

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channel = client.get_channel(ID)
    #channels = ["general"]
    if (message.content.startswith('!incense') and message.channel.id == ID):
        while (True):
            
            await channel.send("p!buy incense")
            
            time.sleep(3660)
            await channel.send("Wait for a few second till next incense")
            
    if (message.content.startswith('!test') and message.channel.id == ID):
        await channel.send("Sup!")
        

client.run("*************************************", bot=False)

#-------------- Please replace the ***** With user token of spam user --------------
