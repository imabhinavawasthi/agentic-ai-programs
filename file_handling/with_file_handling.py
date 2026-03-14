# file = open("abhinav.txt", "w") # open the file in write mode
with open("abhinav.txt", "w") as file:
    file.write("Hello, this is Abhinav.\n") # write a line to the file
    file.write("I am learning Python file handling.\n") # write another line to the file
    file.write("This is the third line.\n") # write a third line to the file

print("File has been written successfully.")
