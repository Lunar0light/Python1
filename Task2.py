class Road:
    def __init__(self, lenght, width):
        self.par_road = (lenght, width)
        print(self.par_road)

    def mass_asph(self):
        print(f'm={self.par_road[0] * self.par_road[1] * 25 * 5}')

road_1 = Road(10, 10)
road_1.mass_asph()