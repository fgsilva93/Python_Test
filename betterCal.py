num1 = float(input("Ehter first number: ")) 
op = input("Ehter operator: ") 
num2 = float(input("Ehter second number: ")) 

if op == "+": 
    print(num1 + num2)
elif op == "-": 
    print(num1 - num2)
elif op == "*": 
    print(num1 * num2)
elif op == "/": 
    print(num1 / num2)
else: 
    print("Invaild operatotr!")