import os
import re

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
    def inputValidator(value):
      try:
        if 2 > len(value) or value.index(" "): # .index() should be faster than .count()
          return False
      except Exception:
        return True
    # end def

    def handler(text):
      _print(text)
      
      userInput = input().strip()
      
      if inputValidator(userInput):        
        if (userInput == userInput[::-1]):
          return _print('yes')
          
        _print('no')
      else:
        _print("Строка должна быть одним словом не разделенная пробелами и иметь не менее 2-ух символов. Попробуйте снова.")
        
        os.system('pause')
        
        return handler(text)
    # end def
    
    handler("Введите строку чтобы узнать является ли она палиндромом:")
    
#task №2
  case "2":
    def inputValidator(value):
      return 1000 >= len(value)
    # end def

    def handler(text):
      _print(text)
      
      userInput = input().strip()
      userInputLen = len(userInput)
      
      if inputValidator(userInput):
        userInput = re.sub(r"(\s{2,})", " ", userInput)
        
        _print(f"Результат:")
        print(f"{userInputLen} сим. -> {len(userInput)} сим.")
        print(userInput)
      else:
        _print("Количество символов в строке превышает допустимое значение. Попробуйте снова.")
        print(f"Кол-во символов в переданной строке: {userInputLen}")
        
        os.system('pause')
        
        return handler(text)
    # end def
    
    handler("Введите строку не более 1000 символов и имеющую в себе лишние пробелы(более 2-ух подряд):")

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 2.")