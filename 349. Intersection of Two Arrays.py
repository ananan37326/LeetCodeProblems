class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        vals = set(nums1)

        res = []

        for num in nums2:
            if num in vals:
                res.append(num)
                vals.remove(num)

        return res
        