import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for file in os.listdir("./modules"):
            if file.endswith(".py"):
                self.load_extension(f"modules.{file[:-3]}")
        
    async def on_ready(self):
        print(f"Logged in as {self.user.name} (ID: {self.user.id})")

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = Bot(command_prefix="!", case_insensitive=True, intents=intents)

bot.run(os.environ["TOKEN"])