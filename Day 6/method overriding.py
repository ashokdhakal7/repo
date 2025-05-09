from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract Method"
        # print ("Abstract Method")
        return
class circle(shape):
    def draw(self):
        super().draw()
        print ("Draw a Circle")
        return
class rectangle(shape):
    def draw(self):
        super().draw()
        print ("Draw a Rectangle")
        return
shapes = [circle(), rectangle()]
for shp in shapes:
    shp.draw()