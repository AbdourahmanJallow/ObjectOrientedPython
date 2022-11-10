from Level_2.employee import Employee


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self._annualSalary = salary

    def weeklyPay(self, hoursWorked):
        weeksPerYear = 52
        return self._annualSalary / weeksPerYear
