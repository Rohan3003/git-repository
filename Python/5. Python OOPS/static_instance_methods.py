from typing import Self
from datetime import date

class Calculator:
    def __init__(self, version: float):
        self.version = version
    
    def description(self):
        print(f'Currently running Calculator on version: {self.version}')
    
    @staticmethod
    def add_numbers(*numbers : float) -> float:
        s = sum(numbers)
        print(s)
        return s

if __name__ == '__main__':
    calc1 = Calculator(1.0)
    calc2 = Calculator(2.0)
    calc1.description()
    calc2.description()
    calc1.add_numbers(1,2,3)
    Calculator.add_numbers(10,20,30) # we don't need any instance to use function add_numbers() - we can use it anywhere.

