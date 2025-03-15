class Build:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city
        # self.get_data()

    def get_data(self):
        print('Year: ', self.year, '. City: ', self.city, sep='')

class School(Build):
    __pupils = None

    def __init__(self, year, city, pupils=200):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_data(self):
        super().get_data()
        print('Pupils:', self.pupils)

class House(Build):
    pass

class Shop(Build):
    pass


school = School(1985, 'Zolo', 105)
school.get_data()
house = House(2005, 'Odesa')
house.get_data()
shop = Shop(2020, 'Kuev')
shop.get_data()

