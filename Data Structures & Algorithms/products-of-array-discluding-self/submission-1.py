class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for _ in range(len(nums))]
        post = [1 for _ in range(len(nums))]

        # create pre
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        # create post
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        result = []
        # now get the product of these two
        for i in range(len(pre)):
            result.append(pre[i]*post[i])
        return result


