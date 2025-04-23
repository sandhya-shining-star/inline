# Handle specific errors 
def divide(a, b): 
    try: 
        result = a / b 
        return result 
    except ZeroDivisionError: 
        print("Division by zero!") 
        return None 
print(divide(10, 2))  # Outputs: 5.0 
print(divide(10, 0))  # Outputs: Division by zero! None