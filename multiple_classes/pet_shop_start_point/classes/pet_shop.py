class PetShop:
    
    def __init__(self, shop_name, list_of_pets_in_shop, cash_in_till):
        self.name = shop_name
        self.pets = list_of_pets_in_shop
        self.total_cash = cash_in_till              # the self.<name> values must match up to the names which are expected in the assertequal part of the tests. on the right hand side names can be internally changed (within the class or the method) to the users specifications.
        self.pets_sold = 0

    def funcname(self, parameter_list):
        pass
    
