class Car :
    def __init__(self, brand, model):
     self.brand = brand
     self.model = model
    def full_name(self):
        return f"{Self.brand} {self.model}"
    class Electriccar(car):
        def __init__(self,brand,model,battery_size):
          super().__init__(brand, model)
          self.battery_size = battery_size
My_tesla = ELectricCar("Tesle","Models""85KWH")
print(My_tesla.model)
print(My_tesla.full_name())
