# task 1

# class Car:
#     odometer=0
#     fuel=70

#     def init(self, make, model, year, odometer, fuel):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel

#     def __add_distance(self, km):
#         self.odometer = km

#     def __subtract_fuel(self, fuel):
#         self.fuel -= fuel
#     def drive(self, km):
#         fuels = km / 10
#         if fuels <= self.fuel:
#             self.__add_distance(km)
#             print('Let’s drive!')
#         elif self.fuel == 0:
#             self.__subtract_fuel(fuels)
#             print('Need more fuel, please, fill more!')

# car = Car()
# car.drive(250)
# print(car.fuel)


# task 2

# class Mobilephone:

#     __imei = 'nokia'
#     __charge = 100

#     if __charge == 0:
#         raise Exception ("Телефон разряжен")

#     def music(self):
#         if self.__charge >= 10:
#             self.__charge -=5
#             print('You listen to music')
#         elif self.__charge <=10:
#             print("You can't listen to music")

#     def video(self):
#         if self.__charge>= 10:
#             self.__charge -=7
#             print('You watch the video')
#         elif self.__charge <= 10:
#             print("You can't watch videos")
        
#     def battery_charging(self):
#         self.__charge = 100

#     def get_info(self):
#         print(self.__charge)


# mobi = Mobilephone()
# mobi.get_info()
# mobi.music()
# mobi.get_info()
# mobi.video()
# mobi.get_info()
# mobi.battery_charging()



# task3














