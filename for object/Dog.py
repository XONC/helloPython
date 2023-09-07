from Animal import Animal
class Dog(Animal):
    # self 相当于this
    def __init__(self, breed, name, spot,len):
        Animal.__init__(self)
        self.breed = breed
        self.name = name
        self.spot = spot
        self.len = len
    def __str__(self):
        print(f'{self.name} and {self.breed}')
    def __len__(self):
        return self.len
    # 使用 del 关键字删除类时，会调用此方法
    def __del__(self):
        print('被删除了')

    def shout(self):
        print(f'Wooo!!,{self.name}')
    def speck(self):
        print('sd')