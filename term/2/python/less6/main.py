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
    numbers = {
      'request': None,
      'input': []
    }
    
    """
    def inputHandler(value):
      value = value.strip()
      
      try:
        value = int(value)
        
        if not numbers['request'] and 0 > value:
          _print("Введенное значение не должно быть отрицательным. Попробуйте снова.")
        else:
          return value
      except Exception:
        _print("Не удалось распознать натуральное число. Попробуйте снова.")  
        
      os.system('pause')
      return None
    # end def
    """
    def inputValidator(value):
      try:
        return True, int(value)
      except Exception:
        return False, None
    # end def

    """
    def handler(text):
      _print(text)
      
      userInput = inputHandler(input())
      
      match(userInput):
        case None:
          return handler(text)
        case _:
          if not numbers['request']:
            numbers['request'] = userInput
          else:
            numbers['input'].append(userInput)
    # end def
    """
    def handler(text):
      _print(text)
      
      userInput = input().strip()
      isVerified, userInput = inputValidator(userInput)
      
      match isVerified:
        case True if not numbers['request']:
          numbers['request'] = abs(userInput)
        case True:
          numbers['input'].append(userInput)
        case False:
          _print("Введены некорректные данные. Попробуйте снова.")
          os.system('pause')
          handler(text)
      # end match
    # end def
    
    handler("Введите кол-во запросов числа которое нужно сделать:")
    
    while(numbers['request'] > len(numbers['input'])):
      handler(f"Введите любое число({len(numbers['input']) + 1}/{numbers['request']}):")
    
    _print(f"Вы ввели {numbers['input'].count(0)} нулевых значений.")
    
#task №2
  case "2":
    numbers = {
      'request': None,
      'input': []
    }
    
    def inputHandler(value):
      value = value.strip()
      
      try:
        value = int(value)
        
        if not numbers['request'] and 0 > value:
          _print("Введенное значение не должно быть отрицательным. Попробуйте снова.")
        else:
          return value
      except Exception:
        _print("Не удалось распознать натуральное число. Попробуйте снова.")
        
      os.system('pause')
      return None
    # end def

    def handler(text):
      _print(text)
      
      userInput = inputHandler(input())
      
      match(userInput):
        case None:
          return handler(text)
        case _:
          if not numbers['request']:
            numbers['request'] = userInput
          else:
            numbers['input'].append(userInput)
    # end def
    
    handler("Введите кол-во запросов числа которое нужно сделать:")
    
    while(numbers['request'] > len(numbers['input'])):
      handler(f"Введите любое число({len(numbers['input']) + 1}/{numbers['request']}):")
    
    _print(f"Вы ввели {numbers['input'].count(0)} нулевых значений.")

#task №3
  case "3":
    inputs = []
    
    def inputHandler(value):
      try:
        return int(value)
      except Exception:
        _print("Не удалось распознать целое число. Попробуйте снова.")
        os.system('pause')
        return False
    # end def
    
    def handler(text):
      _print(text)
      
      userInput = inputHandler(input())
      
      match(userInput):
        case False:
          return handler(text)
        case _:
          if 0 == len(inputs) or inputs[0] <= userInput:
            inputs.append(userInput)
          else:
            _print("Число 'B' должно быть больше числа 'A'. Попробуйте снова.")
            os.system('pause')
            return handler(text)
    # end def
    
    def result():
      cls()
      
      for i in range(inputs[0], inputs[1] + 1):
        separator = " " if inputs[1] > i else ""
        print(i, end = separator) if i % 2 == 0 else ""
    # end def
    
    handler("Вводятся целое число 'A':")
    handler("Вводятся целое число 'B':")
    result()

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 3.")