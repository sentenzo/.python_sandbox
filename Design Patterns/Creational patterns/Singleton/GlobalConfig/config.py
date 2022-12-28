from singleton_meta import SingletonMeta
import json

class Config(metaclass=SingletonMeta):
    path = "default_path_to_config.json"

    def __init__(self) -> None:
        with open(Config.path) as json_file:
            data = json.load(json_file)
            for prop in data:
                self.__dict__[prop] = data[prop]