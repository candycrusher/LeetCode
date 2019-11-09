#给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。 
#
# 说明: 
#
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。 
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
# 
#
# 示例: 
#
# 输入:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6],       n = 3
#
#输出: [1,2,2,3,5,6] 
# Related Topics 数组 双指针



#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_index = m + n - 1
        m_index = m - 1
        n_index = n - 1
        while m_index >= 0 and n_index >= 0:
            if nums1[m_index] <= nums2[n_index]:
                nums1[total_index] = nums2[n_index]
                n_index -= 1
            else:
                nums1[total_index] = nums1[m_index]
                m_index -= 1
            total_index -= 1

        if m_index < 0:
            while total_index >= 0:
                nums1[total_index] = nums2[n_index]
                n_index -= 1
                total_index -= 1

#leetcode submit region end(Prohibit modification and deletion)
