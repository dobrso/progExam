from re import match
from random import randint

class InvalidDateError(Exception):
    pass

def isDateCorrect(date):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$"
    if not match(pattern, date):
        raise InvalidDateError(f"Неверный формат даты: {date}. Дата должна быть дд.мм.гггг")
    return date

class Stage:
    def __init__(self, price, dateStart, dateEnd, description):
        self._price = price
        self._dateStart = isDateCorrect(dateStart)
        self._dateEnd = isDateCorrect(dateEnd)
        self._description = description
        self.__status = None

    @property
    def description(self):
        return self._description

    # Правда не знаю зачем метод next и prev, когда хватает этих трех
    def next(self):
        self._status = "запланирован"

    def prev(self):
        self._status = "запланирован"

    def start(self):
        self._status = "осуществляется"

    def stop(self):
        self._status = "выполнен"

    def reject(self):
        self._status = "забракован"

class Project(Stage):
    def __init__(self, price, dateStart, dateEnd):
        super().__init__(price, dateStart, dateEnd, "Проект")

class Foundation(Stage):
    def __init__(self, price, dateStart, dateEnd):
        super().__init__(price, dateStart, dateEnd, "Фундамент")

class Walls(Stage):
    def __init__(self, price, dateStart, dateEnd):
        super().__init__(price, dateStart, dateEnd, "Стены")

class Roof(Stage):
    def __init__(self, price, dateStart, dateEnd):
        super().__init__(price, dateStart, dateEnd, "Крыша")

class HeatingSystemSetup(Stage):
    def __init__(self, price, dateStart, dateEnd):
        super().__init__(price, dateStart, dateEnd, "Установка отопления")

class Finising(Stage):
    def __init__(self, price, dateStart, dateEnd):
        super().__init__(price, dateStart, dateEnd, "Отделка")

class Construction:
    def __init__(self):
        self.__stages = []
        self.__stage = 0

    def addStage(self, stage):
        self.__stages.append(stage)

    def run(self):
        while self.__stage < len(self.__stages):
            currentStage = self.__stages[self.__stage]

            print(f"Идет этап: {currentStage.description}")
            currentStage.start()

            # Шанс брака
            if randint(0, 100) < 10:
                print(f"Этап {currentStage.description} забракован")
                currentStage.reject()

                # Отмена стройки или возврат к предыдущему этапу
                if self.__stage == 0:
                    return "Стройка отменяется"
                else:
                    self.__stage -= 1

            # Переход к следующему этапу в результате успеха
            currentStage.stop()
            self.__stage += 1

        return "Стройка завершилась успешно"

class Test:
    def __init__(self, date):
        self.__date = isDateCorrect(date)

project = Project(30000, "12.12.2025", "31.12.2025")
foundation = Foundation(100000, "05.01.2026", "01.03.2026")
walls = Walls(200000, "01.03.2026", "01.04.2026")
roof = Roof(150000, "01.04.2026", "25.04.2026")
heatingSystemSetup = HeatingSystemSetup(400000, "25.04.2026", "01.06.2026")
finishing = Finising(100000, "01.06.2026", "01.09.2026")

count = 0
for i in range(1000):
    construction = Construction()
    construction.addStage(project)
    construction.addStage(foundation)
    construction.addStage(walls)
    construction.addStage(roof)
    construction.addStage(heatingSystemSetup)
    construction.addStage(finishing)

    if construction.run() == "Стройка завершилась успешно":
        count += 1

print(f"Количество успешных вызовов: {count}")
print(f"Статистическая оценка: {count/1000 * 100}%")

test = Test("01122024")