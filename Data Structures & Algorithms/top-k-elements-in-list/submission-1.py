class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        
        result = sorted(d.items(), key=lambda item: item[1], reverse=True)

        answer = []
        for i in range(k):
            answer.append(result[i][0])
        return answer