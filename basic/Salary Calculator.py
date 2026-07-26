#salary calculator
emp_name=input("Enter name:")
basic_salary=int(input("Enter salary:"))
bonus=int(input("Enter bonus:"))
gross_salary=basic_salary+bonus
print(gross_salary)
percent=gross_salary/100
tax=int(input("Enter Tax"))
net_salary=gross_salary-(percent*tax)
print(net_salary)