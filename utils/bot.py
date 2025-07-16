import discord
import os
from utils.logger import Logger
from dotenv import load_dotenv as env
from discord.ext import commands
env()


class Orion(commands.Bot):
    def __init__(self):
        self.logger = Logger().get_logger()
        super().__init__(
            command_prefix = ".",
            intents=discord.Intents.all()
        )
    
    async def on_ready(self):
        self.logger.info(f"Logged in as: {self.user.name}")

    def runbot(self):
        self.logger.info(f"Starting bot!")
        self.run(os.getenv("BOT_TOKEN"))