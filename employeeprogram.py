from Level_2.Manager import Manager
from Level_2.hourlyemployee import HourlyEmployee
from Level_2.salariedemployee import SalariedEmployee

staff = [
    HourlyEmployee("Jainaba Bah", 35.0),
    SalariedEmployee("Amadu Jallow", 80_000),
    Manager("Riman Dex", 108_000, 75)
]

for employee in staff:
    hoursWorked = int(input("Enter hours worked by " + employee.getName() + ": "))
    print("Weekly Pay: $%.2f" % employee.weeklyPay(hoursWorked))

