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
    isFirstInit = True
    petInfo = {"age": None, "name": None, "petType": None}
    
    inputRequest = {
      "age": {
          "text": "Введите возраст вашего питомца",
          "expectedValType": "int"
        },
      "name": {
        "text": "Введите имя вашего питомца",
        "expectedValType": "str"
      },
      "petType": {
        "text": "Введите тип вашего питомца",
        "expectedValType": "str"
      }
    }
    
    def declension(year):
      year = int(year)
      yearAbs = abs(year)
      
      if 11 <= (yearAbs % 100) <= 14:
        return "лет"
      
      remainder = yearAbs % 10
      
      if remainder == 1:
          return "год"
      elif 2 <= remainder <= 4:
          return "года"
        
      return "лет"
    # end def
    
    def checkData(data, isFirstInit):
      isFilled = True

      for k, v in data.items():
        if not v:
          isFilled = False
          print(f"Поле \"{k}\" заполнено некорректно. Попробуйте еще раз.")

      if not isFirstInit and not isFilled: os.system('pause')
      
      return isFilled
    # end def
    
    def filler(data, inputRequest):
      for k, _ in data.items():
        _print(inputRequest[k]['text'])
        
        userInput = input()
        isStr = userInput.isalpha()
        expectedType = inputRequest[k]['expectedValType']
        
        checkInt = expectedType == "int" and not isStr
        checkStr = expectedType == "str" and isStr
        
        if checkInt or checkStr: data[k] = userInput
    # end def

    def handler(petInfo, inputRequest):
      global isFirstInit
      
      if not checkData(petInfo, isFirstInit):
        isFirstInit = False
        filler(petInfo, inputRequest)
        handler(petInfo, inputRequest)
      
      _print(f"Это {petInfo['petType']} по кличке \"{petInfo['name']}\". Возраст: {petInfo['age']} {declension(petInfo['age'])}.")
    # end def

    handler(petInfo, inputRequest)
    
#task №2
  case "2":
    pass

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 2.")