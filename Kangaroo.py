#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    try:
        m = (x2 - x1)
        n = (v1 - v2)
        nth_jump = m/n
        nth_rem = m%n
        if nth_jump < 0:
            return 'NO'
        elif nth_rem > 0:
            return 'NO'
        else:
            return 'YES'
    except ZeroDivisionError as e:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
