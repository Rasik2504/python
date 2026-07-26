name=input("Enter The Student name:")
mark1=int(input("Enter The mark1:"))
mark2=int(input("Enter The mark2:"))
mark3=int(input("Enter The mark3:"))
mark4=int(input("Enter The mark4:"))
mark5=int(input("Enter The mark5:"))
total=mark1+mark2+mark3+mark4+mark5
print("The total mark is:", total)
average=total/5
print("The average mark is:", round(average,2))
percentage=(total/500)*100
print("The percentage is:", percentage)