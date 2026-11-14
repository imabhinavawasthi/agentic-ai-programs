try:
    a = int(input())
    b = int(input())
    c = a/b
    print(c)
except ValueError as e:
    print("Please enter valid number", e)
except ZeroDivisionError:
    print("Can't divide by 0")
except Exception as e:
    print(e)
finally:
    print("Program Done")

# write a program to take input of 3 numbers and print their average
# handle possible errors