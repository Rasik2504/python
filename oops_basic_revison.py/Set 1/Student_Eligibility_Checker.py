# QUESTION 5: STUDENT ELIGIBILITY CHECKER
#
# Create a class called Student.
#
# Requirements:
# 1. The class should have:
#    - name
#    - age
#    - cgpa
#
# 2. Use __init__() to initialize the details.
#
# 3. Create an instance method display_details()
#    that displays the student's information.
#
# 4. Create a static method called is_valid_age(age).
#
# 5. is_valid_age(age) should return:
#       True  -> if age is between 17 and 30
#       False -> otherwise
#
# 6. Create another method called
#    is_eligible_for_placement().
#
# 7. A student is eligible if:
#       age >= 18
#       AND
#       cgpa >= 7.0
#
# 8. The method should return True or False.
#
# 9. Create at least two Student objects
#    with different CGPAs.
#
# 10. Check their placement eligibility.
#
# Concepts to practice:
# - Instance methods
# - Static methods
# - @staticmethod
# - Conditional logic
# - Returning values
# - Objects

class Student:
    def __init__(self,name,age,cgpa):
        self.name=name
        self.age=age
        self.cgpa=cgpa

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("CGPA:",self.cgpa)

    @staticmethod
    def is_valid_age(age):
        if age>=17 and age<=30:
            return True
        else: 
            return False

    def placement_eligibility(self):
        if self.age>=18 and self.cgpa>=7:
            return True
        else:
            return False

S1=Student("John",19,8.9)
S1.display()
print(S1.is_valid_age(S1.age))
print(S1.placement_eligibility())
S2=Student("Alice",20,6.7)
print(S2.is_valid_age(S2.age))
print(S2.placement_eligibility())
