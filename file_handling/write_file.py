file = open("abhinav.txt", "w") # open the file in write mode

file.write("Hello, this is Abhinav.\n") # write a line to the file
file.write("I am learning Python file handling.\n") # write another line to the file
file.write("This is the third line.\n") # write a third line to the file

file.close() # close the file

file = open("abhinav.txt", "w") 
file.write("I am learning Python file handling.\n") # this will overwrite the existing content in the file
file.close() # close the file