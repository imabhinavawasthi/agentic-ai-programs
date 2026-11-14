# create a file
# file = open("hello.txt", "x")

# read a file
file = open("hello.txt", "r")
print(file.read()) # whole text

file = open("hello.txt", "r")
print(file.readline()) # first line

file = open("hello.txt", "r")
print(file.readlines()) # lines
file.close()

with open("hello.txt", "r") as file:
    print(file.readlines())

with open("abhinav.txt", "w") as file:
    file.write("hello abhinav\nhii\n")

with open("abhinav.txt", "a") as file:
    file.write("how are you?")