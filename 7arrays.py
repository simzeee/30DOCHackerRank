#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    reversed_array = []
    for i in range(n):
        reversed_array.append(arr[n-i-1])
    print(' '.join(str(i) for i in reversed_array))