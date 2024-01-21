from employee import Employee, SalaryEmployee, HourlyEmployee

class Company:
    def __init__(self):
        self.employees = []
    def print_divider(self):
        print('-' * 20)
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname,i.lname)
        self.print_divider()
    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            self.print_divider()
    
def main():
    my_company = Company()
    
    employee1 = Employee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)