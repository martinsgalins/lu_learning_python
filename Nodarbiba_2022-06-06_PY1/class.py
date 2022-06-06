import random
class Car:
    fuel_cap = 100
    def __init__(self, model, reg_nr):
        self.model = model
        self.reg_number = reg_number
        self.fuel = 0
        self.engine_on = False
    def fuel_up(self):
        if self.fuel < Car.fuel_cap:
            self.fuel = Car.fuel_cap
            print("Filled!")
        else:
            print("Already Filled!")

    def start_engine(self):
        can_start = random.randint(0, 1)
        
        if can_start: # False ja 0, True ja 1
            self.engine_on = True
            print('Engine started')
            
        else:
            print('Failed to start the engine')


my_car = Car(model="Tesla", reg_nr="AF-2234")



