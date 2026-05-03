def Solution(nums, target):
    for i in range(len(nums) - 1):
        for j in range((len(nums) - 1), i, -1):
            sum = nums[i] + nums[j]

            if (sum == target):
                return i,j
            