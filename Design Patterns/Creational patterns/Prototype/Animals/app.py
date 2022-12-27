from animal_prototypes import AnimalPrototypesCollection as AnimalsCollection

def main():
    some_dog = AnimalsCollection.DOG.clone()
    [print(some_dog.checkup()) for _ in range(5)]

    some_cat = AnimalsCollection.CAT.clone()
    [print(some_cat.checkup()) for _ in range(5)]
	
    some_rabbit = AnimalsCollection.RABBIT.clone()
    [print(some_rabbit.checkup()) for _ in range(5)]

if __name__ == "__main__":
    main()