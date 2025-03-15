import os
import math

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
    minValue = 1
    maxValue = int(10e5)
    inputs = {
      "requestCount": 0,
      "userInput": []
    }

    def inputHandler(value):
      try:
        return int(value)
      except Exception:
        _print("Не удалось распознать целое число. Попробуйте снова.")
        os.system('pause')
        return False
    # end def
    
    def inputRequestHandler(currentTry):
      global inputs, minValue, maxValue
      
      _print(f"Текущий запрос: {currentTry}/{inputs["requestCount"]}\n\rВведите число от {minValue} до {maxValue}:")
      
      value = inputHandler(input())
      
      if value is False:
        return inputRequestHandler(currentTry)
      elif minValue > value or maxValue < value:
        _print(f"Вводимое число должно быть больше или равно {minValue} и меньше или равно {maxValue}. Попробуйте снова.")
        os.system('pause')
        return inputRequestHandler(currentTry)
      
      inputs["userInput"].append(value)
    # end def
    
    def handler(text):
      _print(text)
      
      userInput = inputHandler(input())
      
      match(userInput):
        case False:
          return handler(text)
        case _:
          if userInput < 1:
            _print("Введите положительное, не нулевое кол-во запросов чисел. Попробуйте снова.")
            os.system('pause')
            return handler(text)

          inputs["requestCount"] = userInput

          for i in range(inputs["requestCount"]):
            inputRequestHandler(i + 1)
          # end for
    # end def
    
    def result():
      global inputs
      
      _print("Результат:")
      print(*inputs["userInput"][::-1])
    # end def
    
    handler("Введите кол-во запросов чисел:")
    result()
    
#task №2
  case "2":
    minValue = 1
    maxValueByRequest = [100000, int(10e9)]
    inputs = {
      "userInput": []
    }
    
    msgList = {
      "currentRequest": "Текущий запрос: %d/%d",
      "request": [
          "Введите целое число от %d до %d",
          "Введите ряд целых чисел от %d до %d разделенные пробелом"
        ],
      "err": {
        "noneVal": "Не удалось распознать целое число.",
        "currTry": "Ошибка в запросе %d.",
        "invData": "Переданные данные: %s",
        "tryAgain": "Попробуйте снова.",
        "rangeVal": "Вводимое число должно быть больше или равно %d и меньше или равно %d.",
        "fatal": "Возникли непредвиденные последствия."
      }
    }

    def inputHandler(value):
      try:
        return int(value)
      except Exception:
        return None
    # end def
    
    def inputRequestHandler():
      global inputs, minValue, maxValueByRequest
      
      reqCount = len(inputs["userInput"])
      reqHumCount = reqCount + 1
      reqTotal = len(msgList["request"])
      
      _print(msgList["currentRequest"] % (reqHumCount, reqTotal))
      print(msgList["request"][reqCount] % (minValue, maxValueByRequest[reqCount]))
      
      match reqCount:
        case 0:
          value = inputHandler(input())
          
          if value is None:
            cls()
            print(*[
                msgList["err"]["currTry"] % reqHumCount,
                msgList["err"]["noneVal"],
                msgList["err"]["tryAgain"]
              ])
            os.system('pause')
          elif minValue > value or maxValueByRequest[reqCount] < value:
            cls()
            print(*[
                msgList["err"]["currTry"] % reqHumCount,
                msgList["err"]["rangeVal"] % (minValue, maxValueByRequest[reqCount]),
                msgList["err"]["tryAgain"]
              ])
            os.system('pause')
          else:
            inputs["userInput"].append(value)
        case 1:
          tmpValue = input()
          
          try:
            value = list(map(lambda i: inputHandler(i), tmpValue.split(" ")))
          except Exception:
            cls()
            print(*[
                msgList["err"]["currTry"] % reqHumCount,
                msgList["err"]["fatal"],
                msgList["err"]["tryAgain"]
              ])
            os.system('pause')
            
          if any(map(lambda i: i is None, value)):
            cls()
            print(*[
                msgList["err"]["currTry"] % reqHumCount,
                msgList["err"]["noneVal"],
                msgList["err"]["invData"] % tmpValue,
                msgList["err"]["tryAgain"]
              ], sep = "\n\r")
            os.system('pause')
          elif not all(map(lambda i: minValue <= i and maxValueByRequest[reqCount] >= i, value)):
            cls()
            print(*[
                msgList["err"]["currTry"] % reqHumCount,
                msgList["err"]["rangeVal"] % (minValue, maxValueByRequest[reqCount]),
                msgList["err"]["tryAgain"]
              ], sep = "\n\r")
            os.system('pause')
          else:
            inputs["userInput"].extend(value)
            reqCount += 1
      #end match
      
      if reqCount < reqTotal:
        return inputRequestHandler()
      else:
        return result()
    # end def
    
    def result():
      global inputs
      
      inputs["userInput"].insert(0, inputs["userInput"].pop(-1))
      
      _print("Результат:")
      print(*inputs["userInput"], sep = ", ")
    # end def
    
    inputRequestHandler()

#task №3
  case "3":
    m = int(input())
    n = int(input())
    weight = 0
    for i in range(n):
        weight += int(input())
    print(math.ceil(weight/m))

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 3.")