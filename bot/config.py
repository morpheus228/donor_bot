from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass
class BotConfig:
    token: str


@dataclass
class Config:
    bot: BotConfig

    @classmethod
    def set(cls, path: str = '.env'):
        # load_dotenv(path)

        cls.bot = BotConfig(
            token = os.getenv('BOT_TOKEN')
        )