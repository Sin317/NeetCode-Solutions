"""
Problem: LeetCode 215 - Kth Largest Element in an Array

Key Idea:
To find the kth largest element in an array, we can use a min-heap (priority queue) with a maximum size of k. As we iterate through the array, we push elements into the min-heap. If the size of the heap exceeds k, we remove the smallest element. The top element of the min-heap will be the kth largest element.

Time Complexity:
- Building the min-heap: The time complexity of building the min-heap is O(k), where k is the maximum size of the heap.
- Adding elements: The time complexity of adding an element to the min-heap is O(n * log k), where n is the length of the array and k is the maximum size of the heap.

Space Complexity:
- The space complexity is O(k), where k is the maximum size of the min-heap.
"""

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

    # quickselect
    def quickselect(arr, k):
            pivot = arr[0]
            l = []
            r = []
            e = []
            for i in arr:
                if i < pivot:
                    r.append(i)
                elif i > pivot:
                    l.append(i)
                else:
                    e.append(i)
            if k <= len(l):
                return quickselect(l,k)
            elif k > (len(l)+ len(e)):
                return quickselect(r, k - len(l) - len(e))
            else:
                return pivot

    # bucket sort
    def bucketSort()
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1
        
        remain = k
        
        for num in range(len(count) -1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1