class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1

        frequencies = list(count.items())
            
        frequencies.sort(key=lambda x: x[1], reverse=True)
        answer = []

        for i in range(k):
            answer.append(frequencies[i][0])

        return answer

            

        