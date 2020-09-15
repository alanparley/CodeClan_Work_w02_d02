class PetShop:
    
    def __init__(self, shop_name, list_of_pets_in_shop, cash_in_till):
        self.name = shop_name
        self.pets = list_of_pets_in_shop
        self.total_cash = cash_in_till              # the self.<name> values (the property names) MUST match up to the names which are expected in the assertequal part of the tests. on the right hand side names can be internally changed (within the class or the method) to the users specifications.
        self.pets_sold = 0

#4
    def stock_count(self,):
        return len(self.pets)
#5    
    def increase_pets_sold(self,):
        self.pets_sold += 1
#6
    def increase_total_cash(self, cash_transaction):
        self.total_cash += cash_transaction
#7
    def add_pet(self, pet_to_add):
        self.pets.append(pet_to_add)
#8
    def remove_pet(self, pet_to_remove):
        self.pets.remove(pet_to_remove)
#9
    def find_pet_by_name(self, name_of_pet):
        for any_pet in self.pets:
            if any_pet.name == name_of_pet:         # KEEP VARIABLE NAME (any_pet) CONSISTANT!
                return any_pet
#10
    def sell_pet_to_customer(self, pet_name, customer):
        pet_to_sell = self.find_pet_by_name(pet_name)          # call a method from this class on a variable! Then pass it the input required from the method declaration.
        customer.add_pet(pet_to_sell)                           # no self. on customer because self. only refers to the class that we are currently in, customer comes from outside and so we dont need self.
        self.remove_pet(pet_to_sell)                           # invoking the earlier method in the class
        self.increase_pets_sold()
        self.increase_total_cash(pet_to_sell.price)             # we only have access to .price here because we erlier run the method find_pet_by_name which found the pet and loaded in its details including the price.




# NOTES:
# do you need to use a return?
# if  functions job is to bring back data, its a return
# if the job o the function is to chane something, we dont need a return
# if you GET something, youll almost certianlyhave to RETURN something
# eg increase pets sold isnt a get, so its a change to something and no need to return - practice makes perfect.

# dont jusst add things into the initialisation method because the methods that you write are doorways by way of which things from outside the clas can be brought in for use. keep the initialisation data to things which are native to the class in which they belong.