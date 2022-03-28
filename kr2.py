class Animal(): #создаём класс Animal
    name = "name" #атрибут имени животного
    def __init__(self): #метод-конструктор выводящий надпись
        print('Родилось животное!')
    def eat(self): #метод eat выводящий надпись
        print('Ням-ням')
    def makenoise(self): #метод makenoise выводящий надпись
        print(self.name + ' говорит Гррр')
    def givename(self, newname): #метод givename присваивающий имя
        self.name = newname

class Cat(Animal): #подкласс Cat класса Animal
    name = '' #атрибут имени
    def __init__(self): #метод-конструктор выводящий надпись и вызывающий родительский конструктор
        print('Родился кот!')
        super().__init__() #вызов родительского метода-конструктора def __init__ 
    def makenoise(self): #метод makenoise подкласса Cat
        print(self.name + ' говорит Мяу!')
    

class Dog(Animal): #подкласс Dog класса Animal
    name = '' #атрибут имени
    def __init__(self): #метод-конструктор выводящий надпись и вызывающий родительский конструктор
        print('Родилась собака!')
        super().__init__() #вызов родительского метода-конструктора def __init__
    def makenoise(self): #метод makenoise подкласса Dog
        print(self.name + ' говорит Гав!')

#создаем 4 объекта: 1 кот, 2 собаки и одно простое животное
c1 = Cat()
d1 = Dog()
d2 = Dog()
a1 = Animal()


c1.givename('Joshua')
d1.givename('Frank')
d2.givename('Boris')
a1.givename('Denise')
c1.makenoise()
c1.eat()
d1.makenoise()
d1.eat()
d2.makenoise()
d2.eat()
a1.makenoise()
a1.eat()

                
