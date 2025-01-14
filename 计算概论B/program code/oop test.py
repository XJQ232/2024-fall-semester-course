from math import gcd
class fraction:
    def __init__(self,top,bottom):
        self.up = top
        self.down = bottom
    def __eq__(self,other):
        num1 = self.up*other.down
        num2 = self.down*other.up
        return num1 == num2
    def __str__(self):
        return str(self.up)+"/"+str(self.down)
    def show(self):
        print(str(self.up)+"/"+str(self.down))
    def __add__(self,other):
        num1 = self.up*other.down+self.down*other.up
        num2 = self.down*other.down
        num3 = gcd(num1,num2)
        return fraction(num1//num3,num2//num3)
    def __sub__(self,other):
        return self+fraction(0-other.up,other.down)
    def __mul__(other1,other2):
        num1 = other1.up*other2.up
        num2 = other1.down*other2.down
        num3 = gcd(num1,num2)
        return fraction(num1//num3,num2//num3)
temp1,temp2= map(int,input().split())
f1 = fraction(temp1,temp2)
temp1,temp2= map(int,input().split())
f2 = fraction(temp1,temp2)
print(f1*f2)
