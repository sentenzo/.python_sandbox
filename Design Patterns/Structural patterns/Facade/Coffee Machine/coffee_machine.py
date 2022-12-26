from cm_subsystems import *
from enum import Enum
from outer_world import OuterWorld as out

class CoffeeSize(Enum):
    i12oz = 340
    i16oz = 454
    i8oz = 227

class CoffeeType(Enum):
    BoiledWatter = 0
    Expresso = 1
    Americano = 2
    Latte = 3

class CoffeeMachine:
    def __init__(self) -> None:
        self.grinder = CmCoffieGrinder()
        self.brews_chamber = CmBrewsChamber(self.grinder)
        self.liquid_press = CmLiquidPress()

    def make(self, coffee: int, watter: int, crem: int, t: int):
        self.grinder.grind_coffee(coffee)
        self.brews_chamber.grab_grind()
        self.liquid_press.grab_liquid(watter, crem)
        self.liquid_press.boil(t)
        self.liquid_press.press()
        self.brews_chamber.flush()

class SimpleCoffeeMachine:
    def __init__(self) -> None:
        self.cm = CoffeeMachine()

    def make_BoiledWatter(self, size: CoffeeSize) -> None:
        self.cm.make(0, size, 0, 100)

    def make_Expresso(self, size: CoffeeSize) -> None:
        self.cm.make(0.1 * size, 0.5 * size, 0, 120)

    def make_Americano(self, size: CoffeeSize) -> None:
        self.cm.make(0.1 * size, 1.0 * size, 0, 110)

    def make_Latte(self, size: CoffeeSize) -> None:
        self.cm.make(0.1 * size, 0.5 * size, 0, 110)
        self.cm.make(0, 0, 0.5 * size, 100)

    def make(self, type: CoffeeType, size: CoffeeSize) -> None:
        (
            self.make_BoiledWatter,
            self.make_Expresso,
            self.make_Americano,
            self.make_Latte,
        )[type.value](size.value)
        out.do(f"{type} {size}")
        out.do("...")