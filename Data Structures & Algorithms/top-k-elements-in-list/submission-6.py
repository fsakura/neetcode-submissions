import heapq
class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
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
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in freq_map.items():
            buckets[f].append(n)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res