# coding: utf-8
import math
"""Working with classes"""


class Customer:
    """A customer of XYZ bank with a savings account."""

    def __init__(self, name, balance=0.0):
        """Return a Customer object"""
        # self.name = name
        self.__name = name
        self.__balance = balance

    def get_name(self):
        """Returns the customer's name"""
        return self.__name

    def set_name(self, name):
        """Sets the customer's name"""
        self.__name = name

    def get_balance(self):
        """Returns the customer's balance"""
        return self.__balance

    def set_balance(self, balance):
        """Sets the customer's balance"""
        self.__balance = balance

    @property
    def name(self):
        """The @property decorator makes this function become a property
        that can be accessed by:
        c1 = Customer()
        c1.name --> where name is not a function, but now a property
        """
        print("inside the getter")
        return self.name

    # @name.setter
    # def name(self, input_name):
    #     print("inside the setter")
    #     self.name = input_name

    def withdraw(self, amount):
        """Allow withdrawal and return remaining
        balance"""
        if amount > self.get_balance():
            raise RuntimeError("Amount is greater than balance")
        bal = self.get_balance()
        bal -= amount
        return bal

    def deposit(self, amount):
        """Allow deposit and return remaining balance"""
        bal = self.get_balance()
        bal += amount
        return bal

    def __str__(self):
        """Returns a human-readable string of the class and an instance object"""
        return self.get_name() + ": " + str(self.get_balance())

    def __unicode__(self):
        """Returns a human-readable string representation of a Customer for < Python 3"""
        return self.get_name() + ": " + str(self.get_balance())

Jerome = Customer("Jerome", 2345.00)
# Jerome.set_name("Chris")
# print(Jerome.get_name())
Jerome.get_name()
# print(Jerome.deposit(30000.00))
# print(Jerome.withdraw(3000.00))

# Jerome.withdraw(20)
# print(Customer.withdraw(Jerome, 20))
