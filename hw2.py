class SuperHero:
    people = 'people'

    def _init_(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name

        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_info(self):
        print(f"Name: {self.name}")

    def multiplied_health(self):
        self.health_points *= 2

    def hero_info(self):
        print(f"Nickname: {self.nickname}")

        print(f"Superpower: {self.superpower}")
        print(f"Health points: {self.health_points}")

    def catchphrase_length(self):
        print(f"Catchphrase length: {len(self.catchphrase)}")


hero = SuperHero("Bruce Wayne", "Batman", "High intelligence", 100, "I whatever Gotham needs me to be")

hero.name_info()
hero.multiplied_health()
hero.hero_info()
hero.catchphrase_length()