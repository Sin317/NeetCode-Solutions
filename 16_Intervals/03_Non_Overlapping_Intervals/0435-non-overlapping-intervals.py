"""
Problem: LeetCode 435 - Non-overlapping Intervals
 
Key Idea:
We can solve this problem by first sorting the intervals based on their end times. Then, we iterate through the sorted intervals and count the number of overlapping intervals. If the start of the current interval is less than the end of the previous interval, it means there is an overlap, so we increment the count and skip adding the current interval to the non-overlapping set. If there is no overlap, we update the end of the previous interval to be the end of the current interval.

Time Complexity:
- The time complexity of this approach is O(n log n) due to the sorting step, where n is the number of intervals.

Space Complexity:
- The space complexity is O(1), as we use only a constant amount of extra space.
"""

"""
Intuition for greedy:
Finding the minimum number of intervals to remove is equivalent to finding the maximum number of non-overlapping intervals. This is the famous interval scheduling problem.

Let's start by considering the intervals according to their end times. Consider the two intervals with the earliest end times. Let's say the earlier end time is x and the later one is y. We have x < y.

If we can only choose to keep one interval, should we choose the one ending at x or ending at y? To avoid overlap, We should always greedily choose the interval with an earlier end time x. The intuition behind this can be summarized as follows:

We choose either x or y. Let's call our choice k.
To avoid overlap, the next interval we choose must have a start time greater than or equal to k.
We want to maximize the intervals we take (without overlap), so we want to maximize our choices for the next interval.
Because the next interval must have a start time greater than or equal to k, a larger value of k can never give us more choices than a smaller value of k.
As such, we should try to minimize k. Therefore, we should always greedily choose x, since x < y.
In general, k is equal to the end time of the most recent interval we kept.

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        non_overlapping = 1  # Count of non-overlapping intervals
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_end:
                non_overlapping += 1
                prev_end = intervals[i][1]

        return len(intervals) - non_overlapping
