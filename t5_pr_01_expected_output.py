'''
Q1: what is expected output of the following Python code.

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))
'''

'''
Input = data = [10, 501, 22, 37, 100, 999, 87, 351]
logic = lambda function with filter function
Output = [10, 501, 22, 37, 100, 999, 87, 351]
'''

# Given list
data = [10, 501, 22, 37, 100, 999, 87, 351]

# Lambda and Filter function
result = filter(lambda x: x > 4, data)

#Print the result as list
print(list(result))

'''
Output = [10, 501, 22, 37, 100, 999, 87, 351]
'''