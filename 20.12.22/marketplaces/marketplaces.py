class Marketplace:
    def __init__(self, Marketplace: str):
        self.__namemkp = Marketplace

    def get_name(self) -> str:
        return self.__namemkp

    def __str__(self) -> str:
        return f'''{self.__namemkp}'''


class Category:
    def __init__(self, Category: str, Marketplace: Marketplace):
       self.__catmkp = Category
       self.__parent = Marketplace

    def get_name(self) -> str:
        return self.__catmkp

    def get_parentname(self) -> str:
        return self.__parent.get_name()


class Subcategory:
    def __init__(self, Subcategory: str, Category: Category):
        self.__subcat = Subcategory
        self.__parent = Category

    def get_subcat(self) -> str:
        return self.__subcat
    
    def get_parentname(self) -> str:
        return self.__parent.get_name()


class Dados:
    def get_mktplaces():
        mktplaces = []
        arq = open('dados/mkplaces.txt', 'r')
        for i in arq:
            i = i.strip() #tira o \n
            i = {'mktplace':i} 
            mktplaces.append(i)
        arq.close()
        return mktplaces

    def get_cat():
        cat = []
        arq = open('dados/categorias.txt', 'r')
        for i in arq:
            i = i.strip() #tira o \n
            j = i.split(';')
            i = {'categoria':j[1], 
                'mkplace':j[0]
            } 
            cat.append(i)
        arq.close()
        return cat
        
    def get_subcat():
        subcat = []
        arq = open('dados/subcategorias.txt', 'r')
        for i in arq:
            i = i.strip() #tira o \n
            j = i.split(';')
            i = {'subcategoria':j[1], 
                'categoria':j[0]
            } 
            subcat.append(i)
        arq.close()
        return subcat