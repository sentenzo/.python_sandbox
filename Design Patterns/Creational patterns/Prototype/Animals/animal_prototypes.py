from animal import Animal, AnimalType

dog = Animal("dog", AnimalType.CARNIVORE)
dog.add_actions(["sais \"Woof!\"", "is chasing squirrels"])

cat = Animal("cat", AnimalType.CARNIVORE)
cat.add_actions(["sais \"Mew!\""
	, "is watching the birds from the window",
      "is having a nap",])

rabbit = Animal("rabbit", AnimalType.HERBIVORE)
rabbit.add_actions(["is hiding in the rabbit hole"])

class AnimalPrototypesCollection:
    DOG = dog
    CAT = cat
    RABBIT = rabbit
