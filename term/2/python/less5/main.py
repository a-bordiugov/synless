from functools import reduce
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
    def checkList(value):
      # Пример исключительно для практики, т.к. использование match для
      # этой задачи тратит чуть больше процессорного времени из-за одной лишней проверки
      # в условиях case
      match(value):
        case value if value < 0:
          return "число не является четным" if value % 2 else "отрицательное четное число"
        
        case value if value > 0:
          return "положительное четное число" if not value % 2 else "число не является четным"
        
        case _:
          return "нулевое число"
    # end def
    
    def inputHandler(value, text):
      value = value.strip()
      
      try:
        return int(value)
      except Exception:
        _print("Не удалось распознать целое число. Попробуйте снова.")
        
        os.system('pause')
        
        return handler(text)
    # end def
    
    def handler(text):
      _print(text)
      
      value = inputHandler(input(), text)
      
      _print(f"Результат: {checkList(value)}")
    # end def
    
    handler("Введите целое число:")
    
#task №2
  case "2":
    charCount = {
      'vowels': {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
      },
      #'anyConsonants': 0
    }
    
    def result(value):      
      for key in charCount['vowels'].keys():
        charCount['vowels'][key] = value.count(key)
        value = value.replace(key, '')
      # end for
      
      vowelsList = charCount['vowels'].values()
      
      if all(vowelsList):
        vowelsCount = reduce(lambda a, b: a + b, vowelsList)
        consonantsCount = len(value)
        
        print(f"Согласных = {consonantsCount}, гласных = {vowelsCount}")
      else:
        print("False")
    # end def
    
    def inputValidator(value):
      return value.isalpha()
    # end def
    
    def handler(text):
      _print(text)
      
      value = input().strip().lower()
      
      if inputValidator(value):
        _print("Результат:")
        result(value)
      else:
        _print("Не удалось распознать строку на латинице. Попробуйте снова.")
        
        os.system('pause')
        
        return handler(text)
    # end def
    
    handler("Чтобы получить результат введите слово содержащее в себе 5 гласных и состоящее из латинского алфавита:\nНапример: \"sequoia\"")

#task №3
  case "3":
    company = {
      'name': 'НовыеТехнологии',
      'finance': {
        'minInvest': 0,
        'investors': {}
      }
    }
    
    def setMinInvest(value):
      global company
      
      company['finance']['minInvest'] = value
    # end def
    
    def setInvestor(investor, invest):
      global company
      
      company['finance']['investors'][investor] = invest
    # end def
    
    def inputValidator(value):
      errMsg = "Введены некорректные данные. Попробуйте снова."
      
      try:
        if isinstance(complex(value), complex):
          value = int(value)
          
          if value > 0:
            return True
          else:
            errMsg = "Сумма инвестиций не может быть отрицательной или нулевой. Попробуйте снова."
      except Exception:
        pass
      
      _print(errMsg)
      
      os.system('pause')
      
      return False
    # end def

    def result():
      global company
      
      # Обрабатываем информацию об инвесторах
      # Даем им ответ
      mikeFunds = company['finance']['investors']['Mike']
      ivanFunds = company['finance']['investors']['Ivan']
      minInvest = company['finance']['minInvest']
      
      if minInvest <= mikeFunds and minInvest <= ivanFunds:
        _print(2) # Оба могут вложиться
      elif minInvest >= mikeFunds and minInvest <= ivanFunds:
        _print("Ivan") # Только Иван
      elif minInvest <= mikeFunds and minInvest >= ivanFunds:
        _print("Mike") # Только Майкл
      elif minInvest <= (mikeFunds + ivanFunds):
        _print(1) # Только совместно
      else:
        _print(0) # Никто
    # end def

    def handler(text, cb):
      _print(text)
      
      userInput = input().strip()
      
      if inputValidator(userInput):
        userInput = int(userInput)
        
        # Добавляем информацию о минимальной инвестиции
        # Добавляем информацию об инвесторах
        if callable(cb):
          cb(userInput)
        elif isinstance(cb, list):
          cb[0](cb[1], userInput)
        else:
          _print("Непредвиденная ошибка. Работа программы была завершена.")
      
          os.system('pause')
          
          exit()
      else:
        return handler(text, cb)
    # end def

    handler(f"Вы фаундер стартапа \"{company['name']}\", объявите минимальную сумму($) для инверстирования:", setMinInvest)
    handler(f"Вы инвестор Майкл и хотите инвестировать в стартап \"{company['name']}\". Какую сумму($) вы хотите инвестировать?", [setInvestor, 'Mike'])
    handler(f"Вы инвестор Иван и хотите инвестировать в стартап \"{company['name']}\". Какую сумму($) вы хотите инвестировать?", [setInvestor, 'Ivan'])
    result()
  
  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 3.")