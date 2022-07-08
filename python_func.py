#function finding the max number out of the list
from turtle import right


def max_num(num):
    return max(num)
print(max_num([2, 51, 20]))

#function to multiply each given number within the list and outputting the result
def mult_list(num):
    results = 1
    for i in num:
        results *= i
    return results
print(mult_list([8, 6, 31]))

#function to reverse a given string
def rev_string(str):
    return str[::-1]
print(rev_string('Software Development'))

#checking to see if 1st number parameter falls within 2nd and 3rd number
def num_within(n, num2, num3):
    if n in range(num2, num3):
        return True
    else:
        return False
print(num_within(15, 11, 20))

def pascal(n):
    top_row = [1]
    y = [0]
    for i in range(n):
        print(top_row)
        top_row = [ left + right for left, right in zip(top_row+y, y+top_row)]
    return n >= 1
print(pascal(3))

# I had no idea how to do pascal function so i looked up online. The only part I don't clearly understand is line 35-36