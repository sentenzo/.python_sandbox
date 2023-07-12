from dice import Dice, d4, d6, d8, d10, d12


class Weapon:
    def __init__(
        self, name: str, damage_dice: Dice, crit_thrashold: int, crit_multiplier: int
    ) -> None:
        self.name = name
        self.damage_dice = damage_dice
        self.crit_thrashold = crit_thrashold
        self.crit_multiplier = crit_multiplier

    def __repr__(self) -> str:
        crit = "   20" if self.crit_thrashold == 20 else f"{self.crit_thrashold}-20"
        name = self.name
        name_len = 24
        if len(name) > name_len:
            name = name[: name_len - 3] + "..."
        name = name.ljust(name_len)
        damage_dice = str(self.damage_dice).ljust(4)
        return f"Weapon [{name} - {damage_dice} - {crit} (x{self.crit_multiplier})]"


_no_weapon = Weapon("(no weapon)", Dice(0), 20, 0)

weapons_onehanded = [
    Weapon("Dwarven Waraxe (Exotic)", d10, 20, 3),
    Weapon("Bastard Sword (Exotic)", d10, 19, 2),
    Weapon("Estoc (Exotic)", 2 * d4, 18, 2),
    Weapon("Falchion (Martial)", 2 * d4, 18, 2),
    Weapon("Falcata (Exotic)", d8, 19, 3),
    Weapon("Heavy Pick (Martial)", d6, 20, 4),
    Weapon("Scimitar (Martial)", d6, 18, 2),
    Weapon("Rapier (Martial)", d6, 18, 2),
    Weapon("Warhammer (Martial)", d8, 20, 3),
]

weapons_twohanded = [
    Weapon("Greataxe (Martial)", d12, 20, 3),
    Weapon("Earth Breaker (Martial)", 2 * d6, 20, 3),
    Weapon("Scythe (Exotic)", 2 * d4, 20, 4),
    Weapon("Elven Curve Blade (Exotic)", d10, 18, 2),
    Weapon("Greatsword (Martial)", 2 * d6, 19, 2),
]

# if __name__ == "__main__":
#     print(*weapons, sep="\n")
