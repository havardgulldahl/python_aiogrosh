from configparser import ConfigParser
from python_grosh import GroshApp
from asyncio import get_event_loop

if __name__ == "__main__":
    from pprint import pprint as pp

    c = ConfigParser()
    c.read("config.ini")
    grosh = GroshApp(c)
    loop = get_event_loop()
    loop.run_until_complete(grosh.startup())

    lists = loop.run_until_complete(grosh.getLists())

    some_list = [l for l in lists if l.get("size", 0) > 2][-1]

    pantry = loop.run_until_complete(grosh.getList(some_list.get("id")))
    pp(pantry)
