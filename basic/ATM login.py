attempt=0
while(attempt<3):
    pin=int(input("Enter password:"))
    if pin==1234:
        print("Login successful")
        break
    else:
        print("Incorrect pin")    
        attempt=attempt+1
if attempt==3:
    print("card blocked")
