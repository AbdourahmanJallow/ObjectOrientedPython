from Level_2.employee import Employee


class HourlyEmployee(Employee):

    def __init__(self, name, wage):
        super().__init__(name)
        self._hourlyWage = wage

    def weeklyPay(self, hoursWorked):
        pay = self._hourlyWage * hoursWorked

        if hoursWorked > 40:
            # overtime pay rate is 0.5
            pay = pay + (hoursWorked - 40)*(0.5 * self._hourlyWage)

        return pay
