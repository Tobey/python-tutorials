class business:


    def __init__(self, name, franchises ):
        self.name = name
        self.franchises = franchises



class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def availablemenus(self, time):
        self.time = time

        available_menu = []

        for menu in self.menus:
            if time >= menu.starttime and time <= menu:
                available_menu.append(menu)

            return available_menu

class Menu:
    def __init__(self,name,items,starttime,endtime):
        self.name = name
        self.items = items
        self.starttime = starttime
        self.endtime = endtime

    def __repr__(self):
            return self.name + str(self.starttime) + str(self.endtime)

    def calculatebill(self, purchaseditems):

      bill = 0
      for purchaseditem in purchaseditems:
          if purchaseditem in self.items:
             bill += self.items[purchaseditem]
          return  bill

      brunchitems = {
            'pancakes': 7.50, 'waffles':  9.00, 'burger': 11.00, 'home fries': 4.50,
            'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa':10.50,'orange juice': 3.50 }

      brunchmenu = Menu('brunch' + brunchitems + str(self.starttime) + str(self.endtime) + 1100  + 1600 )

      brunchmenu.calculatebill(['pancakes', 'home fries', 'coffee'])


      earlybirditems = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                            'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                            'coffee': 1.50, 'espresso': 3.00,}

      earlybirdmenu = Menu('early bird' + earlybirditems + str(self.starttime) + str(self.endtime) + 1500 + 1800)

      earlybirdmenu.calculatebill(['salumeria plate', 'mushroom ravioli(vegan)'])


      Dinneritems = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
            'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
      Dinnermenu = Menu('Dinner available' + Dinneritems + str(self.starttime) + str(self.endtime) + 1700  + 2100)





      Kidsitems = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
      Kidsmenu = Menu('brunch' + Kidsitems + str(self.starttime) + str(self.endtime) + 1100  + 1600 )


      arepasitems = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
      arepasmenu = Menu('arepas available' + arepasitems + str(self.starttime) + str(self.endtime) + 1000 + 2000  )


      menus = [brunchmenu, earlybirdmenu, Dinnermenu, Kidsmenu, arepasmenu ]

      flagshipstore = Franchise("1232 West End Road", menus)

      newinstallment = Franchise("12 East Mulberry Street", menus)

      print(flagshipstore)

      flagshipstore.availablemenus(1200)

      newinstallment.availablemenus(1700)

      basta = business("Basta Fazoolin' with my Heart", [flagshipstore, newinstallment ])

      arepas_place = Franchise("189 Fitzgerald Avenue", menus)






















































