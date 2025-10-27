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
        super()
    def stop(self):
        print(self.name)
        super()
innova = toyootacar("Innova")
innova.start()