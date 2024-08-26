'''
Q3: Using the python Lambda function create a fibonacci series from 1 to 50 elements?
'''

'''
Input = 1 to 50 elements
logic = lambda and reduce function with fubctools module
Output = print(fibonacci series from 1 to 50 elements)
'''


# Way to use the reduce() function from the functools module to reduce data
from functools import reduce

# lamdba and reduce function to get fibonacci_series
fibonacci_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])

# Print fibonacci series from 1 to 50 elements                                
print(fibonacci_series(50))    