import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')
# end def

def _print(text):
  cls()
  print(text)
# end def

_print("Выберите задание от 1 до 3:")
choosen = input()

match choosen:
#task №1
  case "1":
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    print(len(s))
    
#task №2
  case "2":
    s1 = set(input().split())
    s2 = set(input().split())
    print(len(s1.intersection(s2)))

#task №3
  case "3":
    s = set()
    n = input().split()
    for i in n:
      if i in s:
        print(i, 'YES')
      else:
        print(i, 'NO')
        s.add(i)

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 3.")