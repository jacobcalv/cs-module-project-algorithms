
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# count returns how many times a number occurs -- good for this problem
def single_number(arr):
    # Your code here
    for i in arr:
        if arr.count(i) == 1:
            return i


