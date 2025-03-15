import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')
# end def

def _print(text):
  cls()
  print(text)
# end def

_print("Выберите задание от 1 до 2:")
choosen = input()

match choosen:
#task №1
  case "1":
    class Transport:
      def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    class Bus(Transport):
      def __init__(self, name, max_speed, mileage, passengers):
        super().__init__(name, max_speed, mileage)
        self.passengers = passengers
          
      def __str__(self):
        return "Марка: "+self.name+" Макс. скорость: "+str(self.max_speed)+" Пробег: "+str(self.mileage)+" Вместимость: "+str(self.passengers)

    bus=Bus("Renault Logan", 180, 12,10)
    print(bus)
    
#task №2
  case "2":
    class Transport:
      def __init__(self, name, max_speed, mileage):
          self.name = name
          self.max_speed = max_speed
          self.mileage = mileage
          
      def seating_capacity(self, capacity):
          return f'Вместимость одного автобуса {self.name}  {capacity} пассажиров'
 
    class Autobus(Transport):
      def __init__(self, name, max_speed, mileage, seating_capacity=50):
          super().__init__(name, max_speed, mileage)
  
      def seating_capacity(self, capacity=50):
          return f'Вместимость одного автобуса {self.name}: {capacity} пассажиров'
    
    a = Autobus('Renault', 10, 10)
    print(a.seating_capacity(15))

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 2.")