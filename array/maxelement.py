class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     last = len(nums) - 1
    #     sorted = nums.sort()
    #     print(sorted[last]/2)

    # nums = [2,2,1,1,3,4,2]
    # output: 2
    # hashmaps are good at counting
    def majorityElement(self, nums: List[int]) -> int:
        # sums = {}
        # for n in nums:
        #   if n not in sums:
        #     sums[n] = 1
        #   else:
        #     sums[n] += 1

        #   if sums[n] > len(nums)/2:
        #     return n

        # or

        return sorted(nums)[len(nums)//2]
