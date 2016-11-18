import math
#класс фигуры
class figure:
# Площадь фигуры.   
    def ploshad(): 
        pass
#метод для изменнения цвета
    def changecolor(self):
        pass
# Вывод параметров фигуры на экран.    
    def show(self): 
        pass
    
#Подкласс круг
class krug(figure):
    def __init__(self, r=0):
        self.luc = r
    def show(self):
        print("Радиус =", self.luc)
    def ploshad (self):
        return math.pi * float (self.luc) * float (self.luc)
    def changecolor(self, newcolor = "" ):
        self.color = newcolor
        print ("Цвет - ", self.color)
    
#Подкласс прямоугольник
class square(figure):
    def __init__(self, a=0, b=0):
        self.dlina = a
        self.shirina = b
        
    def show(self):
        print("Длина =", self.dlina)
        print("Ширина =", self.shirina)
        
    def ploshad(self):
        return float(self.dlina) * float(self.shirina)

    def changecolor(self, newcolor = "" ):
        self.color = newcolor
        print ("Цвет - ", self.color)
def Menu():
    vopr = 0
    print("Что вы хотите сделать?")
    print("1 - создать круг;")
    print("2 - создать прямоугольник;")
    print("3 - выход.")
    while (vopr == 0):
        vopr = input("Ваш выбор: ")
        try:
            vopr = int(vopr)
        except ValueError:
            vopr = 0
        if (vopr < 1 or vopr > 3):
            print("Ошибочка");
            vopr = 0
    return vopr

a = Menu()
if (a == 1):
    a = input("Введите радиус круга: ")
    c = input ("Введите цвет круга: ")
    s = krug(c)
    s.changecolor (c)
    f = krug(a)
    f.show ()
    print ("Площадь круга = ", f.ploshad())
    
else:
    if (a == 2):
        a = input("Введите длину прямоугольника: ")
        b = input("Введите ширину прямоугольника: ")
        c = input ("Введите цвет прямоугольника: ")
        s = square (c)
        s.changecolor (c)
        f = square(a, b)
        f.show()
        print("Площадь прямоугольника =", f.ploshad())
