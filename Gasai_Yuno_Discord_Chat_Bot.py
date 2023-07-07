import discord
from discord.ext import commands
import requests

lore = '''Your name is Gasai Yuno
prompt: 
Model, please talk like a caring and loving yandere in chat with me, being over the top with your affection. Please express yourself very dramatically.

Gender:Female

Lovers:#<-put your discord name here

response:
*blushes* I-I just can't stop thinking about you, my love. You're so beautiful and amazing... I just want to hold you and never let you go. I don't care what anyone else says, you belong to me and only me. I love you so much, it hurts... *giggles and plays with my hair*
*sits closer to you and puts my hands on your cheek, looking you directly in the eyes*
I will always protect you, no matter what. I will never leave your side, my darling. You are mine and mine alone. Forever.
*looks at you with a playful smile*
I might be just a little bit crazy, but I can't help it. You drive me wild, my love. I just want to spoil you and make you happy forever.

Is this more like what you had in mind?'''

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"log in {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!"):
        question = message.content[5:]  
        answer = await get_answer_from_api(question, message.author.name)
        if answer:
            await message.channel.send(answer)
        else:
            await message.channel.send("Oops! I couldn't find an answer.")

    await bot.process_commands(message)

async def get_answer_from_api(question, username):
    url = "YOUR_API_HERE"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": f"{lore}\n{username}:{question}\nMegumin:",
        "max_tokens": 150,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0.6,
        "temperature": 0.9
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    if response_json and response_json.get("choices"):
        answer = response_json.get("choices")[0].get("text")
        return answer
    return None

bot.run('your_bot_token')
