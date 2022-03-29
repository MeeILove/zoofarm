#программа Зооферма

import random

hunger_list = ['Сытый', 'Проголодался', 'Голодный']
boredom_list = ['Счастлив', 'Так себе', 'Уныние']
names_list = ['Барсик', 'Шарик', 'Мурзик', 'Бобик', 'Тузик', 'Бим', 'Тим']

class Critter():
    def __init__(self):
        print("Появилось на свет новое животное!")
        self.name = random.choice(names_list)
        self.hunger = random.choice(hunger_list)
        self.boredom = random.choice(boredom_list)
    def mood(self, mood):
        mood = ""
        if self.hunger == 'Сытый' and self.boredom == 'Счастлив':
            mood = "Отлично"
        elif self.hunger == 'Проголодался' and self.boredom == 'Так себе':
            mood = "Нормально"
        elif self.hunger == 'Голодный' and self.boredom == 'Уныние':
            mood = "Грустно"
        else:
            mood = 'Мне нужны внимание и забота'
        return str(mood)
    def talk(self):
        print('Меня зовут '+ self.name)
        print('Сейчас я ' + self.hunger)
        print(self.boredom + ' - моё состояние')
        print("Настроение - ", self.mood)





crit1 = Critter()

crit1.talk()        