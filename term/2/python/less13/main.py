import os
import random

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')
# end def

def _print(text):
  cls()
  print(text)
# end def

_print("Выберите задание от 1 до 1:")
choosen = input()

match choosen:
#task №1
  case "1":
    
    matrix_1 = [[random.randint(-50, 200) for _ in range(10)] for _ in range(10)]
    matrix_2 = [[random.randint(-50, 200) for _ in range(10)] for _ in range(10)]
    print('matrix_1')
    for row1 in matrix_1:
      print(*row1)
    print('matrix_2')
    for row2 in matrix_2:
      print(*row2)

    matrix_3 = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
      for j in range(10):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
    print('matrix_3')
    for row3 in matrix_3:
      print(*row3)

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 1.")