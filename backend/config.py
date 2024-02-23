from dataclasses import dataclass
import os


@dataclass
class BotConfig:
    token: str

@dataclass
class MYSQLConfig:
    host: str
    password: str
    user: str
    database: str
    port: str


@dataclass
class Config:
    bot: BotConfig

    @classmethod
    def set(cls, path: str = '.env'):
        
        cls.bot = BotConfig(
            token = os.getenv('BOT_TOKEN')
        )

        cls.mysql = MYSQLConfig(
            host=os.getenv('MYSQL_HOST'),
            password=os.getenv('MYSQL_PASSWORD'),
            user=os.getenv('MYSQL_USER'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT')
        )