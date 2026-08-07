# PRACTICE PROBLEM: STUDENT RESULT MANAGEMENT
#
# 1. Create a class named Student.
#
# 2. Create these instance variables:
#    - roll_no
#    - name
#    - department
#    - __marks (must be private)
#
# 3. Create a constructor (__init__) to initialize all values.
#
# 4. Create a @property getter for marks.
#    - Return the private __marks.
#
# 5. Create a @marks.setter.
#    - Marks must be between 0 and 100.
#    - If valid, update the marks.
#    - Otherwise print "Invalid Marks".
#
# 6. Create a method calculate_grade().
#    - marks >= 90  -> "A"
#    - marks >= 75  -> "B"
#    - marks >= 60  -> "C"
#    - marks >= 50  -> "D"
#    - marks < 50   -> "F"
#
# 7. Create a method is_passed().
#    - Marks >= 50 -> print "Passed"
#    - Marks < 50  -> print "Failed"
#
# 8. Create a display() method.
#    - Display roll number
#    - Display name
#    - Display department
#    - Display marks
#    - Display grade
#
# 9. Create an object:
#    s1 = Student(101, "Rasik", "AI & DS", 85)
#
# 10. Test your program:
#     - Display student details
#     - Print the marks using the property
#     - Update marks using the property
#     - Check the grade
#     - Check pass/fail
#
# IMPORTANT:
# Use @property and @marks.setter.
# Do NOT create get_marks() or set_marks().