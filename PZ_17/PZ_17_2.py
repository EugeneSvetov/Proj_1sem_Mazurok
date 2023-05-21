# Создайте класс "Животное", который содержит информацию о виде и возрасте 
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса 
# "Животное" и содержат информацию о породе.

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed
        
class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

dog1 = Dog("Собака", 3, "Смешная")
print("Вид:", dog1.species)
print("Возраст:", dog1.age)
print("Порода:", dog1.breed)

cat1 = Cat("Котьик", 5, "Грустнявый")
print("Вид:", cat1.species)
print("Возраст:", cat1.age)
print("Порода:", cat1.breed)
