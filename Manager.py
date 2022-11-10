from Level_2.salariedemployee import SalariedEmployee


class Manager(SalariedEmployee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self._weeklyBonus = bonus

    def weeklyPay(self, hoursWorked):
        return super().weeklyPay(hoursWorked) + self._weeklyBonus
