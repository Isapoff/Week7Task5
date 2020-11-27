# task 1

# class Mylist(list):
#     def __init__(self, value):
#         self.value = value
    
#     def __getitem__(self, item):
#             return self.value[item -1]

# x  = Mylist([1, 2, 3, 4, 5])
# print(x[1])


# task 2

# class Student(dict):
#     def __init__(self, name, lastname, grade, mark):
#         self.name = name
#         self.lastname = lastname
#         self.grade = grade
#         self.mark = mark

#     def overall_mark(self, value):
#         marks = 0
#         for i in value.values():
#             marks+= i
#             self.marks = marks

#     def __gt__(self, other):
#         if self.marks > other.marks:
#             print(f'средний балл {self.name} {self.marks} больше чем у {other.name} {other.marks}')
    
#     def __lt__(self, other):
#         if self.marks < other.marks:
#             print(f'средний балл {self.name} {self.marks} меньше чем у {other.name} {other.marks}')

#     def __eq__(self, other):
#         if self.marks == other.marks:
#             print(f'средний балл {self.name} {self.marks} равен {other.name} {other.marks}')

# sasha = Student('Sasha', 'Petrov', {'history': 89, 'math': 100, 'literature': 88},10)
# sasha.overall_mark(sasha.grade)
# masha = Student('Masha', 'Aksenova', {'history': 87, 'math': 100, 'literature': 88},10)
# masha.overall_mark(masha.grade)
# masha > sasha
# masha < sasha
# masha == sasha


