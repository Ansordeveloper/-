class People:
    def __init__(self,name):
        self.name = name
        



class People1:
    def __init__(self,age):
        self.age = age



class Run:
    def run(self):
        print(self,'running')

 
class Name:
    
    def names(self):
        print(self)
   
 

class People4(People,People1,Run,Name):
    def __init__(self, name,age):
        People.__init__(self,name)
        People1.__init__(self,age)
    
    def __str__(self):
        return f'{self.name} {self.age}'
human = People4('Asror', 19)



# print(human)
# human.run()
# human.names()
# print(human.age)
# print(human.name)




