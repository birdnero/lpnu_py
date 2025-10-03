from abc import ABC, abstractmethod


class User():
    
    def __init__(self, name: str, surname: str, login: str, passwd: str):
        if login == None or passwd == None or len(login) <= 6:
            raise ValueError("bad login or passwd")
        self.name = name
        self.surname = surname
        self.__login = login
        self.__passwd = passwd
        
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, v: str):
        if v is not None and len(v) > 6:
            self.__login = v
    
    def __str__(self):
        return f"Hello, I'm {self.name} {self.surname}, but for u, I am {self.__login} and {self.__class__.__name__}"
    
    @property
    def passwd(self):
        return self.__passwd
    
    def passwd_ch(self, old_passwd: str, new_passwd = None):
        if old_passwd == self.__passwd:
            if(new_passwd is not None):
                self.__passwd = new_passwd
            return True
        return False
    
    


class Imaker(ABC):
    @abstractmethod
    def make(self, user: User):
        pass


        
        
class Client(User, Imaker):
    
    @classmethod
    def make(cls, user: User):
        return Client(name=user.name, surname=user.surname, login=user.login, passwd=user.passwd)
    
    def __init__(self, purchases: int = 0, bonuses: int = 0, bankId: str = None, card: str = None, debt: int = 0, **kwargs):
        super().__init__(**kwargs)

        if purchases < 0 or bonuses < 0:
            raise ValueError("purchases/bonuses must be >= 0")

        if not (debt <= 0 or (bankId is not None and card is not None)):
            raise ValueError("invalid debt condition")

        self.purchases = purchases
        self.bonuses = bonuses
        self.__bankId = bankId
        self.__card = card
        self.debt = debt
        
    @property
    def bankId(self):
        return self.__bankId
    
    @bankId.setter
    def bankId(self, v: str):
        if v is not None and len(v) == 16:
            self.__bankId = v
            
    @property
    def card(self):
        return self.__card
    
    @card.setter
    def card(self, v: str):
        if v is not None and len(v) == 16:
            self.__card = v
            




class Driver(User, Imaker):
    __driver_index: list = []
    
    @classmethod
    def get_driver_index(cls):
        return cls.__driver_index.copy()
        
    @classmethod
    def make(cls, user: User):
        return Driver(name=user.name, surname=user.surname, login=user.login, passwd=user.passwd)
    
    def __init__(self, busy: bool = 0, deliveryPrice: int = 0, coordinats: str = None, **kwargs):
        super().__init__(**kwargs)

        if deliveryPrice < 0:
            raise ValueError("deliveryPrice must be >= 0")

        self.busy = busy
        self.deliveryPrice = deliveryPrice
        self.__coo = coordinats
        Driver.__driver_index.append(self)
        
    
    @property
    def coordinats(self):
        return self.__coo
    
    
    
    
class ATBprovider(Client, Driver, Imaker):
    
    @classmethod
    def make(cls, user: User):
        return ATBprovider(name=user.name, surname=user.surname, login=user.login, passwd=user. passwd)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    