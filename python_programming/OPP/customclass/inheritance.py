import random
class Person:
    def __init__(self,name,phone_number,address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = ""

        # self.phone_number = 1000

    def update_contact(self,new_number):
        self.phone_number = new_number
        print(f"The phone number has been updated to {self.phone_number}.")

# new_person = Person()
# print(new_person)
# print(new_person.phone_number)
# new_person.update_contact(1000)
# print(new_person.phone_number)

# class Customer:
#     def __init__(self):
#         pass
#
#     def purchase(self, item):
#         print(f"The item {item} has been purchased")
#
# new_customer = Customer()
# new_customer.purchase("Coffee")


class Customer (Person):
    def __init__(self,name):
        super().__init__(name=name,phone_number="",address="")
        self.customer_id = random.randint(1,100)

    def purchase(self, item):
        print(f"The item {item} has been purchased.")

new_customer_00 = Customer("User1")
print(new_customer_00.name)
new_customer_01 = Customer("User2")
print(new_customer_01.name)
new_customer_00.purchase("Coffee")
new_customer_00.update_contact("1000")
print(new_customer_00.customer_id)
print(new_customer_00.email)
new_customer_00.email = "user@email.com"
print(new_customer_00.email)
