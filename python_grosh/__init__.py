
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
        self.lists = []

    async def startup(self) -> None:
        self.session = ClientSession(headers=self._headers)


    async def getLists(self) -> List:
        async with self.session.get(self.apiUrl + "/users/me/households") as resp:
            self.lists = await resp.json()
            return self.lists

    async def getList(self, listId:int) -> Dict:
        async with self.session.get(self.apiUrl + f"/households/{listId}/current") as resp:
            _list = await resp.json()
            return _list
                
