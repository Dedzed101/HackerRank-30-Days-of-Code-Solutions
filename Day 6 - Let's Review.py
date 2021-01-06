# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    test_string = input()
    even_string = ""
    odd_string = ""

    for j in range(len(test_string)):
        if j % 2 == 0:
            even_string += test_string[j]
        else:
            odd_string += test_string[j] 

    print(str(even_string + " " + odd_string))