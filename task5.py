# task 1

# def dollarize(float):
#     dollar = ('${:,.2f}'.format(float))
#     return dollar
    
# print(dollarize(123456.78901))
# print(dollarize(-123456.7801))
# print(dollarize(1000000))


# class MoneyFmt:
#     amount = 0

#     def __init__(self, amount):
#         self.money = amount

#     def update(self, dollar):
#         self.money = dollar

#     def __repr__(self):
#         result = str(self.money)
#         print(result)
#         return result

#     def __str__(self):
#         self.result = ('${:,.2f}'.format(self.money))
#         return self.result

# cash = MoneyFmt(12345678.021)
# print(cash) 
# cash.update(100000.4567)
# print(cash) 
# cash.update(-0.3)
# print(cash) 
# repr(cash) 


# task 2

# class Bike:
#     def __init__(self, cost, make, model, year, condition, _sale_price, sold):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = None
#         self.sold = False
    
#     def price(self):
#         s = input("предложение покупателя: ")
#         if s < self.cost:
#             print(f'мин цена велосипеда {self.cost} ')
#         else:
#             print("мин прибыль", int(s) - int(self.cost))


    
#     def service(self):
#         """цена после ремонта"""
#         rp = 15
#         r =  rp + int(self.cost)
#         print(f'новая цена после ремонта {r}')
    
    
#     def sell(self, s):
#         self.sold = True
#         i = int(s) - int(self.cost)
#         print(f'прибыль с продажи {i}')

#     def get_default_bike(self):
#         # pass
#         bike = Bike('120 ', 'gt', 'agr', 2018, 'b/u', None, False)
#         bike.price()
#         bike.service()
#         bike.sell(135)
#         return bike
        
# bike = Bike.get_default_bike('')



# task 3
# import random

# class Soldier:
#     def __init__(self, number, team):
#         self.number = number
#         self.team = team
    
#     def follow_hero(self, hero):
#         self.hero = hero
#         print(f'soldier numbered {self.number} follow hero {hero.number}')

#     # def follow_hero2(self, hero):
#     #     self.hero = hero
#     #     print(f'soldier numbered {self.number} follow hero {hero.number}')


# class Hero(Soldier):
#     def __init__(self, number, team, level):
#         super().__init__(number, team)
#         self.level = level

#     def up_level(self):
#         self.level += 1
#         print(f'the hero {self.number} level up')

#     # def up_level2(self):
#     #     self.level += 1
#     #     print(f'the hero {self.number} level up')


# s1 = []
# s2 = []
# h1 = Hero(1, 1, 0)
# h2 = Hero(1, 2, 0)

# n =2
# while n < 20:

#     s = Soldier(n + 1, random.randint(1, 2))
#     n +=1
#     if s.team == 1:
#         s1.append(s)
#     elif s.team ==1:
#         s2.append(s)
    
# print(' number of soldiers of the hero', h1.number, 'is', len(s1),'\n number of soldiers of the hero', h2.number, 'is', len(s2))

# if len(s1) >= len(s2):
#     h1.up_level()
#     s = random.choice(s1)
#     s.follow_hero(h1)
# else:
#     h2.up_level()
#     s = random.choice(s2)
#     s.follow_hero(h2)



