class OrderList:
    def __init__(self):
        #self.order_number = order_number
        #self.product_name = product_name
        #self.price = price
        #self.quantity = quantity
        self.orders = []  # Список всех заказов
        #self.add_order(order_number, product_name, price, quantity)
        #self.total = float(0)
        #self.max = float
        self.max_lst = []
        
    
    #todo 1. add_order(order_number, product_name, price, quantity): добавляет заказ в список.
    def add_order(self, order_number, product_name, price, quantity):
        self.orders.append({
            'order_number': order_number,
            'product_name': product_name,
            'price': price,
            'quantity': quantity
        })
       
        
    #todo 2. remove_order(order_number): удаляет заказ по его номеру.
    def remove_order(self, order_number):
        for elem in self.orders: # elem это целый словарь, карточка заказа
            if elem ["order_number"] == order_number:
                self.orders.remove(elem)
                           
    #todo 3. calculate_total(): возвращает общую сумму всех заказов.
    def calculate_total(self): 
        total = []
        for elem in self.orders:
            total.append( elem['price'] * elem['quantity'])
        print(f'Сумма всего заказа: {sum(total):.2f}')
    
    #todo 4. get_expensive_order(): находит самый дорогой заказ (по цене * количеству).
    def get_expensive_order(self):
        max_lst = []
        for elem in self.orders:    
            max_lst.append (elem['price'] * elem['quantity'])
        print("Самый дорогой заказ: ", max(max_lst))    
    
    #todo 5. display_orders(): выводит все заказы.
    def display_orders(self):
        for elem in self.orders:
           print(elem)

        
    
order_list = OrderList()
order_list.add_order(1, "Хлеб", 120.51, 10)
order_list.add_order(2, "Молоко", 119.22, 10)
order_list.add_order(3, "Масло", 220.11, 10)
order_list.add_order(4, "Апельсины", 130, 20)
#order_list.remove_order(2)
order_list.calculate_total()
order_list.get_expensive_order()
order_list.display_orders()
print(order_list)

