class Animals:
    def __init__(self, name):
        self.name = name


class Bird(Animals):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_wing_length(self):
        return self.wingspan


class Fish(Animals):
    def __init__(self, name, max_depth: int):
        super().__init__(name)
        self.max_depth = max_depth

    def get_depth(self):
        if self.max_depth < 10:
            return 'shallow water'
        elif self.max_depth > 100:
            return 'deep water'
        else:
            return 'mid-water'


class Mammal(Animals):
    def __init__(self, name, weight: int):
        super().__init__(name)
        self.weight = weight

    def get_category(self):
        if self.weight < 1:
            return 'small'
        elif self.weight > 200:
            return 'giant'
        else:
            return 'normal'


class AnimalFactory:
    def create_animal(self, animal_type: str, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError(f'Unknown animal type: {animal_type}')



if __name__ == '__main__':
    factory = AnimalFactory()
    a1 = factory.create_animal("Bird", 'Falcon', 2)
    a2 = factory.create_animal("Fish", 'Salmon', 50)
    a3 = factory.create_animal("Mammal", 'Bear', 150)
    print(f"{a1.name}'s wing length is {a1.get_wing_length()}")
    print(f"{a2.name}'s inhabiting depth type is {a2.get_depth()}")
    print(f"{a3.name}'s weight category is {a3.get_category()}")
