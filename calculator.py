from addition import add
from substraction import subtract

def main():
    print("Simple Calculator")
    print("-----------------")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Enter choice (1/2): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"The result of addition is: {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of subtraction is: {result}")

    else:
        print("Invalid input. Please select 1 or 2.")


if __name__ == "__main__":
    main()