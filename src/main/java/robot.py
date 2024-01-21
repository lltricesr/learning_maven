# Relationships between classes
# Has-a: This Class has-a dependent class
class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def calculate_paycheck(self):
        return self.salary/52

class Company():
    def __init__(self):
        self.employees = []
    def print_divider(self):
        print('-' * 20)
    def add_employee(self,new_employee):
        self.employee.append(new_employee)
    def display_employees(self):
        print('Company employees are:')
        for i in self.employees:
            print(f.name, l.name)
            self.print_divider()
    def pay_employees(self):
        print('Paying employees:')
        for i in self.employees:
            print(f'Employee: {}, {}',i.fname,i.lname)
            print(f'Amount: ${i.calculate_paycheck:,.2f}')
            self.print_divider()

def main():
    my_company = Company()
    employee1 = Employee('Sarah','Hess',20000')
    my_company.add_employee(employee1)
    employee2 = Employee('Michael','Smith', 30000)
    my_company.add_employee(employee2)
    
    my_company.display_employees()
    my_company.pay_employees()

main()