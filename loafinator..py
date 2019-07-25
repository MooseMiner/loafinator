# Work with Python 3.6
import discord

TOKEN = 'NjAzNzk0MDE3MTc1NzMyMjU1.XTkmQA.IwJgtNcqK2sxlKbMnHX-YwYQkq8'

client = discord.Client()




@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!loafme'):
        msg = 'https://tr.rbxcdn.com/c13164f77e8f40c50fb7e6d84398b864/420/420/Decal/Png'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!edf'):
        msg = 'https://www.youtube.com/watch?v=cRmES6IJk_o'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!hotboys'):
        msg = 'http://www.bleachers.co.uk/uploads/2/5/4/5/25457155/s342424778808016717_p224_i16_w640.jpeg'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
