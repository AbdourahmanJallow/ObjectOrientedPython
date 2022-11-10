class Employee:

    def __init__(self, name):
        self._name = name
        self._rate = None

    def getName(self):
        return self._name

    def setPayRate(self, rate):
        self._rate = rate

    def weeklyPay(self, hoursWorked):
        return 0


