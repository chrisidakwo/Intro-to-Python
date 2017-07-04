# coding=utf-8
from working_with_classes import Customer


class CustomerInherit(Customer):
    """"""
    def __init__(self, age, name, balance):
        super().__init__(name, balance)
        self.__age = age

    def get_age(self):
        """"""
        return self.__age

    def __str__(self):
        return "(%s %s): %s" % (self.get_name(),
                                self.__age,
                                self.get_balance())


NewCustomer = CustomerInherit(21, "Chris", 230000.00)
print(NewCustomer.withdraw(12000.00))
print(NewCustomer.deposit(2303.00))
print(NewCustomer.get_age())
print(NewCustomer)

