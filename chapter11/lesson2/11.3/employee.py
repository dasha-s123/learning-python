class Employee:
    """создается модель работника"""
    def __init__(self, name, surname, year_salary):
        self.name = name
        self.surname = surname
        self.year_salary = year_salary

    def give_raise(self, increase=5000):
        """Увеличивает ежегодный оклад"""
        self.year_salary += increase


new_employee_1 = Employee('Mark', "Shantin", 3000)
print(new_employee_1.year_salary)
new_employee_1.give_raise(2000)
print(new_employee_1.year_salary)