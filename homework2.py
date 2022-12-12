class SuperHero:
    people ='people'
    fly = True
    def __init__(self,name,nickname,superpower,health_points):
        self.name = name
        self.nicname = nickname
        self.superpower = superpower
        self.health_points = health_points

    def __str__(self):
        return f'name is {self.name}\n' \
            f'nicname is {self.nicname}\n' \
                f'superpower is {self.superpower}\n' \
                    f'health_points is {self.health_points}'    

hero = SuperHero('Tony stark','stark','iron man',100)        
print(hero)


class Spiderman(SuperHero):
    fly = False
    
    def __init__(self, name, nickname, superpower, health_points):
        super().__init__(name, nickname, superpower, health_points)

spiderman = Spiderman('Piter Parker','parker','spider',150)
print(spiderman)   

class Kapitan(Spiderman):...

kapitan = Kapitan('Capitan America','mistitel','the winter soldier',200)
print(kapitan)
