# PRACTICE PROBLEM
# Topic: Constructor + Inheritance + super()
#
# 1. Create a parent class named Person.
#
# 2. Create a constructor __init__() with:
#       name
#       age
#
# 3. Store them as instance variables.
#
# 4. Create a method display_person().
#    It should display:
#       Name
#       Age
#
# 5. Create a child class named Student.
#    Student should inherit Person.
#
# 6. Create a constructor in Student with:
#       name
#       age
#       department
#       year
#
# 7. Use super().__init__() to initialize:
#       name
#       age
#
# 8. Initialize department and year inside Student.
#
# 9. Create a method display_student().
#    Display:
#       Name
#       Age
#       Department
#       Year
#
# 10. Create an object:
#       s1 = Student( "Rasik", 20, "AI & DS", 2 )
#
# 11. Call display_student().
#
# Expected Output:
#
# Name       : Rasik
# Age        : 20
# Department : AI & DS
# Year       : 2
#
# IMPORTANT:
# - Person = Parent class
# - Student = Child class
# - Use super().__init__()
# - Do not repeat self.name = name and self.age = age
#   inside Student.