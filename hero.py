# 1)создать класс SuperHero с атрибутом класса people='people'

# def name(a,b):...
# class SuperHero:
#     people ='people'

# 2)создать конструктор класса с атрибутами name,nickname,superpower,health_points,
# catchphrase.

    # def __init__(self,name,nickname,superpower,health_points):
    #     self.name = name
    #     self.nicname = nickname
    #     self.superpower = superpower
    #     self.health_points = health_points

# 5) добавить магический метод который 
# выводит прозвище героя,его суперспособность и его здоровье


    # def __str__(self):
    #     return f'{self.name}\n' \
    #            f'{self.nicname}\n' \
    #            f'{self.superpower}\n' \
    #            f'{self.health_points}'

# 6)создать магический метод который считает длину коронной фразы героя 

#     def __len__(self):
#         return len(self)           

# a = SuperHero('Tony Stark','stark','iron man',100)
# print(len(a.name))

# 3)добавить метод который выводит имя героя

# print(a.name)

# 4)добавить метод который умножает здоровье героя на 2 

# print(a.health_points * 2)


   
class Hero:

    people ='people'

    def __init__(self,name,nickname,superpower,health_points):
        self.name = name
        self.nicname = nickname
        self.superpower = superpower
        self.health_points = health_points


    def mul(self):
        print(self.health_points * 2) 

    def __str__(self):
        return f'{self.name}\n' \
               f'{self.nicname}\n' \
               f'{self.superpower}\n' \
               f'{self.health_points}'  

    
    def yuname(self):
        print (f'name is {self.name}')


    def __len__(self):
        return len(self.name) 

a = Hero('Tony Stark','stark','iron man',100)
# print(a)
# a.yuname()
# a.mul()
# print(len(a.name))

class Hero1(Hero):
    h = 1

    def __init__(self, name, nickname, superpower, health_points, fly = False):
        Hero.__init__(self,name, nickname, superpower, health_points)

        self.fly = fly

    def print_name_hero(self):
            print(f'{self.health_points ** 2}')
            self.fly = True

    def __str__(self):
        return f'{self.name}\n' \
               f'{self.nicname}\n' \
               f'{self.superpower}\n' \
               f'{self.health_points}' 

    def fly_true(self):
            print(f' fly in the True_phrase')    

p = Hero1('Piter Parker','parker','spider',150)
p.print_name_hero()
p.fly_true()
class Hero2(Hero):
    P = 1
    def __init__(self, name, nickname, superpower, health_points, fly = False):
        super().__init__(name, nickname, superpower, health_points)
        self.fly = True

    def print_name_hero(self):
            print(f'{self.health_points ** 2}')
            self.fly = True

    def __str__(self):
        return f'{self.name}\n' \
               f'{self.nicname}\n' \
               f'{self.superpower}\n' \
               f'{self.health_points}'    

    def fly_true(self):
            print(f'fly in the True_phrase')    

c = Hero2('Capitan America','mistitel','the winter soldier',200)
c.print_name_hero()
c.fly_true()
class Hero3(Hero):
    s = 1

    def __init__(self, name, nickname, superpower, health_points, fly = False):
        super().__init__(name, nickname, superpower, health_points)
        self.fly = True

    def print_name_hero(self):
            print(f'{self.health_points ** 2}')
            self.fly = True

    def __str__(self):
        return f'name is {self.name}\n' \
               f'nicname is {self.nicname}\n' \
               f'superpower is {self.superpower}\n' \
               f'health_points is {self.health_points}'        

    def fly_true(self):
            print(f'fly in the True_phrase') 

t = Hero3('Thor','thor','thunder', 300) 
# print(t)
t.print_name_hero()
t.fly_true()

