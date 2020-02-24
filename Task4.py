class Car:
    def __init__(self, us_speed, us_color, us_name, us_is_police):
        self.name = us_name
        self.color = us_color
        self.speed = us_speed
        self.is_police = us_is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина повернула направо')
        elif direction == 'left':
            print('Машина повернула налево')

    def show_speed(self):
        print('speed=', self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('speed=', self.name, self.color, self.speed, 'ПРЕВЫШЕНИЕ СКОРОСТИ!')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('speed=', self.name, self.color, self.speed, 'ПРЕВЫШЕНИЕ СКОРОСТИ!')

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass


car_1 = Car(50, 'black', 'Mazda', False)
car_1.go()

car_2 = Car(60, 'white', 'Tesla', True)
car_2.turn('right')
car_2.stop()
car_2.show_speed()

car_1=WorkCar(50, 'black', 'Mazda', False)
car_1.show_speed()