#обычно все переключения светоформа происходят через жёлтый,
#но требование проргаммы чётко установлено
#вызов класса сопровождается вводом начального сигнала светофора

from time import sleep #для приостановления действий

class TrafficLight:
    def __init__(self, color):
        self.n_color = color

    def _running(self):
        print('running:')
        if self.n_color == 'red':
            print(self.n_color)
            sleep(7)
            color = 'yellow'
            print(color)
            sleep(2)
            color = 'green'
            print(color)
            sleep(5)

        elif self.n_color == 'yellow':
            print(self.n_color)
            sleep(2)
            color = 'green'
            print(color)
            sleep(5)
            color = 'red'
            print(color)
            sleep(7)

        elif self.n_color == 'green':
            print(self.n_color)
            sleep(5)
            color = 'red'
            print(color)
            sleep(7)
            color = 'yellow'
            print(color)
            sleep(2)

        else:
             exit(1)


traf_li=TrafficLight('red')
traf_li._running()