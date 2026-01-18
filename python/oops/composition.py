class Engine:

    def __init__(self):
        print("In the Init Method")

    def start(self):
        print("Starting the engine")


class Car:

    def __init__(self, engine):
        print('In the init method of Car')
        self.engine = engine

    def start(self):
        self.engine.start()


engine = Engine()
car = Car(engine)
car.start()
