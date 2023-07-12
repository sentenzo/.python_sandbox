from dice import roll_d20, D20Result
from weapon import Weapon
from dataclasses import dataclass


@dataclass(order=True)
class Hit:
    d20_attack_roll: D20Result
    d20_crit_roll: D20Result
    crit_multi: int
    atack_modifier: int
    damage_value: int

    def calc_crit_damage(self):
        return self.damage_value * self.crit_multi

    def is_successful_hit(self, defance_value: int) -> bool:
        if self.d20_attack_roll == D20Result.AUTO_FAILURE:
            return False
        if self.d20_attack_roll == D20Result.AUTO_SUCCESS:
            return True
        attack_value = self.atack_modifier + self.d20_attack_roll.value
        return attack_value >= defance_value

    def is_crit(self, defance_value: int) -> bool:
        if self.d20_crit_roll == D20Result.AUTO_FAILURE:
            return False
        if self.d20_crit_roll == D20Result.AUTO_SUCCESS:
            return True
        if not self.is_successful_hit(defance_value):
            return False
        crit_attack_value = self.atack_modifier + self.d20_crit_roll.value
        return crit_attack_value >= defance_value


class Creature:
    def __init__(
        self,
        atack_modifier: int,
        damage_modifier: int,
        defence_modifier: int,
        damage_absorption: int = 0,
        crit_immunity: bool = False,
    ) -> None:
        self.atack_modifier = atack_modifier
        self.damage_modifier = damage_modifier
        self.defence_modifier = defence_modifier
        self.damage_absorption = damage_absorption
        self.crit_immunity = crit_immunity
        self.weapon: Weapon | None = None

        self.damage_taken = 0

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def make_hit(self) -> Hit:
        if self.weapon is None:
            raise ValueError("Unable to make a hit without any weapon equipped.")
        d20_attack_roll = roll_d20()
        d20_crit_roll = D20Result.AUTO_FAILURE
        if d20_attack_roll.value >= self.weapon.crit_thrashold:
            d20_crit_roll = roll_d20()
        damage_value = self.weapon.damage_dice.roll() + self.damage_modifier
        return Hit(
            d20_attack_roll,
            d20_crit_roll,
            self.weapon.crit_multiplier,
            self.atack_modifier,
            damage_value,
        )

    def take_hit(self, hit: Hit):
        defence_value = self.defence_modifier + roll_d20().value
        damage = 0
        if not self.crit_immunity and hit.is_crit(defence_value):
            damage = hit.calc_crit_damage()
        elif hit.is_successful_hit(defence_value):
            damage = hit.damage_value
        damage -= self.damage_absorption
        damage = max(0, damage)
        self.damage_taken += damage


dummies = {
    "easy": Creature(0, 0, 10),
    "medium": Creature(0, 0, 20, 5),
    "hard": Creature(0, 0, 40, 10),
    # "boss": Creature(0, 0, 65, 15),
    "easy_crit_immune": Creature(0, 0, 10, 0, True),
    "medium_crit_immune": Creature(0, 0, 20, 5, True),
    "hard_crit_immune": Creature(0, 0, 40, 10, True),
    # "boss_crit_immune": Creature(0, 0, 65, 15, True),
}

heroes = {
    "worrior": Creature(20, 4, 0),
    "rogue": Creature(25, 0, 0),
    "goon": Creature(15, 8, 0),
    # "champion": Creature(25, 8, 0),
    # "superman": Creature(40, 10, 0),
}
