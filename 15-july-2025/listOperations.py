"""The following code in the file is written to be tested"""
from operator import countOf

"""Testing String Utility Functions"""

def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for nums in numbers:
        if nums > max_num:
            max_num = nums
    return max_num

def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def calc_average(avg_nums):
    # if not avg_nums:
    #     return None
    average = sum(avg_nums)/len(avg_nums)
    return average




