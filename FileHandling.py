#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

#"t" - Text - Default value. Text mode

#"b" - Binary - Binary mode (e.g. images)

#to create a file
file = open("File.txt",'x')
#to read and make text
file = open("File.txt",'rt')
file.read()
#to write
file = open("File.txt",'w')
file.write("you're my gf")
#to write and append
file = open("File.txt",'a')
file.write("\nI wanna see you Oneday")
#to read
file = open("File.txt",'r')
file.read()
#to close
file.close()

#1st close then remove otherwise it will not done
import os
os.remove("File.txt")

file = open("FileF1.txt",'r')
file.read()

#read line One by One
with open ("FileF1.txt",'r') as file:
    print(file.readline())
    print(file.readline())


