class Order:
    __idGen = 0
    
    @classmethod
    def nextId(cls):
        cls.__idGen += 1
        return cls.__idGen - 1
    
    def __init__(self, client, driver):
        self.__id = Order.nextId()
        self.client = client
        self.driver = driver
    
    @property
    def id(self):
        return self.__id
        
        

class OrderTomato:
    __orders: list[Order] = []
    
    @classmethod
    def addNewElement(cls, el):
        cls.__orders.append(el)
    
    @classmethod
    def listPurchases(cls, order: Order):
        return  list(filter(lambda x: x.order == order.id, cls.__orders))
        
    
    def __init__(self, order: Order, sort: str, amount: int):
        self.__oid = order.id
        self.__sort = sort
        self.__amount = amount
        OrderTomato.addNewElement(self)

        
    @property 
    def order(self):
        return self.__oid
        
    @property 
    def sort(self):
        return self.__sort
    
    @property 
    def amount(self):
        return self.__amount
