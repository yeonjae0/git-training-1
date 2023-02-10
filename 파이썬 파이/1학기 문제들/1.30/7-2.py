class doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, breed):
        self.breed = breed
        doggy.num_of_dogs += 1
        doggy.birth_of_dogs +=1
    
    def bark(self):
        print('왕왕')

    def dead(self):
        doggy.num_of_dogs -= 1
    
    def get_status(self):
        print(f'{doggy.birth_of_dogs}마리의 강아지가 태어났습니다.')
        print(f'{doggy.num_of_dogs}마리의 강아지가 있습니다.')

d1 = doggy('ShihTzu')
d2 = doggy('ShihTzu')

doggy.get_status(d1)
doggy.dead(d1)
doggy.get_status(d2)
doggy.bark(d1)
del d1
d1.bark()
