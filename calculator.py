#calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot divide by zero"
    return a/b
print("simple calculator")
print("1.Addition")
print("2.Subtraction")
print("3.multiplication")
print("4.division")
choice=input("Enter  your choice(1-4):")
num1=float(input("Enter first num: "))
num2=float(input("Enter second num: "))
if choice=='1':
           print("Addition:",add(num1,num2))
elif choice=='2':
    print("Subtraction:",sub(num1,num2))
elif choice=='3':
    print("multiplication:",multiply(num1,num2))
elif choice=='4':
    print("division:",divide(num1,num2))
else:
    print("invalid choice")
    
                 

                 
