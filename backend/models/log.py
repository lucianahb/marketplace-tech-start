from datetime import datetime, time


class Log:
    
    
    def __init__(self, description:str, date: datetime = None, hour: time = None, id: int = None) -> None:
        self.id = id
        self.description = description
        self.date = date
        self.hour = hour
