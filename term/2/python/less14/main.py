import os

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
    cls()
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    
    def print_elements(lst, index=0):
      if index < len(lst):
        print(lst[index])
        print_elements(lst, index + 1)
      else:
        print("Конец списка")
      
    print_elements(my_list)

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 1.")