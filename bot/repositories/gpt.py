import httpx


class GPT:
    def __init__(self):
        self.url: str = "https://api.chaindesk.ai/agents/clszrvuoh00d4o98iglw5yexx/query"
        self.headers = {
            "Authorization": "Bearer 30b82f0c-9d27-45ed-9a2b-5d0fe1b69bb1",
            "Content-Type": "application/json"
        }
        
    async def make_request(self, request: str) -> str|None:
        async with httpx.AsyncClient() as client:
            payload = {"query": request}
            response = await client.post(self.url, json=payload, headers=self.headers)

            if response.status_code == 200:
                return response.json()['answer']
            else:
                print(response.json())