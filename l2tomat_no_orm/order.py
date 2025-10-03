from user import Driver, ATBprovider, Client

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


class OrderService:
    @staticmethod
    def create_order(client: Client):
        l = list(filter(lambda x: not x.busy, Driver.get_driver_index()))
        if len(l) == 0:
            return None
        l[0].busy = True
        return Order(client, l[0])
    
    @staticmethod
    def addTomato(order: Order, sort: str, amount: int):
        return OrderTomato(order, sort, amount)
    
    @staticmethod
    def create_ATB_order(atb: ATBprovider):
        if not atb.busy:
            atb.busy = True
            return Order(atb, atb)