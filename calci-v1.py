num1 = int(input("Enter First Number: "))
Operator = input("Enter Operator: ")
num2 = int(input("Enter Second Number: "))  

if Operator == "+":
    print (f"{num1} + {num2} = {num1 + num2}")
elif Operator == "-":
    print (f"{num1} - {num2} = {num1 - num2}")
elif Operator == "*":
    print (f"{num1} * {num2} = {num1 * num2}")
elif Operator == "/":
    print (f"{num1} / {num2} = {num1 / num2}")  
else:
    print ("Invalid Operator")
    