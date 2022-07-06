"""
Function that takes in a non-empty array of arbitrary intervals, merges any overlapping intevals and returns the new
intervals in no particular order. Each interval is an array of two integers, with interval[0] as the start of
the interval and interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. For example, [1,5] and [6,7] aren't
overlapping; however, [1, 6] and [6, 7] are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of that interval.


        Sample Input                                    |           Sample Output
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]   |    [[1, 2], [3, 8], [9, 10]]
                                                        |   // Merge the intervals [3, 5], [4, 7] and [6, 8].
                                                        |   // The intervals could be ordered differently.
"""

# O(nlog(n)) time | O(n) space - where n is the length of the output array
def merge_overlapping_intervals(intervals: []) -> []:
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in sorted_intervals:
        _, current_interval_end = current_interval
        next_interval_start, next_interval_end = next_interval

        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals


print(merge_overlapping_intervals(intervals=[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))    # [[1, 2], [3, 8], [9, 10]]