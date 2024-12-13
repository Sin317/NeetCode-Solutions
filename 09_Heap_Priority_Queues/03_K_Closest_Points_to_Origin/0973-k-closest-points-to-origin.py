"""
Problem: LeetCode 973 - K Closest Points to Origin

Key Idea:
To find the k closest points to the origin, we can calculate the distance of each point from the origin and use a min-heap (priority queue) to keep track of the k closest points. As we iterate through the points, we push each point into the min-heap. If the size of the heap exceeds k, we remove the farthest point. The remaining points in the heap will be the k closest points.

Time Complexity:
- Calculating distances: The time complexity of calculating the Euclidean distance for each point is O(n), where n is the number of points.
- Pushing and popping elements: The time complexity of each push and pop operation in the min-heap is O(log k), where k is the number of closest points we want.

Space Complexity:
- The space complexity is O(k), where k is the number of closest points we want to find. This is due to the space required to store the min-heap.
"""

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        min_heap = [(distance(point), point) for point in points]
        heapq.heapify(min_heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result

    # quickselect since we want k closest points -> so sorted in ascending order

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
            
        distances = [squared_distance(points[i]) for i in range(len(points))]
        def quickselect(left, right):
            pivot_idx = right
            pivot = distances[pivot_idx]
            start = left
            if left > right:
                return points[:left]
            for idx in range(left, right):
                if distances[idx] < pivot:
                    distances[idx], distances[start] = distances[start], distances[idx]
                    points[idx], points[start] = points[start], points[idx]
                    start += 1

            # swap the pivot with the right elem
            distances[start], distances[pivot_idx] = distances[pivot_idx], distances[start]
            points[start], points[pivot_idx] = points[pivot_idx], points[start]
            if start < k:
                # need more elems on lef
                return quickselect(start + 1, right)

            elif start == k:
                # we have enough so return the points
                return points[:k]
            else:
                return quickselect(left, start - 1)

        return quickselect(0, len(points)-1)
