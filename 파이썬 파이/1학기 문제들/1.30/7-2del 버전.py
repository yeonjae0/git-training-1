class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    def bark(self):
        print("왕! 왕!")
    def get_status(self):
        print("태어난 개의 숫자 :", Doggy.birth_of_dogs)
        print("현재 있는 개의 숫자 :" ,Doggy.num_of_dogs)
    def __del__(self):
        Doggy.num_of_dogs -= 1
        #print(f"죽었습니다.")

d1 = Doggy('poppy', '포메라니안')
d2 = Doggy('poppy', '포메라니안')
Doggy.get_status(d1)
d1.__del__()
del d1
Doggy.get_status(d1)
d1.bark()
d2.bark()

#왜 del을 써도 인스턴스가 살아있을까