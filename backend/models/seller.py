class Seller:
    
    def __init__(self,name: str, tel: str, email: str, id:int = None) -> None:
        self.id = id
        self.name= name
        self.tel=tel
        self.email=email