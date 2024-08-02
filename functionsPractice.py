#A function for finding maximum of three numbers
def max_num(a, b, c):
    return max(a, b, c)

print(max_num(2,4,6))
print(max_num(10,30,15))
print(max_num(1,30,2))

#A function for multiplying all numbers in a list
def mult_list(numbers):
    if len(numbers) == 0: 
        result = 0
    else:                       
        result = 1
    for num in numbers:
        result *= num
    return result

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))

# Write a Python function called rev_string() to reverse a string.

def rev_string(s):
    return s[::-1]

print(rev_string("Hello World"))
print(rev_string("AI")) 

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num, start, end):
    return start <= num <= end

print(num_within(15, 10, 20))
print(num_within(5, 10, 20))
#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    for row in triangle:
        print(' '.join(map(str, row)).center(n * 2))

pascal(5)
