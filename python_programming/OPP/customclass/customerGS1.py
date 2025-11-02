class Customer():
    def __init__(self, name, balance):
        self.name = name
        self.__set_balance(balance)

    def __get_balance(self):
        return self.__balance
    def __set_balance(self, balance):
        if balance < 0:
            self.__balance = 0
        elif balance > 1000:
            self.__balance = 1000
        else:
            self.__balance = balance

    balance = property(__get_balance, __set_balance)

customer1 = Customer("user", 1000)
print(customer1.balance)
# customer1.display_balance()

#