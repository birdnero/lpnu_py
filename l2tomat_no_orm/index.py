from user import User, Client, Driver, ATBprovider
from order import OrderTomato

u = User(name="Andriy", surname="Fediv", login="andriy123", passwd="soelceenraet123")
print(u.introduce())

client = Client.make(u)
client.purchases = 5
client.bonuses = 20
client.bankId = "1234567890123456"
client.card = "9876543210987654"
print(client.introduce())
print(f"Client bankId: {client.bankId}, card: {client.card}")

driver1 = Driver(
    busy=False,
    deliveryPrice=100,
    name="Ivan",
    surname="Petrenko",
    login="ivan555",
    passwd="pass555",
)
driver2 = Driver(
    busy=False,
    deliveryPrice=120,
    name="Petro",
    surname="Kovalenko",
    login="petro666",
    passwd="pass666",
)


print("Drivers index:", list(map(str, Driver.get_driver_index())))


order1 = client.create_order()
print(f"Order created: id={order1.id}, driver={order1.driver.name}")

client.addTomato(order1, "Cherry", 10)
client.addTomato(order1, "Roma", 5)


tomatoes = OrderTomato.listPurchases(order1)
for t in tomatoes:
    print(f"Order {t.order}: {t.amount} of {t.sort} tomatoes")


provider = ATBprovider.make(u)
provider.busy = False
order2 = provider.create_order()
print(f"ATBprovider order: id={order2.id}, driver={order2.driver.name}")
