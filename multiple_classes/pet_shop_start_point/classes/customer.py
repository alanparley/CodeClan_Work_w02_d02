class Customer:                         # capitalisation of the start of the class name and its pascal camel case helps to differenciate between methods and functions

    def __init__(self, name, cash):     # every __init__ needs a self, as the first declaration. Think of this as a function with the parameters name nd cash
        self.name = name                # this decalres that class Customer name in def__init__ is name? declared properties CAN ONLY GO ON THE RIGHT. If it makes it easier, use input_name and input_cash to help you differentiate in your brain.
        self.cash = cash                # so using self.cash would be corresponding to customer.cash in the test you run (self. refers back to the Customer class).
        self.pets = []                  # all of these self.X are properties. Properties which we set up do not need to be declared properties. Here this INSTANCE VARIABLE of self.pets means every new customer creted will have by default an empty list for their pets, this means that we dont need to pass in an empty list for this parameter each time. This is useful for when you have default values (eg wheels on a car). It is named pets and not pet_count because we need the entire pet obect here in order to then be able to do more than one thing with it. Having an additoonal pet_count as well would be redundent because we can get pet_count through the pets anyway.

    def pet_count(self):
        return len(self.pets)           # customer.pet_count() would return the same as len(customer.pets) but its MUCH CLEANER. Get into this good habit of accessing the method from the class and not invoking a function on a class data structure.


    def add_pet(self, added_pet):
        self.pets.append(added_pet)     # no return statement required because this method is adding a pet to the pets list and the test checks the list.

    def get_total_value_of_pets(self):  # we dont need any parameters because all of the information that we need for the method is in the class the method is in. We need additional parameters if we need data from outside the class. External data becomes part of the costomer class once it is brought in as a prameter for the method.
        total = 0
        for pet in self.pets:
            total += pet.price

        return total

    



