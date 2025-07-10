"""
Ошибки:
1. Неправильный тип данных
2. Пустой ввод
3. Год рождения привышает 2025
"""


class AgeCalculator:

    def __init__(self):
        self.birth_year = self.input_year()

    def input_year(self):
        while True:
            birth_year = input('Введите год рождения: ')
            if not birth_year.strip():
                print("Пустой ввод. Попробуйте снова.")
                continue
            try:
                birth_year = int(birth_year)
                if birth_year >= 2025:
                    print("Год рождения не может быть равен или выше 2025.")
                    continue
                return birth_year
            except ValueError:
                print(f"'{birth_year}' — это не число. Попробуйте ещё раз.")

def main():
    year = AgeCalculator()
    print(f'Ваш год рождения: {year.birth_year}')

if __name__ == "__main__":
    main()