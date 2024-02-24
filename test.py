import asyncio
from bot.repositories.gpt import GPT

async def main():
    print(await GPT().make_request("Что такое DonorDash"))


asyncio.run(main())