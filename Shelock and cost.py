#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
# def get_new_array(B, max_num_index):
#     req_eq = []
#     if len(B) == 3:
#         if (B[0] - B[1]) > (B[1] - B[2]):
#             ret_eq = [B[0],1,B[2]]
#         else:
#             ret_eq = [1,B[1],1]
#     else:
#         if (max_num_index < len(B)-1) and (max_num_index > 0):
#         if max_num_index > 0:
#             ret_eq = get_new_array(B,max_num_index-1) + \
#                 get_new_array(B[max_num_index-1:max_num_index+2],max_num_index) +\
#                 get_new_array(B,max_num_index+1)

#     return ret_eq

def get_new_array(B, _index):

    if (_index > len(B)) or (_index < 0):
        return B 

    start_index = _index 
    end_index = _index + 2
    if len(B) == 3:
        start_index = 0
        end_index = start_index + 2
        


    if start_index >=0 and end_index < len(B):
        print('--1')
        req_arr = B[start_index:end_index+1]
        if (req_arr[0] - req_arr[1]) > (req_arr[1] - req_arr[2]):
            B[start_index:end_index+1] = [req_arr[0],1,req_arr[2]]
        else:
            B[start_index:end_index+1] = [1,req_arr[1],1]
    print(B, start_index, len(B))


    if start_index > 0:
        print('---2')
        B = get_new_array(B, start_index-1)
    if end_index < len(B):
        print('---3')
        B = get_new_array(B, start_index+1)
    


def cost(B):
    max_num_index = 0
    for _e in range(len(B)):
        if B[max_num_index] < B[_e]:
            max_num_index = _e
    print('init max_index', max_num_index)
    Btemp = get_new_array(B, max_num_index)
    print(Btemp)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)
    print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
