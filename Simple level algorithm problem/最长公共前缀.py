
# 问题：
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
# 说明: 所有输入只包含小写字母 a-z 。


class CommonPrefixProblem(object):
    @staticmethod
    def palindrome(str_list):
        temp_str = ""
        for i in zip(*str_list):
            if len(set(i)) == 1:
                temp_str += i[0]
            else:
                break
        print(temp_str)


str_array = ["flower", "flow", "flight"]
CommonPrefixProblem().palindrome(str_array)


# zip函数：
# >>>a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]

