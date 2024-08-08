#!/usr/bin/python3

class Customer:

    def __init__(self, fname, lname, purchase=0.00):
        if not isinstance(fname, str) or not isinstance(lname, str):
            raise TypeError("names must be of type string")
        if not isinstance(purchase, int) and not isinstance(purchase, float):
            raise TypeError("purchase amount must be of type int or float")
        self.first_name = fname
        self.last_name = lname
        self.purchase = purchase

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_discount(self):
        self.purchase = int(self.purchase * Customer.discount)

    discount = 0.95
