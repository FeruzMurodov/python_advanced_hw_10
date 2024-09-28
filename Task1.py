class Parent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = []

    def parent_info(self):
        return f"My name is {self.name}, I'm {self.age} years old."

    def add_child(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f'Child {child.name} added to {self.name}')
        else:
            print(f'Child {child.name} NOT added to {self.name}, as the difference between ages is too small.')

    def calm_down_child(self, child):
        if child in self.children:
            child.state_calm = True
            print(f'{self.name} calmed down {child.name}')
        else:
            print(f"{child.name} is not {self.name}'s child")

    def feed_child(self, child):
        if child in self.children:
            child.state_hungry = False
            print(f'{self.name} fed {child.name}')
        else:
            print(f"{child.name} is not {self.name}'s child")
    def list_children(self):
        if self.children:
            print(f'{self.name} has following children:')
            for child in self.children:
                print(f' - {child.name}, {child.age} years old')
        else:
            print(f'{self.name} has no children for now')

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state_calm = False
        self.state_hungry = True

    def get_status(self):
        calm_status = 'calm' if self.state_calm else 'not calm'
        hungry_status = 'well-fed' if not self.state_hungry else 'hungry'
        print(f'Child {self.name} is {calm_status} and {hungry_status}')

if __name__ == '__main__':
    # Создание объектов
    parent = Parent("Иван", 40)
    child1 = Child("Анна", 20)
    child2 = Child("Петя", 10)
    child3 = Child("Маша", 3)
    for child in [child1, child2, child3]:
        parent.add_child(child)
    print(parent.parent_info())
    print(parent.list_children())

    for child in parent.children:
        parent.feed_child(child)
        parent.calm_down_child(child)
        child1.get_status()
        child2.get_status()
        child3.get_status()



