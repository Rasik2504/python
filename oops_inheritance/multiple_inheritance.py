# PRACTICE — MULTIPLE INHERITANCE
#
# 1. Create class A.
#
#    Add:
#    show()
#    Print "Class A"
#
# 2. Create class B.
#
#    Add:
#    show()
#    Print "Class B"
#
# 3. Create class C(A, B).
#
# 4. Create object:
#    c1 = C()
#
# 5. Call:
#    c1.show()
#
# 6. Print:
#    C.mro()
#
# 7. Identify which show() Python executes first.
#
# 8. Change C(A, B) to C(B, A).
#
# 9. Run again and observe the difference.
class A:
    def show(self):
        print("Class A")


class B:
    def show(self):
        print("Class B")


class C(B,A):
    pass


c1 = C()

c1.show()

print(C.mro())
