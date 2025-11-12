from addition import add
from substraction import subtract
from multiplication import multipy
from division import divide

def main():
    print("Simple Calculator")
    print("-----------------")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplcation")
    print("4. Division")
    choice = input("Enter choice (1/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"The result of addition is: {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
    
    elif choice == '3':
        result = multipy(num1, num2)
        print(f"The result of multiplication is: {result}")
    
    elif choice == '4':
        result = divide(num1, num2)
        if result is not None:
            print(f"The result of division is: {result}") 
        else:    
            print(f"Division failed")    
            
    else:
        print("Invalid input. Please select 1 to 4.")


if __name__ == "__main__":
    main()