class Item():
    def item(self):

            import csv

            FILENAME = "items.csv"

            in_file = open(FILENAME)
            self.items = csv.reader(in_file, delimiter = ',')

            self.names = []
            self.descriptions = []
            self.prices = []
            self.states = []

            for line in self.items:

                name = line[0]
                description = line[1]
                price = float(line[2])
                state = line[3]

                self.names.append(name)
                self.descriptions.append(description)
                self.prices.append(price)
                self.states.append(state)

            in_file.close()