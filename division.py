def divide(a, b):
    try:
        result = a / b 
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None  