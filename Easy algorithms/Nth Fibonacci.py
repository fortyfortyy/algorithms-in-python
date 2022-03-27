"""
The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1 and the nth
number is the sum of the (n-1) and (n-2)th numbers. Function has to take an integer n and returns the nth Fubonacci
number.

Sample input:                        |       Sample Output:
n = 6                                |            5           # 0, 1, 1, 2, 3, 5

"""

# # O(2^n) time | O(n) space (the slowest algorithm)
# def get_nth_fib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return get_nth_fib(n - 1) + get_nth_fib(n - 2)

# # O(n) time | O(n) space (the average algorithm)
# def get_nth_fib(n, memorize={1: 0, 2:1}):
#     if n in memorize:
#         return memorize[n]
#
#     memorize[n] = get_nth_fib(n - 1, memorize) + get_nth_fib(n - 2, memorize)
#     return memorize[n]

# #  O(n) time | O(1) space
def get_nth_fib(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1

    return  last_two[1] if n > 1 else last_two[0]


print(get_nth_fib(6))