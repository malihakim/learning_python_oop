class IceCream:

    #class variables
    numIC = 0
    tax_amount = 1.1 #price + 10% of price 

    def __init__(self, name, flavour, price):
        self.name = name
        self.flav = flavour
        self.price = price
        self.ad = name + ' Ice Cream for only ' + str(price) + '$'

        IceCream.numIC += 1
        
    def fullname(self):
        return '{} {}'.format(self.name, self.flav)

    def apply_tax(self):
        self.price = int(self.price * self.tax_amount)
        
ic1 = IceCream('Madagascar', 'Vanilla', 30)
ic2 = IceCream('Chunky Monkey', 'Chocolate', 25)

print(ic1.ad)
print(ic1.fullname())

print('Total number of ice creams: ' + str(IceCream.numIC))

