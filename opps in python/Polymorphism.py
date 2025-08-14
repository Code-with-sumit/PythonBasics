class Car:
    def __init__(Self,brand,model):
        self.brand = brand
        self.model = model
    def get_brand(Self):
        return self.brand + "!"
    def full_name(self):
        return f"{self .brand}{self.model}"
    def fuel_type(Self):
        return f"{self.brand}{self.model}"
    class ElectricCar(Car):
        def __init__(Self,brand,model,battery_size):
            super().__init__(brand, model)
            self.battery_size = battary_size
    def fuel_type(self):
        return"Electric charge"
    My_tesla = ElectricCar("Tesla","Model s","85KWH")
print(My_tesla.fuel_type())
safari = Car("Tota","Safari")
print(Safari.fuel_type())