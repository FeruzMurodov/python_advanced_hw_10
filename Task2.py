from random import randint


class Human:
    def __init__(self, name):
        self.name = name
        self.fed_level = 50
        self.house = None
        self.is_alive = True
        self.money = 0
        self.food = 0
        print(f'Person {self.name} created.')

    def eat(self):
        self.fed_level += 10
        print(f'{self.name} was fed. Current fed level: {self.fed_level}')

    def work(self):
        self.fed_level -= 10
        self.money += 10
        print('Working done')

    def play(self):
        self.fed_level -= 10
        print('Played')

    def go_shop_for_foods(self):
        self.food += 10
        self.money -= 10
        print(f'Shopping done')

    def live_a_day(self):
        pass


class House:
    dwellers = []

    def add_dweller(self, person: Human):
        self.dwellers.append(person)
        person.house = self
        print(f'{person.name} is added to house.')

    def start_living(self):
        print('Life is started!')
        for i in range(1, 366):
            print(f'Day {i} started. House status: Fridge = {self.fridge}. Deposit = {self.nightstand_with_money}')
            for person in self.dwellers:
                print(f'{person.name} is alive. Fed level: {person.fed_level}')
                ran_number = randint(1, 6)
                if person.fed_level < 20:
                    print(f'{person.name} is hungry!')
                    if self.fridge > 10:
                        person.eat()
                        self.fridge -= 10
                    else:
                        print(f'No food left in the fridge!')
                        if self.nightstand_with_money < 50:
                            print(f'Money is less than enough! Have to go work!')
                            person.work()
                            person.money -= 10
                            self.nightstand_with_money += 10
                            person.go_shop_for_foods()
                            person.food -= 10
                            self.fridge += 10
                            person.eat()
                            self.fridge -= 10
                        else:
                            person.go_shop_for_foods()
                            person.food -= 10
                            self.fridge += 10
                            person.eat()
                            self.fridge -= 10
                elif ran_number == 1:
                    person.work()
                    person.money -= 10
                    self.nightstand_with_money += 10
                elif ran_number == 2:
                    if self.fridge > 10:
                        person.eat()
                        self.fridge -= 10
                    else:
                        print(f'No food left in the fridge!')
                        if self.nightstand_with_money < 50:
                            print(f'Money is less than enough! Have to go work!')
                            person.work()
                            person.money -= 10
                            self.nightstand_with_money += 10
                            person.go_shop_for_foods()
                            person.food -= 10
                            self.fridge += 10
                            person.eat()
                            self.fridge -= 10
                        else:
                            person.go_shop_for_foods()
                            person.food -= 10
                            self.fridge += 10
                            person.eat()
                            self.fridge -= 10
                else:
                    person.play()
            if person.fed_level < 0:
                print(f'{person.name} dead by hungriness!')
                self.dwellers.pop(person)
            print(f'Day {i} is end. House status: Fridge = {self.fridge}. Deposit = {self.nightstand_with_money}')
            print()
        print('Year is end!')


    def __init__(self):
        self.fridge = 50
        self.nightstand_with_money = 0
        print('House is built.')


if __name__ == '__main__':
    some_house = House()
    dweller1 = Human('Harry')
    dweller2 = Human('Ron')
    some_house.add_dweller(dweller1)
    some_house.add_dweller(dweller2)
    some_house.start_living()
