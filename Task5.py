class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title} карандашом')
class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title} маркером')
class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title} ручкой')


pic_1 = Stationery('picture_1')
pic_1.draw()


pic_2 = Pencil('picture_2')
pic_2.draw()

pic_3 = Handle('picture_3')
pic_3.draw()

pic_4 = Pen('picture_4')
pic_4.draw()
