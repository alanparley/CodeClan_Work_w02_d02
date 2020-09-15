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
            if any_pet.name == name_of_pet:
                return any_pet




# do you need to use a return?
# if  functions job is to bring back data, its a return
# if the job o the function is to chane something, we dont need a return
# if you GET something, youll almost certianlyhave to RETURN something
# eg increase pets sold isnt a get, so its a change to something and no need to return - practice makes perfect.

