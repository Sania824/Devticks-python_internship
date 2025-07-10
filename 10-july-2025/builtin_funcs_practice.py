# Practicing built-in functions

# Challenge Exercise:
# Combine multiple built-in functions:
# Take a list of numbers from the user (comma-separated input).
# Filter out non-integers (using filter() and isinstance()).
# Square the remaining numbers (using map()).
# Print the sum of squared numbers (using sum()).

integers = []
non_int = []

def squared(x):
    squared_list = []
    for num in x:
        squared_list.append(num**2)
    return squared_list

def sum_of_sqaured(x):
    return sum(x)


def is_int(user_list):
    # user_list = input("Input 5 numbers: ").split(',') # Wrong as input will always consider each numeric input as String
    for num in user_list:
        if isinstance(num, int) == True:
            integers.append(num)
        else:
            non_int.append(num)

    squared_nums = squared(non_int)
    print(squared_nums)

    summed_nums = sum_of_sqaured(squared_nums)
    print(summed_nums)

user_list = [3,4,5.6,1.3,0,8,4]
is_int(user_list)

# is_int()