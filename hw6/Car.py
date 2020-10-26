class Car(object):
    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed


car1 = Car('Mercedes-AMG G 63', 'Mercedes')
for i in range(5):
    car1.accelerate()
    speed = car1.get_speed()
    print('the current speed after', i+1,'time(s) acceleration is',speed)
for i in range(5):
    car1.brake()
    speed = car1.get_speed()
    print('the current speed after', i+1 ,'time(s) brake is', speed)
