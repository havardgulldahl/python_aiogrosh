from configparser import ConfigParser
from python_grosh import GroshApp
from asyncio import get_event_loop

if __name__ == "__main__":
    # shorter because we're lazy termnial users
    from pprint import pprint as pp

    # read settings, see config.ini.example
    c = ConfigParser()
    c.read("config.ini")
    grosh = GroshApp(c)
    # set up session, etc
    loop = get_event_loop()
    loop.run_until_complete(grosh.startup())

    # find all grosh lists
    lists = loop.run_until_complete(grosh.getLists())

    # find a list with grocery items
    some_list = [l for l in lists if l.get("size", 0) > 2][-1]

    # get  that list
    shoppinglist = loop.run_until_complete(grosh.getList(some_list.get("id")))
    pp(shoppinglist)
