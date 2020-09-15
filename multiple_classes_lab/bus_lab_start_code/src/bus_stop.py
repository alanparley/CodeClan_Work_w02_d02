class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_person_to_queue(self, person_in_queue):
        self.queue.append(person_in_queue)

    def clear_bus_stop(self):
        self.queue.clear
