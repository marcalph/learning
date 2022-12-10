class Dog:
    species= "mammal"

    def __init__(self, name , age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    spike = Dog("Spike", 1)
    ed = Dog("Ed", 1)
    print(f"spike is {spike.age} and a {spike.species}")
    print(f"ed is {ed.age} and a {ed.species}")
    ed.species = "lab rat"
    print(f"ed is {ed.age} and a {ed.species}")
 