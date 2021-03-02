# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и
# метод который принимает лист золушек и выводит какой золушки подошла туфелька

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name}'
#
#     def __repr__(self):
#         return f'{self.name} - {self.age} - {self.shoes}'
#
#
# class Cinderella(Human):
#     def __init__(self, name, age, shoes):
#         self.shoes = shoes
#         super().__init__(name, age)
#
#
# cinderellas_l = [Cinderella("Oksana", 18, 38), Cinderella("Dasha", 20, 37), Cinderella("Anna", 24, 35)]
#
#
# class Prince(Human):
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#
#     def choice(self, cinderellas):
#         for i in cinderellas:
#             if i.shoes == self.size:
#                 print(f' This is cinderella {i.name} for {self.name} ')
#
#
# user1 = Prince('Max', 23, 38)
# user1.choice(cinderellas_l)


# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return ''
#
#     def __len__(self):
#         return self.summa()
#
#     def __add__(self, other):
#         return self.area() + other.area()
#
#     def __sub__(self, other):
#         return self.area() - other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __ne__(self, other):
#         return self.area() != other.area()
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __gt__(self, other):
#         return self.area() > other.area()
#
#     def area(self):
#         return self.x * self.y
#
#     def summa(self):
#         return self.x + self.y
#
#
# one = Rectangle(5, 2)
# two = Rectangle(2, 3)
#
# area1 = one.area()
# area2 = two.area()
#
# print(one + two)
# print(one - two)
# print(one == two)
# print(one != two)
# print(one < two)
# print(one > two)
# print(len(one))
# print(len(two))
