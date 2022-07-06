"""
Given an array of positive integers representing the values of coins in possession.
Function returns the minimum amount of change (the minimum sum of money) that cannot be created.
The given coins can have any positive integers value and aren't necessarily unique (multiple coins can have the same value).

Sample input:                        |       Sample Output:
coins = [5, 7, 1, 1, 2, 3, 22]       |       20
"""

# O(nlog(n)) time | O(1) space - where n is the number of coin
def non_constructible_change(coins):
    coins.sort()
    change = 0

    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin

    return change + 1


print(non_constructible_change([5, 7, 1, 1, 2, 3, 22])) # 20