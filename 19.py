class Buildings:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Год:", self.year, "Город:", self.city)

class Schools(Buildings):
    pupils = 0

    def __init__(self, year, city, pupils):
        self.year = year
        self.city = city
        self.pupils = pupils

    def get_info(self):
        print("Год:", self.year, "Город:", self.city, "Ученики:", self.pupils)

class Houses(Buildings):
    pass

class Shops(Buildings):
    pass


school_3 = Schools(2000, 'Москва', 200)
school_3.get_info()
school_49 = Schools(2015, 'Саратов', 80)
school_49.get_info()
house = Buildings(1990, 'Москва')
shop = Buildings(2001, 'Иваново')

