"""
Problem: LeetCode 347 - Top K Frequent Elements

Key Idea:
To find the k most frequent elements in the given list, we can use a hash map (dictionary in Python) to keep track of the frequency of each element. We then use a min-heap (priority queue) to keep the k most frequent elements at the top. We traverse the list once to build the frequency map, and then we traverse the map to keep the k most frequent elements in the min-heap.

Time Complexity:
The time complexity of this approach is O(n + k*log(n)), where n is the number of elements in the input list. Building the frequency map takes O(n) time, and inserting k elements into the min-heap takes O(k*log(n)) time.

Space Complexity:
The space complexity is O(n) because we need to store the frequency map of all elements in the input list. Additionally, the min-heap will also have a space complexity of O(n) in the worst case if all elements are unique.
"""

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        min_heap = []
        for num, frequency in frequency_map.items():
            heapq.heappush(min_heap, (frequency, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for frequency, num in min_heap]


"""
can be done with quickselect as well
avg case of O(N)
"""

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for x in nums:
            counts[x] = counts.setdefault(x, 0) + 1
        
        counter = list(counts.items())
        
        # counter is a list of tuples as: [(1,1), (2,1), (3,2)] if arr was [1,3,2,3]

        def quickSelect(l, r):
            if l == r:
                return counter[:k]
            pivot = r
            start = l

            for idx in range(l, r+1):
                if counter[idx][1] > counter[pivot][1]:
                    counter[start], counter[idx] = counter[idx], counter[start] 

                    start += 1
            counter[start], counter[r] = counter[r], counter[start]
            
            if start < k:
                # need more elements so include from right
                return quickSelect(start+1, r)

            elif start == k:
                return counter[:k]

            else:
                return quickSelect(l, start - 1)

        
        ans = quickSelect(0, len(counter)-1)
        res = []
        for value in ans:
            res.append(value[0])

        return res