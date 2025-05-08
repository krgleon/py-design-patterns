# Base class for all animals; defines the common interface
class Animal:
    def speak(self) -> str:
        # This method must be implemented by all subclasses
        raise NotImplementedError('Subclasses need implement this method')

# Concrete implementation of Animal
class Dog(Animal):
    def speak(self) -> str:
        return "Guau!"  # Dog's sound

# Another concrete implementation of Animal
class Cat(Animal):
    def speak(self) -> str:
        return "Miau!"  # Cat's sound

# Factory class that manages the creation of Animal instances
class AnimalFactory:
    _registry = {}  # Internal dictionary to map animal types to classes

    @classmethod
    def register(cls, animal_type: str, animal_class: type):
        # Registers a new animal type and its corresponding class
        cls._registry[animal_type] = animal_class

    @classmethod
    def create(cls, animal_type: str) -> Animal:
        # Creates an instance of the requested animal type
        if animal_type not in cls._registry:
            raise ValueError(f"Animal '{animal_type}' not registered.")
        return cls._registry[animal_type]()  # Instantiate and return the class

# Register concrete animal classes in the factory
AnimalFactory.register("dog", Dog)
AnimalFactory.register("cat", Cat)

# Create instances using the factory
dog = AnimalFactory.create("dog")
cat = AnimalFactory.create("cat")

# Test the created instances
print(dog.speak())  # Guau!
print(cat.speak())  # Miau!
