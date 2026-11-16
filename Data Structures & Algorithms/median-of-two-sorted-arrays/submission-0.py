class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        # Number of elements required on the left
        half = (m + n + 1) // 2

        low = 0
        high = m

        while low <= high:

            # Find partition positions
            i = (low + high) // 2
            j = half - i

            # Four boundary elements
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Check if partition is valid
            if left1 <= right2 and left2 <= right1:

                # Odd total number of elements
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total number of elements
                return (max(left1, left2) + min(right1, right2)) / 2

            # Too many elements from nums1 on the left
            elif left1 > right2:
                high = i - 1

            # Too few elements from nums1 on the left
            else:
                low = i + 1

        return 0.0