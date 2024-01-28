class calculator():
    def add(self):
        return (f"The addition of {self.a} + {self.b} is {self.a + self.b}")
    
    def sub(self):
        return (f"The subtraction of {self.a} - {self.b} is {self.a - self.b}")

    def mul(self):
        return (f"The multiplication of {self.a} x {self.b} is {self.a * self.b}")
    
    def div(self):
        return (f"The division of {self.a} / {self.b} is {self.a / self.b}")
        

cal = calculator()

cal.a=int(input("Enter the First number: "))
cal.b=int(input("Enter the Second number: "))
print("ADDITION = 1\nSUBTRACTION = 2\nMULTIPLICATION = 3\nDIVISION = 4")
c=int(input("What you want to do: "))

if c==1:
    print(cal.add())
elif c==2:
    print(cal.sub())
elif c==3:
    print(cal.mul())
elif c==4:
    print(cal.div())