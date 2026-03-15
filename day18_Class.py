# class Dog:
#     species = "Canine"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def bark(self):
#         print(f"{self.name} says Woof!")
        
# # Create objects
# dog1 = Dog("Buddy",3)
# dog2 = Dog("Charlie", 5)

# # Access attributes
# print(dog1.name)
# print(dog2.age)

# # Call method
# dog1.bark()
# dog2.bark()


##################################################################################

# # Class definition
# class Car:
#     # Class attribute
#     category = "Vehicle"
    
#     # Constructor (initializer method)
#     def __init__(self, brand, model):
#         # Instance arrtibures
#         self.brand = brand
#         self.model = model
        
#     # Instance method
#     def display_info(self):
#         print(f"{self.brand} {self.model} - {self.category}")
        
# # Creating objects (instance)
# car1 = Car("Toyota", "Camry")
# car2 = Car("Honda", "Accord")

# # Accessing attributes and calling method
# print(car1.brand)
# car2.display_info()


################################################################################

# class Student:

#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
        
#     def display_info(self):
#         print(f"Name:{self.name}, Age:{self.age}, Grade:{self.grade}")
        
#     def is_passing(cls, grade):
#         return grade >= 70
        
# student1 = Student("Alice", 20, 85.5)
# student2 = Student("Bob", 22, 78.2)

# student1.display_info()
# student2.display_info()

# # Update information
# student1.age = 21
# student2.grade = 80.5

# print("Updated Information:")
# student1.display_info()
# student2.display_info()

# # Use the class method is_passing to check if the grade is passing
# result_passing = student1.is_passing(student1.grade)
# print(f"{student1.name} is passing: {result_passing}")

###################################################################################################

# words = ["Hello", "World", "Python"]
# separator = " | "
# result = separator.join(words)
# print(result)

#############################################################################################


# class Book:
#     def __init__(self, name, authors, genre, isbn):
#         self.name = name
#         self.authors = authors
#         self.genre = genre
#         self.isbn = isbn
        
#     def display_info(self):
#         print(f"Book: {self.name}")
#         print(f"Authors: {', '.join(self.authors)}")
#         print(f"Genre: {self.genre}")
#         print(f"ISBN: {self.isbn}")
        
# book1 = Book("The Great Gatsby", ["F. Scott Fitxgerald"], "Fiction", "978-3-16-148410-0")
# book2 = Book("Python Crash Course", ["Eric Mattes", "Some other Author"], "Programming", "978-1-23-456789-0")

# book1.display_info()
# print("\n")
# book2.display_info()



























































































