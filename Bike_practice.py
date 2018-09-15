class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        
    def displayInfo(self):
        print("Price: "+ str(self.price)+ ", Max speed: "+ str(self.max_speed)+ ", Total miles: "+ str(self.miles))
        return self
    def ride(self):
        self.miles += 10
        print("Riding ", self.miles)
        return self
    def reverse(self):
        self.miles -= 5
        print("Reversing ",self.miles)
        return self

bike1 = Bike("$100","50mph")
bike1.ride().ride().ride().reverse().displayInfo()