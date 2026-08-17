class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Using BruteForce
        '''
        maximum = []
        n=len(nums)
        for i in range(n-k+1):
            maximum.append(max(list(nums[i:i+k])))
        return maximum
        '''

        dq = deque()
        ans = []
        left = 0

        for right in range(len(nums)):

            # Rule 1: Remove smaller values
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] < left:
                dq.popleft()

            if right + 1 >= k:
                ans.append(nums[dq[0]])
                left += 1

        return ans
            






