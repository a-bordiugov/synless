from calendar import isleap, monthrange
from datetime import date
from sys import exit as _exit


def get_digit(digit: str) -> list[str]:
    # fmt: off
    digits = {
        '0': [
            " *** ",
            "*   *",
            "*   *",
            "*   *",
            " *** "
        ],
        '1': [
            "  *  ",
            " **  ",
            "  *  ",
            "  *  ",
            " *** "
        ],
        '2': [
            " *** ",
            "*   *",
            "   * ",
            "  *  ",
            "*****"
        ],
        '3': [
            " *** ",
            "*   *",
            "  ** ",
            "*   *",
            " *** "
        ],
        '4': [
            "   * ",
            "  ** ",
            " * * ",
            "*****",
            "   * "
        ],
        '5': [
            "*****",
            "*    ",
            "**** ",
            "    *",
            "**** "
        ],
        '6': [
            " *** ",
            "*    ",
            "**** ",
            "*   *",
            " *** "
        ],
        '7': [
            "*****",
            "    *",
            "   * ",
            "  *  ",
            "  *  "
        ],
        '8': [
            " *** ",
            "*   *",
            " *** ",
            "*   *",
            " *** "
        ],
        '9': [
            " *** ",
            "*   *",
            " ****",
            "    *",
            " *** "
        ],
        '.': [
            "     ",
            "     ",
            "     ",
            " *** ",
            " *** "
        ]
    }
    # fmt: on

    return digits.get(digit, digits["."])


def validate_input(
    day: int, month: int, year: int, current_year: int, min_year: int
) -> None:
    provided_month_range = monthrange(year, month)[1]

    if not 1 <= day <= provided_month_range:
        raise ValueError(f"День должен быть от 1 до {provided_month_range}")
    if not 1 <= month <= 12:
        raise ValueError("Месяц должен быть от 1 до 12")
    if not min_year <= year <= current_year:
        raise ValueError(f"Год должен быть от {min_year} до {current_year}")


def draw_date(provided_date: date) -> None:
    lines = ["", "", "", "", ""]
    formatted_date = date.strftime(provided_date, "%d-%m-%Y")

    for char in formatted_date:
        digit = get_digit(char)
        for i in range(5):
            lines[i] += digit[i] + "  "

    for line in lines:
        print(line)


def get_day_of_week(provided_date: date) -> str:
    days = [
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье",
    ]

    return days[provided_date.weekday()]


def is_leap_year(provided_date: date) -> bool:
    return isleap(provided_date.year)


def calculate_age(provided_date: date) -> int:
    today = date.today()

    # Вычисляем базовый возраст
    age = today.year - provided_date.year

    # Проверяем, был ли день рождения в этом году
    if today.month < provided_date.month or (
        today.month == provided_date.month and today.day < provided_date.day
    ):
        age -= 1

    return age


def main() -> None:
    try:
        current_year = date.today().year
        min_year = current_year - 150

        year_input_msg = f"Введите год рождения ({min_year} - {current_year}): "
        month_input_msg = "Введите месяц рождения (1-12): "
        day_input_msg = "Введите день рождения (1-31): "

        # Ввод данных
        try:
            year = int(input(year_input_msg))
            month = int(input(month_input_msg))
            day = int(input(day_input_msg))
        except ValueError:
            print(
                "Ошибка: Введен неподдерживаемый тип данных. Необходимо использовать числа"
            )
            _exit(0)

        # Валидируем
        validate_input(day, month, year, current_year, min_year)

        # Пользовательский ввод в объекте
        provided_date = date(year, month, day)

        # Получаем день недели
        day_of_week = get_day_of_week(provided_date)
        print()
        print("= " * 40)
        print(f"День недели: {day_of_week}")

        # Проверяем високосный год
        leap = is_leap_year(provided_date)
        print(f"Год високосный: {'Да' if leap else 'Нет'}")

        # Вычисляем возраст
        age = calculate_age(provided_date)
        print(f"Возраст: {age}")

        # Рисуем дату звездочками
        print()
        print("Электронное табло:")
        print()
        draw_date(provided_date)

    except ValueError as e:
        print(f"Ошибка: Введена некорректная дата -> {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
