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
          "name": "Возраст",
          "text": "Введите возраст вашего питомца",
          "expectedValType": "int"
        },
      "name": {
        "name": "Имя",
        "text": "Введите имя вашего питомца",
        "expectedValType": "str"
      },
      "petType": {
        "name": "Тип питомца",
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
    
    def checkData(data, inputRequest, isFirstInit):
      isFilled = True

      for k, v in data.items():
        if not v:
          isFilled = False
          print(f"Поле \"{inputRequest[k]['name']}\" заполнено некорректно. Попробуйте еще раз.")
      # end for

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
      
      if not checkData(petInfo, inputRequest, isFirstInit):
        isFirstInit = False
        filler(petInfo, inputRequest)
        handler(petInfo, inputRequest)
      
      _print(f"Это {petInfo['petType']} по кличке \"{petInfo['name']}\". Возраст: {petInfo['age']} {declension(petInfo['age'])}.")
    # end def

    handler(petInfo, inputRequest)
    
#task №2
  case "2":
    tests = [
      {
        "question": "Назовите первый этап эволюции человека:",
        "answers": ['дриопитек'],
        "userAnswer": ""
      },
      {
        "question": "Назовите второй этап эволюции человека:",
        "answers": ['стадия протантропа', 'протантроп', 'австралопитек'],
        "userAnswer": ""
      },
      {
        "question": "Назовите третий этап эволюции человека:",
        "answers": ['человек умелый', 'умелый'],
        "userAnswer": ""
      },
      {
        "question": "Назовите четвертый этап эволюции человека:",
        "answers": ['стадия архантропа', 'архантроп', 'стадия питекантропа', 'питекантроп', 'человек прямоходящий', 'прямоходящий'],
        "userAnswer": ""
      },
      {
        "question": "Назовите пятый этап эволюции человека:",
        "answers": ['стадия палеоантропа', 'палеоантроп', 'стадия неандертальца', 'неандерталец'],
        "userAnswer": ""
      },
      {
        "question": "Назовите шестой этап эволюции человека:",
        "answers": ['стадия неоантропа', 'неоантроп', 'кроманьонец', 'стадия человека разумного', 'человек разумный', 'разумный'],
        "userAnswer": ""
      }
    ]
    
    def isAnswerCorrect(answersList, userAnswer):
      if not len(userAnswer): return False
      
      percentToCorrect = 70
      letterToPercent = 100 / len(userAnswer)
      maxPercentOfCorrect = 0
      
      for answer in answersList:
        answerLen = len(answer)
        correctLettersPercent = 0
        
        for i in range(0, len(userAnswer)):
          UAC = userAnswer[i]
          AC = answer[i] if i < answerLen else None
          
          if UAC == AC: correctLettersPercent += letterToPercent
        # end for
        
        if correctLettersPercent > maxPercentOfCorrect:
          maxPercentOfCorrect = correctLettersPercent
      # end for

      return maxPercentOfCorrect >= percentToCorrect
    # end def
    
    def startTest(tests):
      for test in tests:
        verdict = ""
        
        cls()
        print(test['question'])
        test['userAnswer'] = input()
        
        if not isAnswerCorrect(test['answers'], test['userAnswer']):
          verdict = "неверно"
        else:
          verdict = "верно"
          
        test['userAnswer'] = f"\"{test['userAnswer']}\" ({verdict})"
      # end for
      
      result(tests)
    # end def
    
    def result(tests):
      testLen = len(tests)
      concStr = " => "
      alternatePrint = []
      
      cls()
      print("Ваши варианты ответов:")
      
      for i in range(0, testLen):
        endStr = concStr if i + 1 < testLen else ""
        str = f"{i + 1}. {tests[i]['userAnswer']}"
        alternatePrint.append(str)
        print(str, end=endStr)
        
      print("\n-----------------------------------------")
      print(*alternatePrint, sep=concStr)
    # end def
    
    startTest(tests)

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 2.")