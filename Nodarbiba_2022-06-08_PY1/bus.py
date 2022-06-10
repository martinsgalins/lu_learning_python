import random


class Car:

    max_fuel = 100

    def __init__(self, model, registration_number):
        self.model = model
        self.registration_number = registration_number
        self.fuel = 0
        self.engine_started = False

    def fuel_car(self):
        if self.fuel < self.max_fuel:
            self.fuel = self.max_fuel
            print("Fuel tank is full now")
        else:
            print("Fuel tank is already full")

    def start_engine(self):
        can_start = random.randint(0, 1)
        if can_start:
            self.engine_started = True
            print("Engine started")
        else:
            print("Couldn't start the engine")

class Bus(Car):
    max_passengers = 30
    def __init__(self, model, registration_number):
        super().__init__(model, registration_number)
        self.passengers = []

    def add_passenger(self, name):
        if self.get_passenger_count() < Bus.max_passengers:
            self.passengers.append(name)
            print("Autobusa iekapa:", name)
        else:
            print("autobuss pilns!")   
    def remove_passenger(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
            print("No autobusa izkapa :",name)
        else:
            print(name, "nav autobusa") 
    def get_passenger_count(self):
        return len(self.passengers)

rigas_satiksme = Bus("asd", "LF-3515")
rigas_satiksme.add_passenger("Andris")
rigas_satiksme.add_passenger("Andris")
rigas_satiksme.add_passenger("Lauris")

print(rigas_satiksme.passengers)
print(rigas_satiksme.get_passenger_count)

rigas_satiksme.remove_passenger("Lauris")
print(rigas_satiksme.passengers)
