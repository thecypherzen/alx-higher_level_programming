#!/usr/bin/python3

class Customer:
    """A customer class For example

    Example:
    >>> customer1 = Customer("Larry", "Barry", 13000)
	>>> customer1.full_name
	'Larry Barry'
	>>> customer1.email
	'Larry.Barry@email.com'
	>>> customer1.apply_discount()
	>>> customer1.purchase
	12350
    """

    def __init__(self, fname, lname, purchase=0.00):
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()