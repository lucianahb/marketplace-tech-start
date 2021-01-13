class Category:
    
    
    def __init__(self, name:str, description:str = None, id: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description
