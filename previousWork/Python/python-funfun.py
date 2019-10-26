import datetime


def nl():
    print("\n")


print(datetime.datetime.now().strftime("%Y, %H, %M, %S"))

if datetime.datetime.now().strftime('%Y') == '2019':
    print("It indeed is year 2019!")

nl()
file_path = 'C:\Python 3.7\python_files\chapter_10\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# playing with individual line in the file
with open(file_path) as file_second_object:
    for line in file_second_object:
        print(line.rstrip())

# Making a list of lines from a file
with open(file_path) as file_third_object:
    lines = file_third_object.readlines()
pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()
nl()
print(pi_string)
print(len(pi_string))
nl()

filename = 'C:\Python 3.7\python_files\chapter_10\pi_million_digits.txt'
lines = ''
with open(filename) as file_fourth_object:
    lines = file_fourth_object.readlines()  # storing ind. line to a list
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:20] + "...")
print(len(pi_string))

# checking if a number is in pi
if "42" in pi_string:
    print("42 is in Pi!")

nl()

new_filename = 'C:\Python 3.7\python_files\chapter_10\in_python.txt'

# printing the contents once by reading in the entire file
with open(new_filename) as file:
    print(file.read())
nl()

# by looping over the file object
with open(new_filename) as file:
    for line in file:
        print(line.rstrip())

nl()
# by storing the lines in a list and then working with them outside the with block
lines = ''
with open(new_filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.replace('python', 'C').rstrip())
nl()
print(*lines)  # printing a list in a single line of code
nl()

str = "The"
temp_str = ""
for i in range (len(str)):
    temp_str += (str[i]*2)
print(temp_str)
