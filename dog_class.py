class Dog:
    def __init__(self,name,bread):
        self.name=name
        self.bread=bread 
    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.bread}.")


my_dog = Dog("Buddy", "Golden Retriever")

my_dog.bark()