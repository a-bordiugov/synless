import os
from decimal import Decimal, getcontext
import re

getcontext().prec = 20
getcontext().Emax = 999999
getcontext().Emin = -999999

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
    rectanlgeSize = []
    
    def inputHandler(value):
      value = value.strip()
      value = value.replace(",", ".")
      
      return value
    # end def
    
    def inputValidator(value):
      global rectanlgeSize
      
      try:
        hasRecLen = len(rectanlgeSize) > 0

        if isinstance(complex(value), complex):
          value = float(value)
          
          #Check list
          isNegativeNumber = value < 0
          isSquare = hasRecLen and value == rectanlgeSize[0]
          
          if isNegativeNumber or isSquare:
            _print("Правила прямоугольной формы:")
            print("- Длина и ширина не могут быть равны")
            print("- Любая из сторон не может быть равна или меньше 0 см")
            
            os.system('pause')
            
            return False
        
        return True
      except Exception:
        _print("Введены некорректные данные. Попробуйте снова.")
        
        os.system('pause')
        
        return False
    # end def
    
    def handler(text):
      global rectanlgeSize
      
      _print(text)
      
      userInput = inputHandler(input())
      
      if inputValidator(userInput):
        rectanlgeSize.append(float(userInput))
      else:
        handler(text)
    # end def
    
    handler("Введите длину прямоугольника в сантиметрах:")
    handler("Введите ширину прямоугольника в сантиметрах:")

    area = rectanlgeSize[0] * rectanlgeSize[1]
    perimeter = 2 * (rectanlgeSize[0] + rectanlgeSize[1])
    
    areaAsStr = str(Decimal(area))
    perimeterAsStr = str(Decimal(perimeter))
    
    #Format weight float numbers without round
    if area >= 1:
      areaAsStr = areaAsStr[:areaAsStr.index('.') + 3]
    else:
      areaAsStr = re.sub(r"(\d\.0+\d{2})\d+|(\d\.\d{2})", lambda m: m.group(1) or m.group(2), areaAsStr)
    
    if perimeter >= 1:
      perimeterAsStr = perimeterAsStr[:perimeterAsStr.index('.') + 3]
    else:
      perimeterAsStr = re.sub(r"(\d\.0+\d{2})\d+|(\d\.\d{2})", lambda m: m.group(1) or m.group(2), perimeterAsStr)

    _print("Характеристика прямоугольника:")
    print(f"Площадь: {areaAsStr} см")
    print(f"Периметр: {perimeterAsStr} см")
  case "2":
    pass
  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 2.")
# end match