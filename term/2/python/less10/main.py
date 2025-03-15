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
    pets = {}
    pet_name = input('Enter name of your pet:')
    pets[pet_name] = {}
    age = int(input('Enter age of your pet:'))
    pets[pet_name]['type'] = input('Enter type of your pet:')
    pets[pet_name]['owner_name'] = input('Enter pet owner name:')

    # Manipulation in of age 
    if age % 10 == 1 and age != 11:
        age = str(age) + ' год'
    elif age % 10 in range(2, 5):
        age = str(age) + ' года'
    else:
        age = str(age) + ' лет'
    pets[pet_name]['age'] = age

    # Print data
    print(f'Это {pets[pet_name]["type"]} по кличке \"{pet_name}\".',
      f"Возраст питомца: {pets[pet_name]['age']}.",
      f"Имя владельца: {pets[pet_name]['owner_name']}")
    
#task №2
  case "2":
    my_dir = {}
    
    for i in range(10, -6, -1):
      my_dir[i] = i ** i
    
    print(my_dir)

  case _:
    _print("Получено некорректное значение. Запустите программу повторно и введите цифру от 1 до 2.")