# read a file

# open the file in read mode
file = open("hello.txt", "r")

# read the contents of the file
contents = file.read()
print(contents)

file.close()

# read the file line by line
file = open("hello.txt", "r")
lines = file.readlines()
print(lines)

file.close()

file = open("hello.txt", "r")
lines = file.readline(7) # read the first 7 characters of the first line
print(lines)

file.close()
