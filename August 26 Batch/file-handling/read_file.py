file = open("abhinav.txt", "r")
print(file.read())

file.close()

file = open("abhinav.txt", "r")
print(file.readline())

file.close()

file = open("abhinav.txt", "r")
print(file.readlines())

file.close()

with open("abhinav.txt", "r") as file:
    print(file.read())