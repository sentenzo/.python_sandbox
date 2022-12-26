from coffee_machine import *

def main():
    cm = SimpleCoffeeMachine()

    cm.make(CoffeeType.Americano, CoffeeSize.i12oz)
    cm.make(CoffeeType.Latte, CoffeeSize.i16oz)
    cm.make(CoffeeType.BoiledWatter, CoffeeSize.i8oz)

if __name__ == "__main__":
    main()