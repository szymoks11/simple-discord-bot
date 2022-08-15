import discord
from secret_token import token
from time import sleep
import os
import sys
from datetime import datetime, date

today = date.today()
now = datetime.now()
bot = discord.Client()

current_time = now.strftime("%H:%M:%S")
d2 = today.strftime("%B %d, %Y")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="!help"))
    print("You are logged as: {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Send me  👍 bro")
        print("!hello:", message.author, current_time, d2)

    if message.content.startswith("!help"):
        await message.channel.send(" !github \n !twitch \n !spotify \n !author \n")
        print("!help:", message.author, current_time, d2)

    if message.content.startswith("!github"):
        await message.channel.send("link")
        print("!github:", message.author, current_time, d2)

    if message.content.startswith("!author"):
        await message.channel.send("if u wannna DM me i'm @szymoks11#4802")
        print("!author:", message.author, current_time, d2)

    if message.content.startswith("!twitch"):
        await message.channel.send("link")
        print("!twitch:", message.author, current_time, d2)

    if message.content.startswith("!spotify"):
        await message.channel.send("link")
        print("!spotify:", message.author, current_time, d2)

    if message.content.startswith("!status"):
        server = "localhost"
        odpowiedz_server = os.system("ping -c 1 " + server)
        if odpowiedz_server == False:  # False= working
            await message.channel.send(":green_circle:  Server is online")
        if odpowiedz_server == 256:
            await message.channel.send(":red_circle: Server is offline")
        print("!status:", message.author, current_time, d2)

    if message.content.startswith("!ping"):
        all_message = str(message.content)
        ip_address = all_message.split()[1]
        odpowiedz_web = os.system("ping -n 2 " + ip_address)
        if odpowiedz_web == False:
            await message.channel.send(ip_address+" :green_circle: Is online")
        elif odpowiedz_web == 256:
            await message.channel.send(ip_address+":red_circle: Is offline")
        print("!ping:", message.author, current_time, d2)

    if message.content.startswith("!stop"):
        print("Shuting down bot:", message.author, current_time, d2)
        sleep(1)
        exit()
    if message.content.startswith("!restart"):
        print("!restart:", message.author, current_time, d2)
        python = sys.executable
        os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    bot.run(token)
