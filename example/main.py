class Business:

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:

    def __init__(self, address, menu, time):
        self.time = time
        self.address = address
        self.menus = menu

    def __repr__(self):
        return self.address

    def available_menus(self, time: int):

        available_menu = []

        for menu in self.menus:
            print('menu.start_time', menu.start_time, type(menu.start_time))
            print('menu', menu, type(menu))
            if int(menu.start_time) <= time <= int(menu.end_time):
                available_menu.append(menu)

            return available_menu


class Menu:
    def __init__(self, name:str, items:dict, start_time:str, end_time:str):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):

        return self.name + str(start_time) + str(end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]

        return bill


if __name__ == '__main__':

    brunch_items = {'pancakes': 7.50, 'waffles':  9.00, 'burger': 11.00, 'home fries': 4.50,
                    'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

    start_time = 1000

    end_time = 1600
    brunch_menu = Menu('brunch',  brunch_items,  str(start_time), str(end_time))

    bill = brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])

    early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                        'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                        'coffee': 1.50, 'espresso': 3.00}

    early_bird_menu = Menu('early bird', early_bird_items, str(start_time), str(end_time))

    early_bird_bill = early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli(vegan)'])

    Dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
                    'pizza with quattro formaggi': 11.00,
                    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
    Dinner_menu = Menu('Dinner available', Dinner_items, str(start_time), str(end_time))

    Kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
    Kids_menu = Menu('brunch', Kids_items, str(start_time), str(end_time))

    arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

    arepas_menu = Menu('arepas available',  arepas_items,  str(start_time), str(end_time))

    menus = [brunch_menu, early_bird_menu, Dinner_menu, Kids_menu, arepas_menu]

    flagship_store = Franchise("1232 West End Road", menus, 1200)

    new_installment = Franchise("12 East Mulberry Street", menus, 2000)

    print(flagship_store)

    flagship_store.available_menus(1200)

    new_installment.available_menus(1700)

    basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

    arepas_place = Franchise("189 Fitzgerald Avenue", menus, 1200)

    print('______END_____')
