from menu import Pizza,Burger,Drinks,Menu
from restaurant import Restaurant
from user import Chef,Server,Customer,Manager 
from order import Order


def main():
    menu = Menu()


    pizza_1 = Pizza('Shutki Pizza' ,600, 'large', ['shutki','onions'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('Alur vorta pizza', 400, 'large', ['potato','onion','oil'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza ('Dal pizza',500, 'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza_3)

    #add burger to the menu

    burger_1=Burger('Naga burger', 1000, 'chicken' , ['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2=Burger('Beef burger', 1200, 'beef' , ['sos','tomato'])
    menu.add_menu_item('burger',burger_2)
  
   #add drinks to the menu
    coke = Drinks('Coke' , 50, True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Mocha', 300 , False)
    menu.add_menu_item('drinks',coffee)
  # show menu
    menu.show_menu()


    restaurant= Restaurant('Sai Baba Restaurant', 2000, menu)
    
    manager = Manager('Kala',555,'kala@chan.com','kaliapur', 1500, 'janu 01 2020' ,'core')
    restaurant.add_employee('manager',manager)
    
    chef = Chef('kopa', 6, 'kopa@com', 'rustamnagar', 3500, 'feb01 2021', 'Chef','everything')

    
    
    server = Server('Chotu', 25, 'naijai.com', 'rasta', 200, 'march 10 2020', 'server')
    restaurant.add_employee('server',server)  

#show  employees
    restaurant.show_employees()

#customer 1 placing an order 
    customer_1 = Customer('Shakib khan', 6, 'sk@com','banani',10000)
    order_1 = Order(customer_1, [pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

#customer 1 pay for order 1
    restaurant.receive_payment(order_1, 2000, customer_1)

    print(restaurant.revenue, restaurant.balance)

#customer 2 placing an order 
    customer_2 = Customer('Shakib Al Hasan', 6, 'sk75@com','banani',10000)
    order_2 = Order(customer_2, [pizza_1,burger_1,coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

#customer 1 pay for order 1
    restaurant.receive_payment(order_2, 2000, customer_2)#customer 1 placing an order 
    customer_1 = Customer('Shakib khan', 6, 'sk@com','banani',10000)
    order_1 = Order(customer_1, [pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

#customer 1 pay for order 1
    restaurant.receive_payment(order_2, 2000, customer_2)




# call the main 
if __name__ == '__main__':
    main()