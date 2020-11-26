import math

# task 1

# class Shape:
#     def area(self):
#         pass

# class Triangle(Shape):
#     base_length = 4
#     height = 3

#     def area(self):
#         return 'площадь треугольника: ' + str(0.5 * self.base_length * self.height)

# class Square(Shape):
#     side_length = 2     

#     def area(self):
#         return 'площадь квадрата: ' + str(self.side_length * 2)
    
# class Circle(Shape):
#     radius = 2

#     def area(self):
#         return 'площадь круга: ' + str(math.pi * self.radius **2)


# def get_shape_area(input_obj):
#     print(input_obj.area())


# triangle = Triangle()
# get_shape_area(triangle)
# square = Square()
# get_shape_area(square)
# circle = Circle()
# get_shape_area(circle)



# task 2

# class Person:
#     def __init__(self, name, lastname):
#         self.__name = name
#         self.__lastname = lastname

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def lastname(self):
#         return self.__lastname

#     def get_info(self):
#         print(f"Привет, меня зовут {self.__name} {self.__lastname}")

# class Employee(Person):
#     def __init__(self, name, lastname, company, position):
#         super().__init__(name, lastname)
#         self.company = company
#         self.position = position

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.lastname}, я работаю в компании {self.company} на должности {self.position}")

# class Student(Person):
#     def __init__(self, name, lastname, university, course):
#         super().__init__(name, lastname)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.lastname} я учусь в {self.university} на {self.course}")


# def human_get_info(self):
#     print(self.get_info())


# std = [
#     Person('Иван', 'Петров'),
#     Employee('Иван', 'Петров', '“ Рога и копыта ”', 'директор'),
#     Student('Иван', 'Петров', 'КГТУ', '3 курсе')
#     ]

# for person in std:
#     person.get_info()
#     print()


# task 3

# def add_objects(string, integer):
#     a = string + str(integer)
#     return a

# class MyInt(int):

#     def add(self, *args, **kwargs):
#         print('Это сложение')
#         return args[0]

    
# class MyString(str):
    
#     def add(self, *args, **kwargs):
#         print('Это конкотенация')
#         return args[0]


# intg = MyInt()
# num = intg.add(1 + 1)
# print(num)
# string = MyString()
# strg = string.add('1' '1')
# print(strg)



































