class Human():

    def __init__(self,
                 name = "no name",
                 age = 0,
                 gender = "no gender",
                 nationality = "no nationality"):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def say(self):
        print('Здравствуйте, {} ! Вам {} лет, Ваш пол: {} ,Ваша национальность: {}'.format(self.name, self.age, self.gender, self.nationality))

Person = Human()
Person.name = input('Введите ваше Имя:')
Person.age = input('Введите ваш Возраст:')
Person.gender = input('Введите ваш пол:')
Person.nationality = input('Введите вашу национальность:')

Person.say()
        
