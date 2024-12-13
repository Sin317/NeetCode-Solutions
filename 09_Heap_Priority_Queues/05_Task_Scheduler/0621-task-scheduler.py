"""
Problem: LeetCode 621 - Task Scheduler

Key Idea:
To schedule tasks with maximum cooling time, we can use a greedy approach. We first count the frequency of each task and sort them in descending order. We then iterate through the tasks and use a cooldown counter to keep track of the remaining time until the next valid task can be scheduled. During each iteration, we schedule the task with the highest frequency that is not on cooldown. If there are no available tasks, we simply wait.

Time Complexity:
- Counting tasks: The time complexity of counting the frequency of each task is O(n), where n is the number of tasks.
- Sorting tasks: The time complexity of sorting the tasks is O(26 * log 26) = O(1), since there are at most 26 different tasks.
- Iterating through tasks: The time complexity of iterating through the tasks is O(n), where n is the number of tasks.

Space Complexity:
- The space complexity is O(26) = O(1), since there are at most 26 different tasks.
"""

import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        cooldown = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap) + 1)

            for count in temp:
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                cooldown += n + 1
            else:
                cooldown += len(temp)

        return cooldown

    # simulation. idle slots will depend on the task with max_frequency
    # so fill up the slots based on the remaining tasks
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a frequency array to keep track of the count of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # Sort the frequency array in non-decreasing order
        freq.sort()
        # Calculate the maximum frequency of any task
        max_freq = freq[25] - 1
        # Calculate the number of idle slots that will be required
        idle_slots = max_freq * n
        # Iterate over the frequency array from the second highest frequency to the lowest frequency

        for i in range(24, -1, -1):
            # Subtract the minimum of the maximum frequency and the current frequency from the idle slots
            idle_slots -= min(max_freq, freq[i])

        # If there are any idle slots left, add them to the total number of tasks
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)