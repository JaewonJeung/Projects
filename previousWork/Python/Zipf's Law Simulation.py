import string
import random
import math
import datetime


def nl():
    print("\n")


def graph(wordlength_list):
    new_dic = {}
    newer_dic = {}

    for number in wordlength_list:
        new_dic[number] = wordlength_list.count(number)

    for key in sorted(new_dic.keys()):
        if key < 10:
            new_key = str(key) + "  "
        elif key < 100:
            new_key = str(key) + " "
        else:
            new_key = str(key)
        newer_dic[new_key] = new_dic[key]

    print(newer_dic)
    nl()

    # print bar graph
    for key in newer_dic:
        altered_value = math.floor((newer_dic[key]) / 2)  # divide and round down
        printer = ""
        printer += str(key)
        printer = printer + "]" + ("I" * altered_value)
        print(printer)


alphabets = list(string.ascii_uppercase)
word_numbers = int(input("How many words do you want to generate? "))
wordlength_list = []
start_time = datetime.datetime.now()

print("\nGenerating " + str(word_numbers) + " words...\n")

for word in range(word_numbers):
    printable = ""

    # word adding/terminating process
    while True:
        rand = random.randint(0, 26)
        if rand == 26:
            if len(printable) == 0:
                continue
            print (printable) #printing out the words
            wordlength_list.append(len(printable))
            break
        else:
            printable += alphabets[rand]

graph(wordlength_list)
end_time = datetime.datetime.now()
print(start_time)
print(end_time)
