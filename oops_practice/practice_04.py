# PRACTICE PROBLEM: BANK ACCOUNT
#
# 1. Create a class named BankAccount.
#
# 2. Create these instance variables:
#    - account_no
#    - name
#    - __balance (must be private)
#
# 3. Create a constructor (__init__) to initialize them.
#
# 4. Create a @property getter for balance.
#    - It should return the private __balance.
#
# 5. Create a @balance.setter.
#    - Balance must not be negative.
#    - If valid, update the balance.
#    - If invalid, print "Invalid Balance".
#
# 6. Create a deposit(amount) method.
#    - Amount must be greater than 0.
#    - Add the amount to the balance.
#    - Otherwise print "Invalid Deposit".
#
# 7. Create a withdraw(amount) method.
#    - Amount must be greater than 0.
#    - Amount must not be greater than the balance.
#    - Otherwise print "Insufficient Balance".
#    - If valid, subtract the amount.
#
# 8. Create a display() method.
#    - Display account number, name, and balance.
#
# 9. Create an object:
#    b1 = BankAccount(101, "Rasik", 5000)
#
# 10. Test the following:
#     - Display account details
#     - Read the balance using the property
#     - Change the balance using the property
#     - Deposit money
#     - Withdraw money
#     - Display the final balance
#
# IMPORTANT:
# Use @property and @balance.setter.
# Do NOT create get_balance() or set_balance() methods.