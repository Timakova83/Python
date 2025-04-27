class Superhero:
    def __init__(self, name = "Неизвестный герой", power = "Неизвестная сила", money = 100 ):
        self.name = name
        self.power = power
        self.money = money
        self._secret_identity()
        
    def set_info (self, new_name, new_power):
        #TODO: метод, который устанавливает имя и суперспособность героя
        self.new_name = self.name
        self.new_power = self.power
        
    
    def earn_money(self, amount):
         #TODO: метод, который добавляет герою деньги
        self.amount = self.money  
    
    def spend_money(self, amount):
         #TODO: метод, который уменьшает деньги героя (но не даёт уйти в минус)
        self.amount = self.money
    
    def _secret_identity(self):
         #TODO: приватный метод, который возвращает строчку: "Секретная личность: [имя]"
        
        print ('Секретная личность: [имя] ')


superhero = Superhero("Vasya", 200, )
superhero.money += 20
superhero.money -= 5 

