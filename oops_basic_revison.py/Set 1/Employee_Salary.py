# QUESTION 2: EMPLOYEE SALARY
#
# Create a class called Employee.
#
# Requirements:
# 1. Create a class variable:
#       company = "ABC Technologies"
#
# 2. The class should have the following instance variables:
#    - name
#    - employee_id
#    - salary
#
# 3. Use __init__() to initialize the employee details.
#
# 4. Create a method display_details()
#    to display the employee information.
#
# 5. Create a method increase_salary(amount)
#    that increases the employee's salary by the given amount.
#
# 6. Create two Employee objects.
#
# 7. Display their original salary.
#
# 8. Increase the salary of one employee.
#
# 9. Display the updated salary.
#
# 10. Display the company name using both objects.
#
# Concepts to practice:
# - Class variables
# - Instance variables
# - Methods
# - Objects
# - Updating object data
class Employee:
    company="ABC Technology"
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        print("Name : ",self.name)
        print("Emp_ID : ",self.emp_id)
        print("Salary : ",self.salary)
    def increase_salary(self,amount):
        if(amount>0):
            self.salary=amount+self.salary
        else:
            print("Invalid Amount")
emp1=Employee("Alice",1,10000)
emp2=Employee("Bob",2,20000)
emp1.display()
emp2.display()
emp1.increase_salary(500)
emp1.display()