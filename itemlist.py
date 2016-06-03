from item import Item

class ItemList():
    def listing_items(self):
        for i in range(len(self.names)):
            return("{} - {} ({}) = ${:,.2f} - {}".format(i, self.names[i], self.descriptions[i], self.prices[i], self.states[i]))