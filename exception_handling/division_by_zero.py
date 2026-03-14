try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a / b
    print("The result of the division is: ", c)
except ZeroDivisionError as e:
    print("Error: You cannot divide by zero.", e)
except ValueError as e:
    print("Error: Invalid input. Please enter numeric values.", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally: # This block will always execute, regardless of whether an exception occurred or not.
    print("Close database connection.")
    print("Execution completed.")