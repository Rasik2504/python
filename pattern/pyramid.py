<<<<<<< HEAD
n=int(input("Enter a number:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i):
        print("*",end="")
    print("*")
=======
n=int(input("Enter the number : "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
>>>>>>> 209092af4138e6eb2673f5792822f1e61e3c5666
    