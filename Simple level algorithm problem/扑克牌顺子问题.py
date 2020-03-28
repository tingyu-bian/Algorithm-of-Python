
# 问题：
# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。


class Solution:
    @staticmethod
    def iscontinuous(numbers):
        if len(numbers) < 5:
            return False
        # 计算0的个数
        zeros_num = numbers.count(0)
        # 排序
        numbers.sort()
        # 序列中间隔的值初始化为0
        sum_gap = 0
        # 遍历非0部分的递增序列
        for i in range(zeros_num, len(numbers) - 1):
            small = numbers[i]
            big = numbers[i + 1]
            # 当前与下一个值的比较，若相等则说明存在对子
            if small == big:
                return False
            else:
                # 若不同，则得到二者的差再减1，若为0则说明连续，否则二者之间存在空缺
                sum_gap += (big-small - 1)
                # 判断0的个数及序列中非0部分间隔值，若0不小于间隔值，则说明满足连续条件
        if zeros_num >= sum_gap:
            return True
        else:
            return False


numbers_list = [0, 3, 5, 7, 0]
solution = Solution()
print(solution.iscontinuous(numbers_list))





