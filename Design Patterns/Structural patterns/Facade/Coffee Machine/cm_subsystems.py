class CmCoffieGrinder:
    def __init__(self) -> None:
        self.grind_inside = 0

    def grind_coffee(self, ammount: int):
        if ammount > 0:
            print(f"[CmCoffieGrinder]: grind_coffee (ammount {ammount} g)")
            self.grind_inside = ammount

class CmBrewsChamber:
    def __init__(self, grinder: CmCoffieGrinder) -> None:
        self.grinder = grinder
        self.is_emplty = True

    def grab_grind(self):
        a = self.grinder.grind_inside
        if a > 0:
            print(f"[CmBrewsChamber]: grab_grind (ammount {a} g)")
            self.is_emplty = False
            self.grinder.grind_inside = 0

    def flush(self):
        if not self.is_emplty:
            print(f"[CmBrewsChamber]: flush")
            self.is_emplty = True


class CmLiquidPress:
    def __init__(self) -> None:
        self.watter_inside = 0
        self.crem_inside = 0

    def grab_liquid(self, watter: int, crem: int) -> None:
        self.watter_inside = watter
        self.crem_inside = crem
        print(
            f"[CmLiquidPress]: grab_liquid (watter {watter} g) (crem {crem} g)")

    def boil(self, temperature: int) -> None:
        print(f"[CmLiquidPress]: boil (temperature {temperature})")

    def press(self):
        print(f"[CmLiquidPress]: press")
        self.watter_inside = self.crem_inside = 0