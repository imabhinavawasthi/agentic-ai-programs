file = open("newton.txt", "w") # open the file in append mode

file.write("This is first line.\n") # write a line to the file
file.write("This is second line.\n") # write another line to the file

file.close() # close the file

file = open("newton.txt", "a") # open the file in append mode
file.write("This is third line.\n") # write a line to the file
file.close() # close the file