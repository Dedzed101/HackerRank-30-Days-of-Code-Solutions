# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phonebook = {}

#Transfer the input entries to the dictionary
for i in range(n):
    entry = str(input()).split(" ")
    name = entry[0]
    phone_number = int(entry[1])
    phonebook[name] = phone_number

#Read the dictionary and determine what to print
for i in range(n):
    name = input()
    if name in phonebook:
        print(name + "=" + str(phonebook[name]))
    else:
        print("Not found")