#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    reverse = []
    for i in range(n):
        reverse.append(arr[n-i-1])
        
    print(' '.join(str(i) for i in reverse))
    
    #Alternatively
    #output_string = ''
    #for i in range(len(reverse)):
    #   output_string += str(reverse[i]) + ' '
        
    #print(output_string)