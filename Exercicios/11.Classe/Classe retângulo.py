class Retangulo():

    def __init__(self, p1 , p2):
        self.h = abs(p2.y - p1.y)
        self.w = abs(p2.x - p1.x)


    def calcula_perimetro(self):
        perimetro = 2*(self.h+self.w)
        print(perimetro)
        return perimetro

    def calcula_area(self):
        area = self.h*self.w
        print(area)
        return area
