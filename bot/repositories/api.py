
import httpx


class API:
    def __init__(self, host: str = "localhost", port: str = "8005"):
        self.host: str = host
        self.port: str = port
        
    async def get(self, url: str):
        async with httpx.AsyncClient() as client:
            url = f"{self.host}:{self.port}/{url}"
            response = await client.get(url)
            return response
    
    async def post(self, url: str):
        async with httpx.AsyncClient() as client:
            url = f"{self.host}:{self.port}{url}"
            response = await client.post(url)
            return response
        
    async def login(self, tg_id: int) -> bool:
        url = f"/v1/login/{tg_id}"
        response = await self.get(url)
        return response.status_code == 200
    
    async def registration(self, tg_id: int) -> bool:
        url = f"/v1/login/{tg_id}"
        response = await self.get(url)
        return response.status_code == 200