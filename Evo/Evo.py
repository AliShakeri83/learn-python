class Evo:
    def __init__(self):
        self.driver = None
        self.distance = 0

    def start_rental(self, name):
        self.driver = name
        if self.driver != None:
            raise RuntimeError

    def drive(self, num):
        self.distance += num
        if num < 0:
            raise AttributeError
        else:
            raise RuntimeError

    def end_rental(self):
        distance = self.distance
        self.driver = None
        self.distance = 0
        if self.driver == None:
            raise RuntimeError
        return distance
