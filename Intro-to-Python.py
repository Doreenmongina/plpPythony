#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

n1=float(input("insert first number:" ))#use input function and convert the input to float or int for the 1st number.
n2=float(input("insert first number:" ))#use input function and convert the input to float or int for the 2nd number.
mOperation=input("insert an operation(+,-,*,/,):" )#use input to input a  mathematical operation.

if mOperation=='+':
    result = n1 + n2
    print(f"{n1}+{n2}={result}")
elif mOperation=='-':
    result = n1 - n2
    print(f"{n1}-{n2}={result}")
elif mOperation=='/':
    result = n1 / n2
    print(f"{n1}/{n2}={result}")
elif mOperation=='*':
    result = n1 * n2
    print(f"{n1}*{n2}={result}")
else:
    print("wrong approach please check")
  