import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)

        min_heap = []
        for n, f in freq_map.items():
            heapq.heappush(min_heap, (f, n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        for e in min_heap:
            res.append(e[1])
        return res