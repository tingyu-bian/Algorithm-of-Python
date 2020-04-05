
# 问题：
# 给你一个数组nums和一个值val，你需要原地移除所有数值等于val的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用O(1)额外空间并原地修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 示例 1:
# 给定 nums = [3,2,2,3], val = 3,
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
# 你不需要考虑数组中超出新长度后面的元素。
#
# 示例 2:
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
# 注意这五个元素可为任意顺序。
# 你不需要考虑数组中超出新长度后面的元素。
#


class RemoveElementProblem:
    @staticmethod
    def remove_element(nums, val):
        length = len(nums)
        i = 0
        j = 0
        while j < length:
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        return i


array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
tag = 2
RemoveElementProblem.remove_element(array, tag)

# 思路：
# 设置双指针 i 和 j，其中，j 用于寻找非 val 元素，来覆盖 i 所指向的元素。
# 初始时：设 i = 0, j = 0
# 遍历数组：
# 若 nums[j] != val：
# 把 j 的值赋给 i：nums[i] = nums[j]
# 同步增长双指针：i = i + 1, j = j + 1
# 若 nums[j] == val：
# j 变为快指针：j = j + 1，寻找下一个非 val 元素
#
