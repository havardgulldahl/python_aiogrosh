
from configparser import ConfigParser
from typing import List, Dict
import aiohttp 
from aiohttp import BasicAuth, ClientSession

class GroshApp(object):
    
    def __init__(self, config:ConfigParser) -> None:
        self.config = config
        self.apiUrl = config.get("default", "apiUrl")
        self.apiUser = config.get("default", "apiUser")
        basicPassword = BasicAuth(self.apiUser, config.get("default", "apiPassword"))
        self._headers = {
            "Authorization": basicPassword.encode()
        }
        self.shoppingLists = []

    async def startup(self) -> None:
        self.session = ClientSession(headers=self._headers)


    async def getShoppingLists(self) -> List:
        async with self.session.get(self.apiUrl + "/users/me/households") as resp:
            self.shoppingLists = await resp.json()
            print(self.shoppingLists)
            return self.shoppingLists

    async def getList(self, listId:int) -> Dict:
        async with self.session.get(self.apiUrl + f"/households/{listId}/current") as resp:
            list = await resp.json()
            return list
                
