#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
#
# 示例 1: 
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
#输出: [5,6,7,1,2,3,4]
#解释:
#向右旋转 1 步: [7,1,2,3,4,5,6]
#向右旋转 2 步: [6,7,1,2,3,4,5]
#向右旋转 3 步: [5,6,7,1,2,3,4]
# 
#
# 示例 2: 
#
# 输入: [-1,-100,3,99] 和 k = 2
#输出: [3,99,-1,-100]
#解释: 
#向右旋转 1 步: [99,-1,-100,3]
#向右旋转 2 步: [3,99,-1,-100] 
#
# 说明: 
#
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
# 要求使用空间复杂度为 O(1) 的 原地 算法。 
# 
# Related Topics 数组



#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        array_length = len(nums)
        if array_length == 1 or k % array_length == 0:
            return
        count = 0
        cur_index = 0
        new_index = 0
        cur_num = nums[cur_index]

        while count < array_length:
            new_index = (new_index + k) % array_length
            tmp = nums[new_index]
            nums[new_index] = cur_num
            if new_index == cur_index:
                cur_index = (cur_index + 1) % array_length
                cur_num = nums[cur_index]
                new_index = cur_index
            else:
                cur_num = tmp

            count += 1

#leetcode submit region end(Prohibit modification and deletion)
