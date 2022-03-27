"""
Given a non-empty array of positive integers representing the amounts of time that specific queries take to execute.
Only one query can be executed at a time, but the queries can be executed in any order.

A query's writing time is defined as the amount of time that it must wait before its execution starts.
In other words, if a query is executed second, then its waiting time is the duration of the first query;
if a query is executed thirtd, then its waiting time is the sum of the durations of the first two queries.

Function returns the minimum amount of total waiting time for all of the queries. For example, the given queries of
durations [1, 4, 5], then the total waiting time if the queries were executed in the order of [5, 1, 4] would be
(0) + (5) + (5 + 1) = 11. The first query of duration 5 would be executed, and the last query would have to wait the
duraiton of the first two queries before being executed.

Sample Input:               |         Sample Output:
queries = [3, 2, 1, 2, 6]   |            17

"""

# O(nlog(n)) time | O(1) space - where n is the number of queries
def minimum_waiting_time(queries):
    queries.sort()

    total_waiting_time = 0
    for idx, query in enumerate(queries):
        len_queries = len(queries) - (idx + 1)
        total_waiting_time += len_queries * query

    return total_waiting_time


queries = [3, 2, 1, 2, 6]
print(minimum_waiting_time(queries))