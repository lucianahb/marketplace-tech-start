from datetime import datetime, time


class Log:
    def __init__(self, description:str, date: datetime = None, hour: time = None, id: int = None) -> None:
        self.__id = id
        self.__description = description
        self.__date = date
        self.__hour = hour

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def date(self) -> datetime:
        return self.__date
 
    @property
    def description(self) -> str:
        return self.__description    
    
    @property
    def hour(self) -> time:
        return self.__hour    
    
    @id.setter
    def id(self, id)-> None:
        self.__id = id
    
    @date.setter
    def date(self, date) -> None:
        self.__date = date
 
    @description.setter
    def description(self, description) -> None:
        self.__description = description
        
    @hour.setter
    def hour(self, hour) -> None:
        self.__hour = hour        