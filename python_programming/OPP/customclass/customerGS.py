class Customer():
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        # create getter and setter method

    # def get_balance(self):
    #     return self.__balance
    #
    # def set_balance(self, balance):
    #     self.__balance = balance
    # @property
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            self.__balance = 0
        elif balance > 1000:
            self.__balance = 1000
        else:
            self.__balance = balance






# customer1 = Customer("user", 100)
# print(customer1.name)
# print(customer1.get_balance())
# # print(customer1.__balance)
#
# customer1.set_balance(200)
# print(customer1.get_balance())
# #
#
# customer2 = Customer("user2", 1000)
#
# total = customer2.get_balance() + customer1.get_balance()
# print(total)

# customer1 = Customer("user",100)
# customer1.balance = 1
# print(customer1.balance)