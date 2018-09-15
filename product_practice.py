class Product():
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    def addTax(self):
        self.price = self.price + self.price*0.1
        return self
    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "like new":
            self.status = "for sale"
            return self
        elif reason == "opened":
            self.status = "used"
            self.price = round(self.price*0.8, 2)
            return self

    def displayInfo(self):
        print self.price, self.name ,self.weight, self.brand, self.status

p1=Product(15,"apple", "1-lb", "fuji")
p1.displayInfo()
p1.sell().displayInfo()
p1.sell().addTax().displayInfo()
# p1.returnItem("defective").displayInfo()
p1.returnItem("like new").displayInfo()
p1.returnItem("opened").displayInfo()