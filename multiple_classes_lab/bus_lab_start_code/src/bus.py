class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []



    def noise_made_by_bus(self):
        return "Brum brum"

    def number_of_passengers_on_the_bus(self):
        return len(self.passengers)

    def pickup(self, passenger_1):
        self.passengers.append(passenger_1)

    def dropoff(self, passenger_2):
        self.passengers.remove(passenger_2)

    def empty_the_bus(self):
        self.passengers.clear()

        