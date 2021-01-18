class Seller:
    
    def __init__(self,name: str, tel: str, email: str, id:int = None) -> None:
        self.__id = id
        self.__name= name
        self.__tel=tel
        self.__email=email

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def tel(self):
        return self.__tel

    @property
    def email(self):
        return self.__email

    @id.setter
    def id(self,id):
        self.__id=id

    @name.setter
    def name(self,name):
        self.__name=name

    @tel.setter
    def tel(self,tel):
        self.__tel=tel

    @email.setter
    def email(self,email):
        self.__email=email

    def __str__(self):
       return str(id(self))
