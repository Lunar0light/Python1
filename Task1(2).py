#порядок не может быть нарушен,если мы сами его прописываем
#единственная проверка это.. если первый цвет - не красный, то прервать выполнение


from time import sleep #для приостановления действий

class TrafficLight:
    def __init__(self, color):
        self.n_color = color

    def _running(self):
        print('running')
        if self.n_color =='red':
            print(self.n_color)
            sleep(7)
            color = 'yellow'
            print(color)
            sleep(2)
            color = 'green'
            print(color)
            sleep(5)
        else:
             exit(1)


traf_li=TrafficLight('red')
traf_li._running()