# Simple Calculator by Ayomola Toluwanimi Henry
# GitHub: @Toluwanimiayomola
# Location: Ekiti, Nigeria
# Email: toluwanimihenry27@gmail.com

def calculator():
    print("=== Toluwanimi's Python Calculator ===")
    print("Operations: +, -, *, /, ** (power)")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /, **): ")
        num2 = float(input("Enter second number: "))
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        elif op == "**":
            result = num1 ** num2
        else:
            print("Invalid operation!")
            return
            
        print(f"\nResult: {num1} {op} {num2} = {result}")
        
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
