from configparser import ConfigParser
from python_grosh import GroshApp
from asyncio import get_event_loop

if __name__ == "__main__":
    c = ConfigParser()
    c.read("config.ini")
    grosh = GroshApp(c)
    loop = get_event_loop()
    loop.run_until_complete(grosh.startup())
