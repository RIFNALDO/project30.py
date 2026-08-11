class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class bus(Vehicle):
    def fare(self):
        base_fare = self.capacity * 100
        return base_fare * 1.10

school_bus = bus(50)
print("Total bus fare is :", school_bus.fare())