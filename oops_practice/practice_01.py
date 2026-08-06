class Student:
    college="EGSPEC"
    def __init__(self,Roll_No,Name,Age,Department,Year,cgpa):
        self.Roll_No=Roll_No
        self.Name=Name
        self.Age=Age
        self.Department=Department
        self.Year=Year
        self.cgpa=cgpa
    def display(self):
        print("Roll No : ",self.Roll_No)
        print("Name : ",self.Name)
        print("Age : ",self.Age)
        print("Department : ",self.Department)
        print("Year : ",self.Year)
        print("CGPA : ",self.cgpa)
        print("College : ",self.college)
    def update_cgpa(cls,new_cgpa):
        cls.cgpa=new_cgpa
    def update_college(cls,new_college):
        cls.college=new_college
    def is_eligible_for_placement(self):
        if (self.cgpa>=7.5):
            print("Eligible")
        else:
            print("Not Eligible")
    @staticmethod
    def is_valid_age(age):
        return 17<=age<=30
student1=Student(1,"Rasik",20,"AI & DS","2nd Year",8.5)
student1.update_cgpa(7)
student1.update_college("AVC")
student1.display()
student1.is_eligible_for_placement()


    