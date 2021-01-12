class Seller:
    
    def __init__(self,name_seller: str, tel: str, email: str, id:int =None) -> None:
        self.id = id
        self.name_seller = name_seller
        self.tel=tel
        self.email=email