class Customer():
    def __init__(self, name, balance, contract_name):
        self.name = name
        self.__balance = balance
        self.__contract_name = contract_name

    def display_details(self):
        print(f'Name: {self.name}, Contract Name: {self.__contract_name}')

    def display_balance(self):
        print(f"Name: {self.name}'s outstanding balance is {self.__balance}")


customer1 = Customer("user", 100, "AP-001")
customer1.display_details()
customer1.display_balance()

#