
from datetime import datetime as d

class Event:
    def __init__(self, name: str, start: d, end: d, color: tuple, desc: str):
        self.name = name
        self.start = start
        self.end = end
        self.color = color
        self.desc = desc

    def __str__(self):
        return f"{self.name} from {self.start} to {self.end}"
