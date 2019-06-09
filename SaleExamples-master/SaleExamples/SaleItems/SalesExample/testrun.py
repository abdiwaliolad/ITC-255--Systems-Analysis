from item import Item
from orderitem import OrderItem
from order import Order
from payment import Payment
from inventory import Inventory

def menu():

    item1=Item(1,'fries', 2.25)
    item2=Item(2,'cheese burger', 5.00)
    item3 =Item(3,'chicken burger', 5.25)
    item4=Item(4,'milk shike', 4.00)

    inventory=Inventory()
    inventory.addItem(item1)
    inventory.addItem(item2)
    inventory.addItem(item3)
    inventory.addItem(item4)

    orderitem1=OrderItem(inventory.getItemByNumber(1),1)
    orderitem2=OrderItem(inventory.getItemByNumber(2),2)
    orderitem3=OrderItem(inventory.getItemByNumber(3),1)
    orderitem4=OrderItem(inventory.getItemByNumber(4),4)

    order = Order()
    order.addOrderItems(orderitem1)
    order.addOrderItems(orderitem2)
    order.addOrderItems(orderitem3)
    order.addOrderItems(orderitem4)

    payment =order.calcTotal()
    print(payment)

menu()