'''
Q2: Write a Python code using Lambdaa function to check every element of list is an integer or string
'''

'''
Input = list of strings and inetgers
logic = lambda and filter function
Output = print(integer list and string list)
'''


# input list
my_list = [3, 8, "88", "ten", 88, "six"]

# Filter for integers
int_list = list(filter(lambda x: isinstance(x, int), my_list))
print("The list of integers =", int_list)

# Filter for strings
str_list = list(filter(lambda x: isinstance(x, str), my_list))
print("\nThe list of strings = ", str_list)