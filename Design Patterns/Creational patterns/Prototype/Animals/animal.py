from __future__ import annotations
from typing import List
from prototype import Prototype
from copy import copy
from enum import Enum, auto
from random import choice

class AnimalType(Enum):
    CARNIVORE = auto()
    HERBIVORE = auto()
    OMNIVORE = auto()

class AnimalSex(Enum):
    MALE = auto()
    FEMALE = auto()

_NAME_POOL_ = {
    AnimalSex.MALE: ["Oliver", "Jack", "Harry", "Jacob", "Charlie"
					 , "Thomas", "George", "Oscar", "James", "William"],
    AnimalSex.FEMALE: ["Amelia", "Olivia", "Isla", "Emily", "Poppy"
					   , "Ava", "Isabella", "Jessica", "Lily", "Sophie"]
}

_ACTIONS_POOL_ = {
    True: ["is sleeping"],
    AnimalType.CARNIVORE: ["is hunting for prey", "is resting in a den"],
    AnimalType.HERBIVORE: ["is grazing ", "is wandering around"],
    AnimalType.OMNIVORE: ["is searching for some food"]
}


class Animal(Prototype):
    def pick_name(self):
        self.animal_sex = choice([AnimalSex.MALE, AnimalSex.FEMALE])
        self.name = choice(_NAME_POOL_[self.animal_sex])

    def generate_actions_set(self):
        self.actions = _ACTIONS_POOL_[True] + _ACTIONS_POOL_[self.animal_type]

    def add_actions(self, actions: List[str]):
        self.actions += actions

    def __init__(self, species: str, animal_type: AnimalType) -> None:
        self.species = species
        self.animal_type = animal_type
        self.pick_name()
        self.generate_actions_set()

    def clone(self) -> Prototype:
        new_self = copy(self)
        new_self.pick_name()
        return new_self

    def __str__(self) -> str:
        s = f"{self.name} the {self.species}"  # Emily the cat
        return s

    def checkup(self) -> str:
        action = choice(self.actions)
        return f"{self} {action}"  # Emily the cat is having a nap