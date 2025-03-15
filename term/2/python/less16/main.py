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
    class Kassa:
      def __init__(self, money=0):
        self.money = money
      
      def top_up(self, x):
        self.money += x
      
      def count_1000(self):
        return self.money // 1000
      
      def take_away(self, x):
        if x > self.money:
          raise ValueError("Not enough money in the cash register.")
        self.money -= x
        
    k = Kassa()
    k.top_up(5000)
    print(k.count_1000())

    k.take_away(3000)
    print(k.money)
    
#task №2
  case "2":
    class Turtle:
      def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
      def go_up(self):
        self.y += self.s

      def go_down(self):
        self.y -= self.s

      def go_left(self):
        self.x -= self.s

      def go_right(self):
        self.x += self.s

      def evolve(self):
        self.s += 1

      def degrade(self):
        if self.s <= 0:
          print('s = 0')
          return
        self.s -= 1

      def count_moves(self, x2, y2):
        return self.x -x2, self.y - y2

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 2.")