import discord
import os
from dotenv import load_dotenv, dotenv_values
import branches

#Create an instance of a client
#Intents specification required apparently
intents = discord.Intents.all()
client = discord.Client(intents=intents)


# EVENT on START
@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))
    
    channel = client.get_channel(997984431883173958) #Put "channel-number" in parentheses
    await channel.send("I have been deployed!")


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


# RUN the CLIENT
load_dotenv()
client.run(os.getenv("KEY1"), bot=True)