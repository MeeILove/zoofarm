#программа Зооферма

import random

hunger_list = [1, 2, 3] #1 - хорошо, 2 - средне, 3 - плохо 
boredom_list = [1, 2, 3] #1 - хорошо, 2 - средне, 3 - плохо 
names_list = ['Барсик', 'Шарик', 'Мурзик', 'Бобик', 'Тузик', 'Бим', 'Тим']

class Critter():
    def __init__(self):
        print("Появилось на свет новое животное!")
        self.name = random.choice(names_list)
        self.hunger = random.choice(hunger_list)
        self.boredom = random.choice(boredom_list)
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    def eat(self, food):
        food = int(input('Какое кол-во еды хотите дать (от 1 до 3)?'))
        print('Мммм, вкусно, Спасибо!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, game):
        game = int(input('Какое кол-во времени вы хотите поиграть(от 1 до 3)?'))
        print('Вау, круто, Спасибо!')
        self.boredom -= game
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def mood(self, mood):
        moody = self.hunger + self.boredom
        if moody < 2:
            mood = "Отлично"
        elif  2<moody<=4:
            mood = "Нормально"
        elif 4<moody<=9:
            mood = "Грустно, мне нужны внимание и забота"
        else:
            mood = 'Мне нужны внимание и забота'
        return mood
    def talk(self):
        print('Меня зовут '+ self.name)
        print('Уровень голода - ' , self.hunger)
        print('Уровень уныния - ' , self.boredom)
        print("Настроение - ", end = '')
        self.__pass_time()

    # choice = None
    # while choice != 0:
    #     print \
    #         ('''
    #         Моё животное 

    #         0 - выйти
    #         1 - узнать о самочувствии животного
    #         2 - покормить животное
    #         3 - поиграть с животным 
    #         ''')
    #     choice = input('Ваш выбор: ')
    #     print()
    #     if choice == '0':
    #         print('До свидания!')
    #     elif choice == '1':
    #         crit.talk()
    #     elif choice == '2':
    #         crit.eat()
    #     elif choice == '3':
    #         crit.play()
    #     else:
    #         print('\nИзвините, неверная команда', choice)







crit = Critter()

crit.talk()
print(crit.mood(mood= ""))

choice = None
while choice != 0:
    print \
    ('''
        Моё животное 
        0 - выйти
        1 - узнать о самочувствии животного
        2 - покормить животное
        3 - поиграть с животным 
    ''')
    choice = input('Ваш выбор: ')
#choice = input('Ваш выбор: ')
    print()
    if choice == '0':
        print('До свидания!')
        break
    elif choice == '1':
        crit.talk()
    elif choice == '2':
        crit.eat(food= 1)
    elif choice == '3':
        crit.play(game= 1)
    else:
        print('\nИзвините, неверная команда', choice)
