class Calculator:
    def __init__(self,num1,num2,op):
        self.num1=num1
        self.num2=num2
        self.op=op
    def calculate(self):
        if self.op=='+':
            print("Addition:",self.num1+self.num2)
        elif self.op=='-':
            print("Subtraction",self.num1-self.num2)
        elif self.op=='*':
            print("Multiplication:",self.num1*self.num2)
        elif self.op=='/':
            print("Division:",self.num1/self.num2)
            
user1=Calculator(10,29,"+")
user1.calculate()
user1=Calculator(10,29,"-")
user1.calculate()
user1=Calculator(10,29,"*")
user1.calculate()
user1=Calculator(10,29,"/")
user1.calculate()
        