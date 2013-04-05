#класс фигуры
class figure:
#изначальное значение цвета-белый
    color = "white"
#метод для изменнения цвета
    def changecolor(self, newcolor ):
        self.color = newcolor
#Подкласс овал 
class oval(figure):
    def __init__(self, r):
        self.luc = r
#Подкласс прямоугольник
class square(figure):
    def __init__(self, a, b):
        self.dlina = a
        self.shirina = b
 
f = figure()
o = oval(15)
 
s = square(25, 4)
s.changecolor("green")
 
print(o.color, o.luc)
print(s.color, s.dlina, s.shirina)