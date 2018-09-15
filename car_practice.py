class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        print("price: "+ str(self.price))
        print("Speed: "+ str(self.speed))
        print("Fuel: "+ str(self.fuel))
        print("Mileage: "+ str(self.mileage))
        if self.price > 10000:
            print("Tax: 0.15% \n")
        else:
            print("Tax: 0.12% \n")
        return self

car1 = Car(2000, "35mph", "Full", "15mpg" )
car1.display_all()
car2 = Car(20000, "35mph", "Full", "15mpg" )
car2.display_all()