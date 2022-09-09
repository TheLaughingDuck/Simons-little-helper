import discord
import os
from dotenv import load_dotenv
import branches

import datetime
import asyncio

#Create an instance of a client
#Intents specification required apparently
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# CHANNELS
dev_channel = client.get_channel(997984431883173958)
remind_channel = client.get_channel(1014166019411038210) #"Production"


# EVENT on START
@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))
    await dev_channel.send("I have been deployed!")
  	#channel = client.get_channel(997984431883173958) #Put "channel-number" in parentheses

# CLOCK
async def timer():
    await client.wait_until_ready()
    msg_sent = False

    while True:
        timenow = datetime.datetime.now()
        if timenow.hour == 15 and timenow.minute == 50:
            if not msg_sent:
                await dev_channel.send("Reminder!") #Change to remind_channel
                msg_sent = True
            else:
                msg_sent = False
        
        await asyncio.sleep(5) #Seconds



# EVENT on MESSAGE
@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    
    # INTERACT WITH COMMANDS
    if message.content.startswith("bot"):
        #Send the content to bot() for interpretation
        output = branches.bot(message.content)
    
        # Print the output from the reminder function
        # This should be a bot message later on
        #print(output)
        await message.channel.send(output)

  # PRESENT THE AVAILABLE COMMANDS
    if message.content == "help":
        help_message = "Theses are my commands:\n"
        help_message+= "------------------------\n"
        help_message+= "hello: Greets you in a friendly manner\n"
        help_message+= "help: Shows this message\n"

        await message.channel.send("```" + help_message + "```")


# RUN clock?
client.loop.create_task(timer())

# RUN the CLIENT
load_dotenv()
client.run(os.getenv("KEY1"), bot=True)