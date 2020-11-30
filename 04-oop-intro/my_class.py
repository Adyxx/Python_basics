import random

class Square:
    default_color = 'bílý'
    picture_on_object = ''
    name_of_object = ''
    size_of_side = 50   # cm


    def __init__(self, name, size, pic):
        self.size = size
        self.pic = pic
        self.name = name
        self.color = Square.default_color

    def __str__(self):
        return f'[ {self.name} ] : [ {self.size}x{self.size} {self.color} čtverec {self.pic} ]'

    def __eq__(self, other):
        return self.color == other.color and self.pic == other.pic and self.size == other.size

    def __gt__(self, other):
        return self.size > other.size

    def __sub__(self, other):
        return abs(self.size - other.size)**2

    def __add__(self, other):
        return self.size+other.size

    @staticmethod
    def random_color():
        return '#' + ''.join([str(hex(random.randint(0,255)))[2:] for i in range(3)])

    @classmethod
    def classm(cls, size, x_max, y_max):
        return cls(random.randrange(size), random.randrange(x_max), random.randrange(y_max))

    def draw(self):
        print(f' ## Object: {self.size}x{self.size} {self.pic}, barva: {self.color}')

    def calc(self, n):
        return self.pic == n.pic

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            value = int(value)
            if value > Square.size_of_side:
                raise Exception(f'Velikost čtverce je větší než velikost, která je nastavena jako výchozí [{Square.size_of_side}]')
            self.__size = value
        except ValueError:
            raise ValueError('Zadaná velikost není číslo.')

class InfoSquare(Square):
    def __init__(self, name, size, pic, surname):
        super().__init__(name, size, pic)
        self.surname = surname

    def __str__(self):
        return f'[ {self.surname} {self.name} ] : [ {self.size}x{self.size} {self.color} čtverec {self.pic} ]'



print("----------------------------")
square01 = Square('Cactus', 20, 'bez obrázku')
print(square01)

Square.default_color = 'žlutý'
square02 = Square('JustOrdinarySquare', 30, 's obrázkem banánu')
print(square02)

if square01 == square02:
    print(" --> Porovnávané objekty jsou stejné")
else:
    print(" --> Porovnávané objekty jsou rozdílné.")

if square01 > square02:
    print(" --> První objekt je větší než ten druhý.")
else:
    print(" --> Druhý objekt je větší než ten první.")

print(" --> Rozdíl obsahu objektů je",(square01 - square02),"cm2")
print(" --> Velikost nového objektu je "+str((square01+square02))+"x"+ str((square01+square02)))

print([Square.random_color() for i in range (5)])

print([Square.classm(10,20,20)for i in range (5)])

square02.draw()
if square02.calc(square01):
    print(" --> Oba objekty jsou",square01.pic)
else:
    print(" --> Obrázky objektů se neshodují")

square03 = Square('NewSq', 24, 'bez obrázku')

if square01.calc(square03):
    print(" --> Oba objekty jsou",square01.pic)
else:
    print(" --> Obrázky objektů se neshodují")

Square.default_color = 'červený'
square04 = InfoSquare('Jahoda', 42, 'bez obrázku','Lahodná')
print(square04)


# square05 = Square('Wrong', 80, 'X')         čtverec je větší než 50 (defaultně nastaveno v size_of_side) -- vyhodí chybu