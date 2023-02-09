class SuperHero:

    people = 'people'




    def __init__(self, name, nickname, superpower, health_points, catchphrase):

        self.name = name

        self.nickname = nickname

        self.superpower = superpower

        self.health_points = health_points

        self.catchphrase = catchphrase




    def display_name(self):

        print(f"Hero's name: {self.name}")




    def multiply_health(self):

        self.health_points *= 2




    def __str__(self):

        return f"Nickname: {self.nickname}\nSuperpower: {self.superpower}\nHealth points: {self.health_points}"




    def __len__(self):

        return len(self.catchphrase)




hero = SuperHero("Bruce", "Betman", "hight power", 100,

                 "Завтрашние заботы пускай останутся завтрашнему мне")

hero.display_name()

hero.multiply_health()

print(hero)

print("Length of catchphrase:", len(hero))


class AirHero(SuperHero):

    people = 'people'




    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):

        super().__init__(name, nickname, superpower, health_points, catchphrase)

        self.damage = damage

        self.fly = fly

    def health_2(self):

        self.fly = True

        self.health_points **= 2

        print(f"Updated health points: {self.health_points}")




    def method_fly(self):

        print(f'Fly in the {self.fly}_phrase')




class CosmicHero(SuperHero):

    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):

        super().__init__(name, nickname, superpower, health_points, catchphrase)

        self.damage = damage

        self.fly = fly







    def health_2(self):

        self.fly = True

        self.health_points **= 2

        print(f"Updated health points: {self.health_points}")




    def method_fly(self):

        print(f'Fly in the {self.fly}_phrase')







airHero = AirHero('Tatsumaki', 'Tornado', 'Esper', 200, 'Know your place, B-Class!', 100)

print(airHero)

airHero.health_2()

airHero.method_fly()

print()




cosmicHero = CosmicHero('King', 'Kingu', 'Strong Heartbeats', 80, 'Im the strongest man on earth. The S-Class Rank 7 /'

                                                                  'hero, King. Do you know that!?!', 150)

print(cosmicHero)

cosmicHero.health_2()

cosmicHero.method_fly()

print()




class Villain(CosmicHero):




    def __init__(self, name, nickname, superpower, health_points, catchphrase):

        super().__init__(name, nickname, superpower, health_points, catchphrase)

        SuperHero.people = 'monster'




    def gen_X(self):

        pass




    def crit(self, hero):

        return hero.damage ** 2







villain = Villain('Psykos', 'Saikosu', 'esper', 1000, 'You lost your chance at winning./'

                ' I was chosen as a superior entity. And I was bestowed more power than you possess.')

print(villain.crit(airHero))

