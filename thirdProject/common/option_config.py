from configparser import ConfigParser
class ConfigOpetion:
    def __init__(self):
        self.config=ConfigParser()
    def read_conf(self,section,key):
        return self.config.get(section,key)