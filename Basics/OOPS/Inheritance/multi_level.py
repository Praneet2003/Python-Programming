class car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")
class toyootacar(car):
    def __init__(self,name):
        self.name = name
    def start(self):
        print(self.name)
        super().start()
    def stop(self):
        print(self.name)
        super().stop()
class fortuner(toyootacar):
    def __init__(self,milage,type,fuel):
        self.milage = milage
        self.type = type
        self.fuel = fuel
    def features(self):
        super().__init__("Fortuner")
        super().start()
        super().stop()
        print("Milage of the ",self.name," is ",self.milage)
        print("Type of the ",self.name," is ",self.type)
        print("fuel of the ",self.name," is ",self.fuel)
fortuner1 = fortuner(8.9,"4X4","Diesel")
fortuner1.features()