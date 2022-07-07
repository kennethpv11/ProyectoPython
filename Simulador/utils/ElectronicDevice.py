import random
from datetime import datetime


class ElectronicDevice:

    def __init__(self):
        self.VALUE_MIN = 10
        self.VALUE_MAX = 100
        self.__id = "LXA230"
        self.__measure = "kh"

    def generateValue(self):
        magnitude = random.randint(self.VALUE_MIN, self.VALUE_MAX)
        return {"device": self.__id, "magnitude": magnitude, "measure": self.__measure,
                "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}
